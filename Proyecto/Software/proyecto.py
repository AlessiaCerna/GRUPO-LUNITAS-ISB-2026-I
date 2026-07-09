"""
proyecto.py - Entrenamiento del modelo multiclase de estres EEG (v2)
=====================================================================
[PARCHE APLICADO] pipeline.py ahora devuelve 5 features
(FAA, TBR, Alpha_rel, Beta_rel, AB_ratio) en vez de 4. Ver
parche_ratio_alpha_beta.py y la nota en pipeline.py. Este script y los
.pkl que genera fueron reentrenados con las 5 features.
Reescritura completa de este script. La version anterior estaba incompleta
(las funciones process_edf_clinical y process_csv_precalculated eran
placeholders vacios) y referenciaba variables (path_data2, path_data4) que
nunca se definian en el propio archivo. Ademas el .pkl que se distribuia en
la carpeta NO correspondia a esta version del script (distinto numero de
clases, distintos hiperparametros): no habia trazabilidad.

Este script:
  1. Usa el modulo pipeline.py (extraccion de biomarcadores FAA/TBR/Alpha_rel/
     Beta_rel, con el filtro Butterworth orden 4 filtfilt 1-45Hz, ventanas de
     4s y PSD Welch nperseg=2*fs especificados para el proyecto).
  2. Incorpora las 4 fuentes de datos:
       - Data3 (eego, Fp1/Fp2 reales, 2000 Hz)       -> PRIMARIA
       - Data4 (clinico 10-20, Fp1/Fp2 reales, 200Hz) -> PRIMARIA
       - Data1 (Emotiv AF3/AF4, aproximacion frontal) -> SECUNDARIA
       - Data2 (Muse, bandas precalculadas, con        -> SECUNDARIA
                etiqueta REAL de estres por sujeto
                tomada del Excel de evaluacion)
  3. Divide train/test por SUJETO/GRABACION (GroupShuffleSplit + GroupKFold),
     nunca por ventana, para que no haya fuga de datos entre train y test.
  4. Escala features con StandardScaler (ajustado SOLO con train) antes de
     entrenar el RandomForest.
  5. Reporta accuracy con validacion cruzada de 5 folds agrupada, ademas del
     resultado en el split de test final.
  6. Guarda modelo, scaler, matriz de confusion y curvas ROC.

IMPORTANTE (leer antes de interpretar resultados):
  El accuracy obtenido en el split por sujeto (~0.55-0.60) es MUCHO menor que
  el que mostraba el .pkl anterior (que llegaba a ~98% en la matriz de
  confusion vieja). Eso NO es una regresion: el modelo anterior "acertaba"
  porque estaba aprendiendo a distinguir el DISPOSITIVO de origen (una clase
  tenia 2617 muestras de una sola fuente), no el nivel de estres. Este nuevo
  resultado es mas bajo pero es el que refleja de verdad la dificultad de
  generalizar biomarcadores de estres entre dispositivos EEG distintos.
"""
import os
import numpy as np
from sklearn.model_selection import GroupShuffleSplit, GroupKFold
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score, roc_curve, auc
from sklearn.preprocessing import label_binarize
import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pipeline as p

# ------------------------------------------------------------------
# RUTAS (relativas a la carpeta del proyecto; ajustar si se mueve de disco)
# ------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_DATA1 = os.path.join(BASE_DIR, 'Data', 'Data1')
PATH_DATA2 = os.path.join(
    BASE_DIR, 'Data', 'Data2',
    'A Comprehensive Dataset of EEG Recordings Capturing Student Stress Responses During Exams', 'Data')
PATH_DATA2_XLSX = os.path.join(
    BASE_DIR, 'Data', 'Data2',
    'A Comprehensive Dataset of EEG Recordings Capturing Student Stress Responses During Exams',
    'Assessment result of stress level.xlsx')
PATH_DATA3_ZIP = os.path.join(BASE_DIR, 'Data', 'Data3', 'EEG and HF data under stress',
                               'EEG and HF data under stress.zip')
PATH_DATA3_EXTRACTED = os.path.join(BASE_DIR, 'Data', 'Data3', '_extracted')
PATH_DATA4 = os.path.join(BASE_DIR, 'Data', 'Data4', 'Chronic Stress')

MODEL_OUT = os.path.join(BASE_DIR, 'modelo_estres_multiclase_v2.pkl')
SCALER_OUT = os.path.join(BASE_DIR, 'scaler_estres_v2.pkl')
CM_FIG_OUT = os.path.join(BASE_DIR, 'matriz_confusion_estres_v2.png')
ROC_FIG_OUT = os.path.join(BASE_DIR, 'roc_curves_estres_v2.png')

LABELS = ['Bajo/Sin estres', 'Moderado', 'Alto']
MODEL_BIN_OUT = os.path.join(BASE_DIR, 'modelo_binario_delta_basal.pkl')
LABELS_BIN = ['Basal/Sin estres', 'Estres']


def build_dataset():
    print(">> Procesando Data3 (eego, Fp1/Fp2 reales, PRIMARIA)...")
    p.ensure_data3_extracted(PATH_DATA3_ZIP, PATH_DATA3_EXTRACTED)
    X3, y3, g3 = p.process_eego_data3(PATH_DATA3_EXTRACTED, fs=2000.0)
    print(f"   {len(y3)} muestras (sujeto x condicion). Clases: {dict(zip(*np.unique(y3, return_counts=True)))}")

    print(">> Procesando Data4 (clinico 10-20, Fp1/Fp2 reales, PRIMARIA)...")
    X4, y4, g4 = p.load_data4(PATH_DATA4)
    print(f"   {len(y4)} muestras. Clases: {dict(zip(*np.unique(y4, return_counts=True)))}")

    print(">> Procesando Data1 (Emotiv AF3/AF4, SECUNDARIA, aproximacion frontal)...")
    X1, y1, g1 = p.load_data1(PATH_DATA1)
    print(f"   {len(y1)} muestras. Clases: {dict(zip(*np.unique(y1, return_counts=True)))}")

    print(">> Procesando Data2 (Muse, SECUNDARIA, etiqueta real desde Excel)...")
    X2, y2, g2 = p.load_data2(PATH_DATA2, PATH_DATA2_XLSX)
    print(f"   {len(y2)} muestras. Clases: {dict(zip(*np.unique(y2, return_counts=True)))}")

    X = np.vstack([X3, X4, X1, X2])
    y = np.concatenate([y3, y4, y1, y2])
    groups = np.concatenate([g3, g4, g1, g2])
    source = np.concatenate([['data3'] * len(y3), ['data4'] * len(y4),
                              ['data1'] * len(y1), ['data2'] * len(y2)])

    print(f"\n>> Dataset combinado: {X.shape[0]} muestras, clases: {dict(zip(*np.unique(y, return_counts=True)))}")
    for cls in [0, 1, 2]:
        mask = y == cls
        srcs, counts = np.unique(source[mask], return_counts=True)
        print(f"   clase {cls} ({LABELS[cls]}): {dict(zip(srcs, counts))}")
    return X, y, groups


def cross_validate(X, y, groups, n_splits=5):
    print(f"\n>> Validacion cruzada agrupada por sujeto ({n_splits}-fold)...")
    gkf = GroupKFold(n_splits=n_splits)
    accs, f1s = [], []
    for fold, (tr, te) in enumerate(gkf.split(X, y, groups)):
        scaler = StandardScaler()
        Xtr = scaler.fit_transform(X[tr])
        Xte = scaler.transform(X[te])
        clf = RandomForestClassifier(n_estimators=300, class_weight='balanced',
                                      max_depth=8, random_state=42)
        clf.fit(Xtr, y[tr])
        pred = clf.predict(Xte)
        acc = accuracy_score(y[te], pred)
        f1 = f1_score(y[te], pred, average='macro')
        accs.append(acc)
        f1s.append(f1)
        print(f"   fold {fold}: n_test={len(te)} accuracy={acc:.3f} f1_macro={f1:.3f}")
    print(f"\n   Accuracy media: {np.mean(accs):.3f} +/- {np.std(accs):.3f}  (nivel de azar 3 clases = 0.333)")
    print(f"   F1-macro media: {np.mean(f1s):.3f} +/- {np.std(f1s):.3f}")
    return accs, f1s


def train_final_model(X, y, groups):
    print("\n>> Entrenando modelo final (split 75/25 por sujeto, sin fuga de datos)...")
    gss = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
    train_idx, test_idx = next(gss.split(X, y, groups))
    assert len(set(groups[train_idx]) & set(groups[test_idx])) == 0, "FUGA DE DATOS: hay sujetos en ambos splits"

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X[train_idx])
    X_test_s = scaler.transform(X[test_idx])
    y_train, y_test = y[train_idx], y[test_idx]

    clf = RandomForestClassifier(n_estimators=300, class_weight='balanced',
                                  max_depth=8, random_state=42)
    clf.fit(X_train_s, y_train)

    y_pred = clf.predict(X_test_s)
    y_proba = clf.predict_proba(X_test_s)

    print(classification_report(y_test, y_pred, target_names=LABELS, zero_division=0))
    cm = confusion_matrix(y_test, y_pred, labels=[0, 1, 2])
    print("Matriz de confusion (test set, holdout por sujeto):\n", cm)
    print("Importancia de features [FAA, TBR, Alpha_rel, Beta_rel, AB_ratio]:", clf.feature_importances_)

    plot_confusion_matrix(cm)
    plot_roc_curves(y_test, y_proba)

    joblib.dump(clf, MODEL_OUT)
    joblib.dump(scaler, SCALER_OUT)
    print(f"\n[V] Modelo guardado en: {MODEL_OUT}")
    print(f"[V] Scaler guardado en: {SCALER_OUT}")
    return clf, scaler


def plot_confusion_matrix(cm):
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(cm, cmap='Blues')
    ax.set_xticks(range(3)); ax.set_yticks(range(3))
    ax.set_xticklabels(LABELS); ax.set_yticklabels(LABELS)
    ax.set_xlabel('Predicted label'); ax.set_ylabel('True label')
    ax.set_title('Matriz de Confusion v2 - Modelo Multi-Dispositivo\n(split por sujeto, sin fuga de datos)')
    for i in range(3):
        for j in range(3):
            ax.text(j, i, cm[i, j], ha='center', va='center',
                    color='white' if cm[i, j] > cm.max() / 2 else 'black')
    plt.colorbar(im)
    plt.tight_layout()
    plt.savefig(CM_FIG_OUT, dpi=150)
    plt.close(fig)


def plot_roc_curves(y_test, y_proba):
    y_test_bin = label_binarize(y_test, classes=[0, 1, 2])
    fig, ax = plt.subplots(figsize=(6, 5))
    colors = ['#6FB6A4', '#E0A03A', '#D8564B']
    for i, name in enumerate(LABELS):
        fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_proba[:, i])
        roc_auc = auc(fpr, tpr)
        ax.plot(fpr, tpr, color=colors[i], label=f'{name} (AUC={roc_auc:.2f})')
    ax.plot([0, 1], [0, 1], 'k--', alpha=0.4)
    ax.set_xlabel('False Positive Rate'); ax.set_ylabel('True Positive Rate')
    ax.set_title('Curvas ROC One-vs-Rest - Modelo v2')
    ax.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig(ROC_FIG_OUT, dpi=150)
    plt.close(fig)


def build_delta_dataset():
    """
    Construye el dataset para el clasificador binario BASAL vs ESTRES usando
    baseline normalization: solo se pueden usar sujetos que tengan AMBAS
    grabaciones (basal Y estres) del MISMO participante/dispositivo, porque
    la normalizacion requiere calcular mean/std del basal propio.

    Fuentes utilizables (unicas con pares reales basal/estres):
      - Data3 (eego): 29 sujetos, EO=basal, AC1+AC2=estres
      - Data4 (clinico): 5 sujetos con ambos archivos (Female1-4, Male1)
    Data1 y Data2 NO se usan aqui: no tienen una grabacion basal pareada por
    sujeto (son sesiones unicas por protocolo/persona).

    El basal de cada sujeto se parte a la mitad: la primera mitad se usa
    SOLO para calcular mean/std de referencia, la segunda mitad se trata
    como una "grabacion basal nueva" (para no evaluar contra si misma).
    """
    print(">> Construyendo dataset delta-basal (Data3 + Data4 con pares reales)...")
    p.ensure_data3_extracted(PATH_DATA3_ZIP, PATH_DATA3_EXTRACTED)
    d3 = p.process_eego_data3_epochs(PATH_DATA3_EXTRACTED, fs=2000.0)
    d4 = p.load_data4_paired_epochs(PATH_DATA4)
    all_subj = {**d3, **d4}
    print(f"   sujetos con par basal/estres real: {len(all_subj)} (Data3={len(d3)}, Data4={len(d4)})")

    X, y, groups = [], [], []
    eps = 1e-8
    for sid, data in all_subj.items():
        basal = data['basal']
        stress = data['stress']
        if len(basal) < 4:
            continue
        split = len(basal) // 2
        ref, test_basal = basal[:split], basal[split:]
        ref_mean, ref_std = ref.mean(axis=0), ref.std(axis=0)
        for e in test_basal:
            X.append((e - ref_mean) / (ref_std + eps)); y.append(0); groups.append(sid)
        for e in stress:
            X.append((e - ref_mean) / (ref_std + eps)); y.append(1); groups.append(sid)

    X, y, groups = np.array(X), np.array(y), np.array(groups)
    print(f"   dataset delta: {X.shape[0]} ventanas, clases: {dict(zip(*np.unique(y, return_counts=True)))}")
    return X, y, groups


def train_delta_classifier(X, y, groups, n_splits=5):
    """Entrena y valida el clasificador binario basal-vs-estres sobre
    features normalizadas contra el basal propio de cada sujeto. A
    diferencia del modelo multiclase, aqui NO se usa StandardScaler: el
    baseline normalization ya deja las features en una escala comparable
    entre sujetos/dispositivos."""
    print(f"\n>> Validacion cruzada agrupada por sujeto ({n_splits}-fold) - clasificador delta-basal...")
    gkf = GroupKFold(n_splits=n_splits)
    accs, f1s = [], []
    for fold, (tr, te) in enumerate(gkf.split(X, y, groups)):
        clf = RandomForestClassifier(n_estimators=300, class_weight='balanced', max_depth=6, random_state=42)
        clf.fit(X[tr], y[tr])
        pred = clf.predict(X[te])
        acc = accuracy_score(y[te], pred)
        f1 = f1_score(y[te], pred, average='macro')
        accs.append(acc); f1s.append(f1)
        print(f"   fold {fold}: n_test={len(te)} accuracy={acc:.3f} f1_macro={f1:.3f}")
    print(f"\n   Accuracy media: {np.mean(accs):.3f} +/- {np.std(accs):.3f}  (azar binario = 0.500)")
    print(f"   F1-macro media: {np.mean(f1s):.3f} +/- {np.std(f1s):.3f}")

    gss = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
    train_idx, test_idx = next(gss.split(X, y, groups))
    assert len(set(groups[train_idx]) & set(groups[test_idx])) == 0

    clf_final = RandomForestClassifier(n_estimators=300, class_weight='balanced', max_depth=6, random_state=42)
    clf_final.fit(X[train_idx], y[train_idx])
    y_pred = clf_final.predict(X[test_idx])
    print("\n   Reporte (holdout 25% por sujeto):")
    print(classification_report(y[test_idx], y_pred, target_names=LABELS_BIN, zero_division=0))
    print("   Matriz de confusion:\n", confusion_matrix(y[test_idx], y_pred, labels=[0, 1]))

    joblib.dump(clf_final, MODEL_BIN_OUT)
    print(f"\n[V] Clasificador delta-basal guardado en: {MODEL_BIN_OUT}")
    return clf_final


def validate_bitalino_s01_baseline(clf_binario):
    """Valida la estrategia de baseline normalization (v3) con S01: usa la
    PRIMERA mitad de Basal1_S01 como referencia, la SEGUNDA mitad como
    control (deberia salir Basal), y Estres1_S01 completo (deberia salir
    Estres)."""
    print("\n>> Validacion con S01 usando BASELINE NORMALIZATION (v3)...")
    basal_path = os.path.join(BASE_DIR, 'Basal1_S01.txt')
    target_path = os.path.join(BASE_DIR, 'Estres1_S01.txt')
    if not (os.path.exists(basal_path) and os.path.exists(target_path)):
        print("   [X] No se encontraron Basal1_S01.txt / Estres1_S01.txt")
        return

    basal_epochs, _ = p.process_bitalino(basal_path)
    target_epochs, _ = p.process_bitalino(target_path)
    n = len(basal_epochs)
    ref, test_basal = basal_epochs[:n // 2], basal_epochs[n // 2:]

    delta_control = p.baseline_normalize(test_basal, ref)
    pred_c = clf_binario.predict(delta_control)
    proba_c = clf_binario.predict_proba(delta_control)
    print(f"   Control (2da mitad del basal, esperado Basal): "
          f"pred={LABELS_BIN[int(np.round(pred_c.mean()))]}  "
          f"proba={dict(zip(LABELS_BIN, np.round(proba_c.mean(axis=0), 3)))}")

    delta_estres = p.baseline_normalize(target_epochs, ref)
    pred_e = clf_binario.predict(delta_estres)
    proba_e = clf_binario.predict_proba(delta_estres)
    print(f"   Estres1_S01 (esperado Estres): "
          f"pred={LABELS_BIN[int(np.round(pred_e.mean()))]}  "
          f"proba={dict(zip(LABELS_BIN, np.round(proba_e.mean(axis=0), 3)))}")


def validate_bitalino_s01(clf, scaler):
    print("\n>> Validacion con datos reales de S01 (NeuroBIT/BITalino)...")
    for fname, expected in [('Basal1_S01.txt', 'Bajo/Sin estres'), ('Estres1_S01.txt', 'Alto')]:
        fpath = os.path.join(BASE_DIR, fname)
        if not os.path.exists(fpath):
            print(f"   [X] No se encontro {fname}")
            continue
        feats_win, feats_avg = p.process_bitalino(fpath)
        Xs = scaler.transform(feats_avg.reshape(1, -1))
        pred = clf.predict(Xs)[0]
        proba = clf.predict_proba(Xs)[0]
        print(f"   {fname} (esperado: {expected})")
        print(f"     FAA={feats_avg[0]:.3f}  TBR={feats_avg[1]:.3f}  "
              f"Alpha_rel={feats_avg[2]:.3f}  Beta_rel={feats_avg[3]:.3f}  "
              f"AB_ratio={feats_avg[4]:.3f}")
        print(f"     Prediccion del modelo: {LABELS[pred]}  |  proba: "
              f"{dict(zip(LABELS, np.round(proba, 3)))}")


if __name__ == '__main__':
    # --- Modelo v2: multiclase (Bajo/Moderado/Alto), StandardScaler global ---
    X, y, groups = build_dataset()
    cross_validate(X, y, groups, n_splits=5)
    clf, scaler = train_final_model(X, y, groups)
    validate_bitalino_s01(clf, scaler)

    # --- Modelo v3: binario (Basal/Estres), baseline normalization ---
    # Estrategia que SI corrige el domain-shift de S01 (ver informe): usa el
    # basal propio de cada sujeto/dispositivo como referencia de escala en
    # vez de un StandardScaler global.
    Xd, yd, groupsd = build_delta_dataset()
    clf_bin = train_delta_classifier(Xd, yd, groupsd, n_splits=5)
    validate_bitalino_s01_baseline(clf_bin)
