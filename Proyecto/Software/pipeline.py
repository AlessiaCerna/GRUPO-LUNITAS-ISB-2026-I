"""
Pipeline unificado de extraccion de biomarcadores EEG (FAA, TBR, Alpha_rel, Beta_rel)
para el proyecto NeuroBIT / Clasificacion Multinivel del Estres.

Fuentes:
  - Data3 (eego, Fp1/Fp2, 2000 Hz, 29 sujetos, EO=basal, AC1/AC2=estres agudo) -> PRIMARIA
  - Data4 (clinico 10-20, Fp1-A1/Fp2-A2, 200 Hz, 9 sujetos, not_stress/stress)  -> PRIMARIA
  - Data1 (Emotiv AF3/AF4 como aproximacion frontal, 128 Hz, 5 protocolos)      -> SECUNDARIA
  - Data2 (Muse, bandas precalculadas AF7/AF8 como aproximacion Fp1/Fp2,       -> SECUNDARIA
           26 sujetos con etiqueta REAL de estres desde el Excel)

Especificacion DSP (dada por el usuario):
  - Filtro Butterworth pasa-banda 1-45 Hz, orden 4, filtfilt
  - Ventanas de 4 s
  - PSD Welch, nperseg = 2*fs
  - FAA = ln(alfa_Fp2) - ln(alfa_Fp1),  banda alfa 8-12 Hz
  - TBR = theta_Fp1 / beta_Fp1,          theta 4-8 Hz, beta 12-30 Hz
  - Alpha_rel, Beta_rel: potencia de banda relativa (banda / potencia total 1-45Hz),
    promediada entre Fp1 y Fp2. Se usa potencia RELATIVA en vez de absoluta para
    reducir el domain-shift entre dispositivos (ver nota en el informe).
  - AB_ratio = Alpha_rel / Beta_rel: ratio alpha/beta explicito (quinta feature).
    Justificado por evidencia directa en Wen & Aris (2020, IJEECS 17(1):175-182):
    el ratio alpha/beta disminuye significativamente bajo estres (VR, 40 sujetos).
    Como Alpha_rel y Beta_rel ya estan normalizadas por la potencia total (misma
    ventana), AB_ratio = Alpha_rel/Beta_rel es algebraicamente identico a
    Alpha_absoluta/Beta_absoluta (el termino de potencia total se cancela), por
    lo que no hace falta recalcular nada extra: se deriva directo de las dos
    features relativas ya existentes. Parche aplicado sobre
    parche_ratio_alpha_beta.py (ver ese archivo para el razonamiento original).
"""
import os
import numpy as np
import pandas as pd
import mne
from scipy.signal import butter, filtfilt

mne.set_log_level('ERROR')

ALPHA = (8, 12)
THETA = (4, 8)
BETA = (12, 30)
FULL = (1, 45)


def bandpass_filter(data, fs, low=1.0, high=45.0, order=4):
    nyq = fs / 2.0
    high_norm = min(high, nyq * 0.98) / nyq
    low_norm = low / nyq
    b, a = butter(order, [low_norm, high_norm], btype='band')
    return filtfilt(b, a, data, axis=-1)


def epoch_features(fp1, fp2, fs, epoch_s=4.0, overlap=0.0):
    """overlap=0.0 (default) reproduce el comportamiento original (ventanas sin
    solape, usado por la interfaz JS y por toda la validacion ya reportada).
    overlap in (0,1) solo se usa para AUMENTAR datos de ENTRENAMIENTO a partir
    de las mismas grabaciones ya recolectadas (mas ventanas por la misma
    duracion de señal), nunca para inferencia en vivo."""
    win = int(epoch_s * fs)
    step = max(1, int(win * (1.0 - overlap)))
    n_epochs = 1 + (len(fp1) - win) // step if len(fp1) >= win else 0
    if n_epochs <= 0:
        return []
    nperseg = int(2 * fs)
    feats = []
    for i in range(n_epochs):
        start = i * step
        seg1 = fp1[start:start + win]
        seg2 = fp2[start:start + win]
        data = np.vstack([seg1, seg2])
        seg_len = min(nperseg, data.shape[-1])
        psds, freqs = mne.time_frequency.psd_array_welch(
            data, sfreq=fs, fmin=FULL[0], fmax=FULL[1],
            n_fft=seg_len, n_per_seg=seg_len, verbose=False)
        a_mask = (freqs >= ALPHA[0]) & (freqs < ALPHA[1])
        t_mask = (freqs >= THETA[0]) & (freqs < THETA[1])
        b_mask = (freqs >= BETA[0]) & (freqs <= BETA[1])
        full_mask = (freqs >= FULL[0]) & (freqs <= FULL[1])

        a_fp1, a_fp2 = np.mean(psds[0, a_mask]), np.mean(psds[1, a_mask])
        t_fp1 = np.mean(psds[0, t_mask])
        b_fp1 = np.mean(psds[0, b_mask])
        total_fp1 = np.mean(psds[0, full_mask])
        total_fp2 = np.mean(psds[1, full_mask])

        if a_fp1 <= 0 or a_fp2 <= 0 or b_fp1 <= 0:
            continue
        faa = np.log(a_fp2) - np.log(a_fp1)
        tbr = t_fp1 / b_fp1
        alpha_rel = 0.5 * (a_fp1 / total_fp1 + a_fp2 / total_fp2)
        beta_rel = 0.5 * (np.mean(psds[0, b_mask]) / total_fp1 + np.mean(psds[1, b_mask]) / total_fp2)
        if beta_rel <= 0:
            continue
        ab_ratio = alpha_rel / beta_rel
        feats.append([faa, tbr, alpha_rel, beta_rel, ab_ratio])
    return feats


def aggregate(feats):
    if len(feats) == 0:
        return None
    return np.mean(np.array(feats), axis=0)


import zipfile


NEEDED_MEMBERS = [
    'EEG/EO/EO_Fp1.csv', 'EEG/EO/EO_Fp2.csv',
    'EEG/AC1/AC1_Fp1.csv', 'EEG/AC1/AC1_Fp2.csv',
    'EEG/AC2/AC2_Fp1.csv', 'EEG/AC2/AC2_Fp2.csv',
]


def ensure_data3_extracted(zip_path, extract_to):
    all_present = all(
        os.path.exists(os.path.join(extract_to, m)) and
        os.path.getsize(os.path.join(extract_to, m)) > 10_000_000
        for m in NEEDED_MEMBERS)
    if all_present:
        return extract_to
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as z:
        for member in NEEDED_MEMBERS:
            z.extract(member, extract_to)
    return extract_to


def process_eego_data3(data3_root, fs=2000.0):
    X, y, groups = [], [], []

    def load_channel(cond):
        fp1 = pd.read_csv(os.path.join(data3_root, 'EEG', cond, f'{cond}_Fp1.csv')).values
        fp2 = pd.read_csv(os.path.join(data3_root, 'EEG', cond, f'{cond}_Fp2.csv')).values
        return fp1, fp2

    eo_fp1, eo_fp2 = load_channel('EO')
    ac1_fp1, ac1_fp2 = load_channel('AC1')
    ac2_fp1, ac2_fp2 = load_channel('AC2')
    n_subj = eo_fp1.shape[1]

    def valid_pair(col1, col2):
        n = min(np.sum(~np.isnan(col1)), np.sum(~np.isnan(col2)))
        if n < int(4 * fs):
            return None, None
        return col1[:n].astype(float), col2[:n].astype(float)

    for s in range(n_subj):
        sid = f'data3_S{s+1:02d}'

        c1, c2 = valid_pair(eo_fp1[:, s], eo_fp2[:, s])
        if c1 is not None:
            eo1 = bandpass_filter(c1, fs)
            eo2 = bandpass_filter(c2, fs)
            f_eo = aggregate(epoch_features(eo1, eo2, fs))
            if f_eo is not None:
                X.append(f_eo); y.append(0); groups.append(sid)

        stress_feats = []
        c1, c2 = valid_pair(ac1_fp1[:, s], ac1_fp2[:, s])
        if c1 is not None:
            a1_1 = bandpass_filter(c1, fs)
            a1_2 = bandpass_filter(c2, fs)
            stress_feats += epoch_features(a1_1, a1_2, fs)
        c1, c2 = valid_pair(ac2_fp1[:, s], ac2_fp2[:, s])
        if c1 is not None:
            a2_1 = bandpass_filter(c1, fs)
            a2_2 = bandpass_filter(c2, fs)
            stress_feats += epoch_features(a2_1, a2_2, fs)
        f_stress = aggregate(stress_feats)
        if f_stress is not None:
            X.append(f_stress); y.append(2); groups.append(sid)

    return np.array(X), np.array(y), np.array(groups)


def process_eego_data3_epochs(data3_root, fs=2000.0, overlap=0.0):
    def load_channel(cond):
        fp1 = pd.read_csv(os.path.join(data3_root, 'EEG', cond, f'{cond}_Fp1.csv')).values
        fp2 = pd.read_csv(os.path.join(data3_root, 'EEG', cond, f'{cond}_Fp2.csv')).values
        return fp1, fp2

    eo_fp1, eo_fp2 = load_channel('EO')
    ac1_fp1, ac1_fp2 = load_channel('AC1')
    ac2_fp1, ac2_fp2 = load_channel('AC2')
    n_subj = eo_fp1.shape[1]

    def valid_pair(col1, col2):
        n = min(np.sum(~np.isnan(col1)), np.sum(~np.isnan(col2)))
        if n < int(4 * fs):
            return None, None
        return col1[:n].astype(float), col2[:n].astype(float)

    out = {}
    for s in range(n_subj):
        sid = f'data3_S{s+1:02d}'
        c1, c2 = valid_pair(eo_fp1[:, s], eo_fp2[:, s])
        if c1 is None:
            continue
        basal_epochs = epoch_features(bandpass_filter(c1, fs), bandpass_filter(c2, fs), fs, overlap=overlap)

        stress_epochs = []
        c1, c2 = valid_pair(ac1_fp1[:, s], ac1_fp2[:, s])
        if c1 is not None:
            stress_epochs += epoch_features(bandpass_filter(c1, fs), bandpass_filter(c2, fs), fs, overlap=overlap)
        c1, c2 = valid_pair(ac2_fp1[:, s], ac2_fp2[:, s])
        if c1 is not None:
            stress_epochs += epoch_features(bandpass_filter(c1, fs), bandpass_filter(c2, fs), fs, overlap=overlap)

        if len(basal_epochs) >= 2 and len(stress_epochs) >= 1:
            out[sid] = {'basal': np.array(basal_epochs), 'stress': np.array(stress_epochs)}
    return out


def process_edf_clinical(file_path):
    raw = mne.io.read_raw_edf(file_path, preload=True, verbose=False)
    fp1_name = next((c for c in raw.ch_names if c.upper().startswith('FP1')), None)
    fp2_name = next((c for c in raw.ch_names if c.upper().startswith('FP2')), None)
    if fp1_name is None or fp2_name is None:
        return None
    fs = raw.info['sfreq']
    data = raw.get_data(picks=[fp1_name, fp2_name]) * 1e6
    fp1 = bandpass_filter(data[0], fs)
    fp2 = bandpass_filter(data[1], fs)
    feats = epoch_features(fp1, fp2, fs)
    return aggregate(feats)


def load_data4(path_data4):
    X, y, groups = [], [], []
    if not os.path.exists(path_data4):
        return np.array(X), np.array(y), np.array(groups)
    for f in sorted(os.listdir(path_data4)):
        if not f.lower().endswith('.edf'):
            continue
        low = f.lower()
        if 'not_classified' in low:
            continue
        label = 0 if 'not_stress' in low else (2 if 'stress' in low else None)
        if label is None:
            continue
        feats = process_edf_clinical(os.path.join(path_data4, f))
        if feats is not None:
            X.append(feats); y.append(label); groups.append('data4_' + f.split('.')[0])
    return np.array(X), np.array(y), np.array(groups)


def process_edf_clinical_epochs(file_path, overlap=0.0):
    raw = mne.io.read_raw_edf(file_path, preload=True, verbose=False)
    fp1_name = next((c for c in raw.ch_names if c.upper().startswith('FP1')), None)
    fp2_name = next((c for c in raw.ch_names if c.upper().startswith('FP2')), None)
    if fp1_name is None or fp2_name is None:
        return None
    fs = raw.info['sfreq']
    data = raw.get_data(picks=[fp1_name, fp2_name]) * 1e6
    fp1 = bandpass_filter(data[0], fs)
    fp2 = bandpass_filter(data[1], fs)
    return np.array(epoch_features(fp1, fp2, fs, overlap=overlap))


def load_data4_paired_epochs(path_data4, overlap=0.0):
    if not os.path.exists(path_data4):
        return {}
    files = os.listdir(path_data4)
    subjects = sorted(set(f.split('_')[0] for f in files if f.lower().endswith('.edf')))
    out = {}
    for subj in subjects:
        not_stress_f = next((f for f in files if f.startswith(subj + '_') and 'not_stress' in f.lower()), None)
        stress_f = next((f for f in files if f.startswith(subj + '_') and f.lower().endswith('stress.edf')
                          and 'not_stress' not in f.lower()), None)
        if not_stress_f is None or stress_f is None:
            continue
        basal_epochs = process_edf_clinical_epochs(os.path.join(path_data4, not_stress_f), overlap=overlap)
        stress_epochs = process_edf_clinical_epochs(os.path.join(path_data4, stress_f), overlap=overlap)
        if basal_epochs is not None and stress_epochs is not None and len(basal_epochs) >= 2:
            out['data4_' + subj] = {'basal': basal_epochs, 'stress': stress_epochs}
    return out


PROTOCOL_LABELS = {
    'Participants Listening to Relaxing Music': 0,
    'Complex Mathematical Problem solving (CMPS)': 1,
    'Stroop Colour Word Test(SCWT)': 1,
    'Trier Mental Challenge Test (TMCT)': 2,
    'Horrer Video Stimulation': 2,
}


def process_edf_emotiv(file_path):
    raw = mne.io.read_raw_edf(file_path, preload=True, verbose=False)
    if 'AF3' not in raw.ch_names or 'AF4' not in raw.ch_names:
        return None
    fs = raw.info['sfreq']
    data = raw.get_data(picks=['AF3', 'AF4']) * 1e6
    af3 = bandpass_filter(data[0], fs)
    af4 = bandpass_filter(data[1], fs)
    feats = epoch_features(af3, af4, fs)
    return aggregate(feats)


def load_data1(path_data1):
    X, y, groups = [], [], []
    if not os.path.exists(path_data1):
        return np.array(X), np.array(y), np.array(groups)
    for protocol, label in PROTOCOL_LABELS.items():
        proto_dir = os.path.join(path_data1, protocol)
        if not os.path.exists(proto_dir):
            continue
        for f in sorted(os.listdir(proto_dir)):
            if not f.lower().endswith('.edf'):
                continue
            feats = process_edf_emotiv(os.path.join(proto_dir, f))
            if feats is not None:
                sid = f'data1_{protocol[:4]}_{f}'
                X.append(feats); y.append(label); groups.append(sid)
    return np.array(X), np.array(y), np.array(groups)


def process_csv_precalculated(file_path):
    df = pd.read_csv(file_path)
    needed = ['Alpha_AF7', 'Alpha_AF8', 'Theta_AF7', 'Beta_AF7']
    if not all(c in df.columns for c in needed):
        return None
    df = df[needed].dropna()
    df = df[(df > 0).all(axis=1)]
    if len(df) == 0:
        return None
    a_fp1 = df['Alpha_AF7'].mean()
    a_fp2 = df['Alpha_AF8'].mean()
    t_fp1 = df['Theta_AF7'].mean()
    b_fp1 = df['Beta_AF7'].mean()
    faa = np.log(a_fp2) - np.log(a_fp1)
    tbr = t_fp1 / b_fp1
    total_fp1_cols = [c for c in ['Delta_AF7', 'Theta_AF7', 'Alpha_AF7', 'Beta_AF7', 'Gamma_AF7'] if c in df.columns]
    if len(total_fp1_cols) >= 3:
        total_fp1 = df[total_fp1_cols].mean().sum()
        alpha_rel = a_fp1 / total_fp1 if total_fp1 > 0 else np.nan
        beta_rel = b_fp1 / total_fp1 if total_fp1 > 0 else np.nan
    else:
        alpha_rel, beta_rel = np.nan, np.nan
    ab_ratio = alpha_rel / beta_rel if (beta_rel and beta_rel > 0 and not np.isnan(beta_rel)) else np.nan
    return np.array([faa, tbr, alpha_rel, beta_rel, ab_ratio])


def load_data2(path_data2, stress_xlsx):
    X, y, groups = [], [], []
    if not os.path.exists(path_data2):
        return np.array(X), np.array(y), np.array(groups)
    labels_df = pd.read_excel(stress_xlsx, sheet_name='Sheet1')
    labels_df.columns = [c.strip() for c in labels_df.columns]
    labels_df['stress level'] = labels_df['stress level'].str.strip()
    level_to_class = {'No': 0, 'Low': 0, 'Moderate': 1, 'High': 2, 'Very high': 2}
    label_map = dict(zip(labels_df['SL NO.'], labels_df['stress level'].map(level_to_class)))

    for f in sorted(os.listdir(path_data2)):
        if not f.lower().endswith('.csv'):
            continue
        sid = f.replace('.csv', '')
        if sid not in label_map or pd.isna(label_map[sid]):
            continue
        feats = process_csv_precalculated(os.path.join(path_data2, f))
        if feats is not None and not np.isnan(feats).any():
            X.append(feats); y.append(int(label_map[sid])); groups.append('data2_' + sid)
    return np.array(X), np.array(y), np.array(groups)


def process_bitalino(file_path, fs=1000.0):
    df = pd.read_csv(file_path, sep=r'\s+', comment='#', header=None)
    G = 40000
    fp1 = ((df.iloc[:, 5] / 1024) - 0.5) * 3.3 / G * 1e6
    fp2 = ((df.iloc[:, 6] / 1024) - 0.5) * 3.3 / G * 1e6
    fp1 = bandpass_filter(fp1.values.astype(float), fs)
    fp2 = bandpass_filter(fp2.values.astype(float), fs)
    feats = epoch_features(fp1, fp2, fs)
    return np.array(feats), aggregate(feats)



def baseline_normalize(target_epochs, basal_epochs, eps=1e-8):
    basal_mean = basal_epochs.mean(axis=0)
    basal_std = basal_epochs.std(axis=0)