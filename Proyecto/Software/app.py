import streamlit as st
import numpy as np
import joblib

import pipeline as p

# ============================================================
# CONFIGURACION
# ============================================================
st.set_page_config(page_title="NeuroCalm . EEG Stress Monitor", page_icon="\U0001F9E0", layout="wide")

# --- Modelo v2 (multiclase, StandardScaler global) ---
# Se mantiene disponible para referencia/comparacion, pero YA NO es el
# clasificador principal: con datos BITalino reales (S01) el StandardScaler
# global no corrige el domain-shift entre dispositivos (el basal se
# clasificaba como "Alto" con 55.8% de confianza). Ver informe del proyecto.
modelo_v2 = joblib.load('modelo_estres_multiclase_v2.pkl')
scaler_v2 = joblib.load('scaler_estres_v2.pkl')
LABELS = ['Sin estres / Bajo', 'Moderado', 'Alto']

# --- Modelo v3 (binario, baseline normalization) - CLASIFICADOR PRINCIPAL ---
# Entrenado sobre deltas (grabacion - basal_propio)/(std_basal_propio) usando
# los 34 sujetos de Data3+Data4 que tienen pares reales basal/estres.
# Con S01 (BITalino real): Estres1_S01 -> "Estres" con 94.5% de confianza
# promedio (correcto). Requiere SIEMPRE una grabacion basal propia del mismo
# participante para poder normalizar -por eso la pagina pide 2 archivos-.
modelo_bin = joblib.load('modelo_binario_delta_basal.pkl')
LABELS_BIN = ['Basal / Sin estres', 'Estres']

# ============================================================
# TOKENS DE DISENO
# ============================================================
COLORS = {
    "bg": "#FAF8FC",
    "surface": "#FFFFFF",
    "ink": "#423A5E",
    "ink_soft": "#8783A6",
    "primary": "#9999CD",
    "primary_dark": "#6E70A8",
    "primary_soft": "#E4E1F4",
    "blue": "#8EB9E4",
    "mauve": "#C09CC8",
    "pink": "#DFCDE5",
    "accent": "#C09CC8",
    "green": "#6FB6A4",
    "amber": "#E0A03A",
    "red": "#D8564B",
}


def inject_css():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500;600&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    .stApp {{
        background: {COLORS['bg']};
    }}

    h1, h2, h3 {{
        font-family: 'Space Grotesk', sans-serif !important;
        color: {COLORS['primary_dark']} !important;
        letter-spacing: -0.01em;
    }}

    p, span, li, label {{
        color: {COLORS['ink']};
    }}

    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {COLORS['blue']} 0%, {COLORS['primary']} 55%, {COLORS['mauve']} 100%);
    }}
    [data-testid="stSidebar"] * {{
        color: {COLORS['ink']} !important;
    }}
    [data-testid="stSidebar"] hr {{
        border-color: rgba(66,58,94,0.18);
    }}

    [data-testid="stFileUploader"] section {{
        background: {COLORS['surface']};
        border: 1.5px dashed {COLORS['primary']}55;
        border-radius: 14px;
    }}

    .stButton>button {{
        background: {COLORS['primary_dark']};
        color: white;
        border-radius: 10px;
        border: none;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
        padding: 0.5rem 1.2rem;
    }}
    .stButton>button:hover {{
        background: {COLORS['ink']};
        color: white;
    }}

    .ncm-card {{
        background: {COLORS['surface']};
        border-radius: 16px;
        padding: 1.4rem 1.6rem;
        box-shadow: 0 4px 20px rgba(14, 92, 86, 0.08);
        border: 1px solid rgba(14, 92, 86, 0.06);
        height: 100%;
    }}

    .ncm-eyebrow {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.72rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: {COLORS['ink_soft']};
        margin-bottom: 0.35rem;
    }}

    .ncm-metric-value {{
        font-family: 'IBM Plex Mono', monospace;
        font-size: 2.1rem;
        font-weight: 600;
        color: {COLORS['primary_dark']};
    }}

    .ncm-metric-unit {{
        font-size: 1rem;
        color: {COLORS['ink_soft']};
        font-weight: 500;
        font-family: 'Inter', sans-serif;
    }}

    .ncm-badge {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.6rem 1.2rem;
        border-radius: 999px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        margin-top: 0.5rem;
    }}

    .ncm-hero {{
        background: linear-gradient(120deg, {COLORS['blue']} 0%, {COLORS['primary']} 50%, {COLORS['mauve']} 100%);
        border-radius: 20px;
        padding: 2.4rem 2.6rem;
        color: {COLORS['ink']};
    }}
    .ncm-hero h1 {{ color: {COLORS['ink']} !important; margin-bottom: 0.4rem; }}
    .ncm-hero p {{ color: {COLORS['ink']} !important; opacity: 0.85; font-size: 1.05rem; max-width: 640px; }}
    .ncm-hero .ncm-eyebrow {{ color: {COLORS['ink']} !important; opacity: 0.7; }}

    .ncm-wave-wrap {{
        overflow: hidden;
        width: 100%;
        line-height: 0;
        margin: 0.4rem 0 1.6rem 0;
    }}
    .ncm-wave-track {{
        display: inline-block;
        animation: ncm-scroll 6s linear infinite;
    }}
    @keyframes ncm-scroll {{
        from {{ transform: translateX(0); }}
        to {{ transform: translateX(-600px); }}
    }}

    .ncm-team-card {{
        background: {COLORS['surface']};
        border-radius: 16px;
        padding: 1.2rem 1.4rem;
        box-shadow: 0 4px 20px rgba(14, 92, 86, 0.08);
        display: flex;
        align-items: center;
        gap: 1rem;
    }}
    .ncm-avatar {{
        width: 44px; height: 44px; border-radius: 50%;
        background: {COLORS['primary_soft']};
        display: flex; align-items: center; justify-content: center;
        font-size: 1.3rem;
    }}
    </style>
    """, unsafe_allow_html=True)


def eeg_wave_svg(color=COLORS['accent']):
    seg = ("0,24 30,24 38,4 46,44 54,24 84,24 92,15 100,33 108,24 138,24 "
           "146,3 154,45 162,24 192,24 200,17 208,31 216,24 246,24 "
           "254,4 262,44 270,24 300,24 308,16 316,32 324,24")
    shifted = " ".join(f"{float(pt.split(',')[0]) + 300},{pt.split(',')[1]}" for pt in seg.split())
    return f"""
    <div class="ncm-wave-wrap">
      <div class="ncm-wave-track">
        <svg width="600" height="48" viewBox="0 0 600 48" xmlns="http://www.w3.org/2000/svg">
          <polyline points="{seg} {shifted}" fill="none" stroke="{color}"
            stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity="0.85"/>
        </svg>
      </div>
    </div>
    """


def metric_card(label, value, unit="", icon="\U0001F30A"):
    st.markdown(f"""
    <div class="ncm-card">
        <div class="ncm-eyebrow">{icon} {label}</div>
        <div class="ncm-metric-value">{value} <span class="ncm-metric-unit">{unit}</span></div>
    </div>
    """, unsafe_allow_html=True)


def status_badge(pred_class, proba, binario=True):
    """Badge basado UNICAMENTE en la salida del modelo, no en umbrales
    manuales. binario=True -> modelo v3 (Basal/Estres); binario=False ->
    modelo v2 de referencia (Bajo/Moderado/Alto)."""
    if binario:
        style = {
            0: (COLORS['green'], "#FFFFFF", "Basal / Sin estres", "\U0001F7E2"),
            1: (COLORS['red'], "#FFFFFF", "Estres", "\U0001F534"),
        }
    else:
        style = {
            0: (COLORS['green'], "#FFFFFF", "Sin estres / Bajo", "\U0001F7E2"),
            1: (COLORS['amber'], "#26210F", "Estres moderado", "\U0001F7E0"),
            2: (COLORS['red'], "#FFFFFF", "Estres alto", "\U0001F534"),
        }
    bg, fg, label, icon = style[pred_class]
    conf = proba[pred_class] * 100
    st.markdown(f"""
    <div class="ncm-badge" style="background:{bg};color:{fg};">
        <span>{icon}</span> {label} <span style="opacity:0.75;font-weight:500;">({conf:.0f}% confianza)</span>
    </div>
    """, unsafe_allow_html=True)


def page_header(eyebrow, title, subtitle=""):
    st.markdown(f'<div class="ncm-eyebrow">{eyebrow}</div>', unsafe_allow_html=True)
    st.markdown(f"<h1 style='margin-bottom:0.15rem;'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p style='color:{COLORS['ink_soft']};font-size:1.05rem;margin-top:0;'>{subtitle}</p>",
                    unsafe_allow_html=True)
    st.markdown(eeg_wave_svg(), unsafe_allow_html=True)


inject_css()

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("## \U0001F9E0 NeuroCalm")
    st.caption("EEG Stress Monitor")
    st.markdown("<hr/>", unsafe_allow_html=True)
    pagina = st.radio("Navegacion", ["Inicio", "Analisis EEG", "Resultados", "Equipo"],
                       label_visibility="collapsed")
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.caption("Sistema de apoyo para monitoreo de carga cognitiva mediante senales EEG.")
    st.caption("Modelo v2 - RandomForest, features estandarizadas (z-score), "
               "entrenado con datos multi-dispositivo (split por sujeto).")

# ============================================================
# LOGICA DE PROCESAMIENTO - ahora usa pipeline.py (mismas funciones que
# proyecto.py) y llama de verdad a modelo.predict()
# ============================================================
def procesar_y_clasificar_baseline(basal_file, target_file):
    """Estrategia principal (v3): baseline normalization + clasificador
    binario basal-vs-estres. Requiere el archivo basal del mismo participante."""
    basal_epochs, basal_avg = p.process_bitalino(basal_file)
    target_epochs, target_avg = p.process_bitalino(target_file)
    delta = p.baseline_normalize(target_epochs, basal_epochs)
    preds = modelo_bin.predict(delta)
    probas = modelo_bin.predict_proba(delta)
    pred_mayoritaria = int(np.round(preds.mean()))
    proba_media = probas.mean(axis=0)
    distrib = {LABELS_BIN[v]: int(c) for v, c in zip(*np.unique(preds, return_counts=True))}
    return target_avg, pred_mayoritaria, proba_media, distrib


def procesar_y_clasificar_v2(file):
    """Estrategia anterior (v2): modelo multiclase + StandardScaler global.
    Se deja disponible solo como referencia/comparacion en la UI.
    NOTA: modelo_v2/scaler_v2 NO fueron reentrenados con el parche AB_ratio
    (pipeline.py ahora devuelve 5 features); se usan solo las primeras 4
    (FAA, TBR, Alpha_rel, Beta_rel) para mantener compatibilidad con el
    .pkl viejo, ya que v2 es solo referencia y no el clasificador principal."""
    feats_win, feats_avg = p.process_bitalino(file)
    Xs = scaler_v2.transform(feats_avg[:4].reshape(1, -1))
    pred = int(modelo_v2.predict(Xs)[0])
    proba = modelo_v2.predict_proba(Xs)[0]
    return feats_avg, pred, proba


# ============================================================
# PAGINAS
# ============================================================
if pagina == "Inicio":
    st.markdown(f"""
    <div class="ncm-hero">
        <div class="ncm-eyebrow">Neurociencia aplicada</div>
        <h1>Deteccion de estres mediante EEG</h1>
        <p>Sistema inteligente para el monitoreo de carga cognitiva a partir de senales
        electroencefalograficas, con biomarcadores FAA/TBR y un clasificador RandomForest
        entrenado con datos de multiples dispositivos EEG (Data3 y Data4 como fuentes
        primarias con Fp1/Fp2 reales).</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""<div class="ncm-card" style="border-left:4px solid {COLORS['blue']};">
        <div class="ncm-eyebrow">\U0001F3A7 Senal</div>
        <p style="margin:0;">Electrodos frontales <b>Fp1 / Fp2</b>, muestreo a 1000&nbsp;Hz,
        filtro Butterworth orden 4 (filtfilt) 1-45&nbsp;Hz.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="ncm-card" style="border-left:4px solid {COLORS['primary']};">
        <div class="ncm-eyebrow">\U0001F4D0 FAA / TBR</div>
        <p style="margin:0;">Asimetria alfa frontal y ratio theta/beta, calculados
        en ventanas de 4s con PSD Welch (nperseg=2*fs).</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="ncm-card" style="border-left:4px solid {COLORS['mauve']};">
        <div class="ncm-eyebrow">\U0001F916 Modelo</div>
        <p style="margin:0;">RandomForest + StandardScaler, entrenado con split
        por sujeto (sin fuga de datos entre train/test).</p></div>""", unsafe_allow_html=True)

elif pagina == "Analisis EEG":
    page_header("Procesamiento en tiempo real", "\U0001F4C8 Analisis de senales",
                "Suba su grabacion BASAL (reposo) y la grabacion a clasificar. "
                "El sistema normaliza contra su propio basal antes de clasificar.")

    st.markdown(f"""<div class="ncm-card" style="margin-bottom:1rem;">
    <p style="margin:0;color:{COLORS['ink_soft']};">
    <b>Por que 2 archivos:</b> el modelo v2 (un solo StandardScaler global) no
    corregia la diferencia de escala del BITalino frente a los dispositivos de
    entrenamiento -el basal se clasificaba como "Alto" con 55.8% de confianza-.
    Normalizando cada grabacion contra el basal propio del mismo participante
    (baseline normalization), la deteccion de estres en S01 paso a ser correcta
    con 94.5% de confianza. La contrapartida: siempre se necesita un basal de
    referencia para poder clasificar.</p>
    </div>""", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        basal_file = st.file_uploader("1. Grabacion BASAL (reposo) - TXT BITalino", type=["txt"], key="basal")
    with col_b:
        target_file = st.file_uploader("2. Grabacion a clasificar - TXT BITalino", type=["txt"], key="target")

    if basal_file and target_file:
        with st.spinner("Procesando senal EEG y normalizando contra el basal..."):
            feats_avg, pred, proba, distrib = procesar_y_clasificar_baseline(basal_file, target_file)
        st.markdown(f"""<div style="color:{COLORS['primary']};font-weight:600;margin-bottom:1rem;">
        ✓ Senal procesada correctamente</div>""", unsafe_allow_html=True)

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            metric_card("Asimetria frontal", f"{feats_avg[0]:.4f}", icon="\U0001F9ED", unit="FAA")
        with col2:
            metric_card("Ratio theta/beta", f"{feats_avg[1]:.2f}", icon="⚡", unit="TBR")
        with col3:
            metric_card("Alpha relativa", f"{feats_avg[2]:.3f}", icon="\U0001F30A", unit="")
        with col4:
            metric_card("Beta relativa", f"{feats_avg[3]:.3f}", icon="\U0001F30A", unit="")
        with col5:
            metric_card("Ratio alpha/beta", f"{feats_avg[4]:.2f}", icon="\U0001F4D0", unit="A/B")

        st.write("")
        st.markdown('<div class="ncm-eyebrow">Clasificacion (baseline normalization + RandomForest binario)</div>',
                    unsafe_allow_html=True)
        status_badge(pred, proba, binario=True)
        st.caption(f"Distribucion por ventana de 4s: {distrib}")
        st.caption("Este resultado usa la estrategia validada con datos propios (S01): "
                   "normalizacion contra el basal del mismo participante, no un "
                   "StandardScaler global.")

elif pagina == "Resultados":
    page_header("Historial", "\U0001F4CA Registro de diagnosticos",
                "Visualiza el historial de pruebas cargadas al sistema.")
    st.markdown(f"""<div class="ncm-card">
        <p style="margin:0;color:{COLORS['ink_soft']};">
        Aun no hay resultados guardados. Cuando proceses una senal en
        <b>Analisis EEG</b>, podras registrar aqui su historial.</p>
    </div>""", unsafe_allow_html=True)

elif pagina == "Equipo":
    page_header("Investigacion", "\U0001F469‍\U0001F52C Equipo de investigacion")
    st.markdown(f"""
    <div class="ncm-team-card">
        <div class="ncm-avatar">\U0001F52C</div>
        <div>
            <div style="font-family:'Space Grotesk',sans-serif;font-weight:600;">Xiomara Apaza</div>
            <div style="color:{COLORS['ink_soft']};font-size:0.9rem;">Ingenieria Biomedica</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
