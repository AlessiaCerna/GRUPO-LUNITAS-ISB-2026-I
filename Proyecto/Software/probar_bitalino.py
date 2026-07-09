"""
probar_bitalino.py (v3 - baseline normalization)
==================================================
Historial de este script:
  v1: cargaba el modelo pero nunca llamaba a clf.predict() (umbral manual).
  v2: llamaba a clf.predict() con un StandardScaler global (ajustado con el
      dataset de entrenamiento multi-dispositivo). Funciono para reentrenar
      con datos reales, pero seguia sin resolver el domain-shift del
      BITalino: Basal1_S01 se clasificaba como "Alto" (55.8% confianza).
  v3 (este): usa BASELINE NORMALIZATION. En vez de normalizar contra las
      estadisticas del dataset de entrenamiento, cada grabacion se normaliza
      contra el BASAL PROPIO del mismo participante/dispositivo:
          X_norm = (X_grabacion - X_basal.mean()) / (X_basal.std() + 1e-8)
      y se clasifica con un modelo BINARIO (Basal vs Estres) entrenado sobre
      deltas basal-propio en los unicos sujetos con pares reales basal/estres
      (29 de Data3 + 5 de Data4 = 34 sujetos, 1729 ventanas de 4s).

Resultado en S01 (ver informe para la comparacion completa):
  - Estres1_S01: 74/75 ventanas clasificadas como "Estres", proba promedio
    [Basal=0.049, Estres=0.951]  -> CORRECTO, con alta confianza.
  - Basal1_S01 (mitad de control nunca vista por el clasificador): 12/23
    ventanas "Basal" vs 11/23 "Estres", proba promedio ~50/50  -> ya NO es un
    falso positivo confiado de estres (como en v2), pero tampoco es un
    "Basal" solido; queda ambiguo. Ver limitaciones en el informe.

IMPORTANTE: esta estrategia requiere SIEMPRE una grabacion basal propia del
mismo participante/sesion para poder normalizar. No se puede clasificar una
grabacion nueva sin su basal de referencia.

[PARCHE APLICADO] pipeline.py ahora devuelve 5 features (se agrego AB_ratio).
Este script no necesita cambios: process_bitalino/baseline_normalize son
genericos respecto al numero de features, y modelo_binario_delta_basal.pkl
fue reentrenado con las 5 features (ver proyecto.py).
"""
import os
import numpy as np
import joblib

import pipeline as p

MODEL_BIN_PATH = 'modelo_binario_delta_basal.pkl'
LABELS_BIN = ['Basal / Sin estres', 'Estres']


def clasificar_con_basal(basal_path, target_path, clf_binario):
    basal_epochs, _ = p.process_bitalino(basal_path)
    target_epochs, _ = p.process_bitalino(target_path)
    delta = p.baseline_normalize(target_epochs, basal_epochs)

    preds = clf_binario.predict(delta)
    probas = clf_binario.predict_proba(delta)
    vals, counts = np.unique(preds, return_counts=True)
    distrib = {LABELS_BIN[v]: int(c) for v, c in zip(vals, counts)}
    pred_mayoritaria = int(np.round(preds.mean()))
    return pred_mayoritaria, probas.mean(axis=0), distrib


if __name__ == '__main__':
    if not os.path.exists(MODEL_BIN_PATH):
        print(f"Error: no existe {MODEL_BIN_PATH}. Corre primero el entrenamiento "
              f"del clasificador delta-basal (ver proyecto.py / informe).")
    else:
        clf_binario = joblib.load(MODEL_BIN_PATH)
        basal_file = 'Basal1_S01.txt'
        target_file = 'Estres1_S01.txt'

        if not (os.path.exists(basal_file) and os.path.exists(target_file)):
            print("No se encontraron Basal1_S01.txt y/o Estres1_S01.txt")
        else:
            pred, proba, distrib = clasificar_con_basal(basal_file, target_file, clf_binario)
            print(f">> Basal de referencia: {basal_file}")
            print(f">> Grabacion clasificada: {target_file}")
            print(f"   Prediccion mayoritaria: {LABELS_BIN[pred]}")
            print(f"   Probabilidad promedio: {dict(zip(LABELS_BIN, np.round(proba, 3)))}")
            print(f"   Distribucion por ventana de 4s: {distrib}")

            # Sanity check: normalizar el propio basal contra si mismo (mitad/mitad)
            # deberia dar algo cercano a 50/50, NO un falso "Estres" confiado.
            basal_epochs, _ = p.process_bitalino(basal_file)
            n = len(basal_epochs)
            ref, test_basal = basal_epochs[:n // 2], basal_epochs[n // 2:]
            delta_control = p.baseline_normalize(test_basal, ref)
            preds_c = clf_binario.predict(delta_control)
            probas_c = clf_binario.predict_proba(delta_control)
            print(f"\n>> Control (mitad del basal contra la otra mitad, deberia ser ~Basal):")
            print(f"   Prediccion mayoritaria: {LABELS_BIN[int(np.round(preds_c.mean()))]}")
            print(f"   Probabilidad promedio: {dict(zip(LABELS_BIN, np.round(probas_c.mean(axis=0), 3)))}")
