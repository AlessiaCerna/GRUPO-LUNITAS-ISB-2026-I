"""
interfaz_backend.py - Backend de la interfaz NeuroCalm v2
============================================================
Este backend NO reimplementa el procesamiento de senal EEG: llama directo
a las funciones ya validadas de pipeline.py (mismo filtro Butterworth,
mismas ventanas de 4s, mismo PSD Welch, mismo modelo .pkl) para que los
numeros mostrados en la interfaz sean identicos a los reportados en el
paper. Lo unico nuevo aqui son:
  1. Extraccion de series de tiempo (para animar la onda cruda)
  2. Espectrograma STFT por canal (mapa de calor tiempo-frecuencia,
     legitimo con 1 solo canal, no requiere multiples electrodos)
  3. Deteccion simple de calidad de senal / artefactos por ventana
     (amplitud pico-a-pico + z-score dentro de la propia sesion)
  4. Endpoints REST para que el frontend HTML/JS consuma todo esto

Ejecutar:  python interfaz_backend.py
Luego abrir http://localhost:5000 en el navegador.
"""
import io
import os
import numpy as np
from scipy.signal import spectrogram as scipy_spectrogram
from flask import Flask, request, jsonify, send_from_directory
import joblib

import pipeline as p

app = Flask(__name__, static_folder='.', static_url_path='')

MODEL_BIN_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modelo_binario_delta_basal.pkl')
_clf_bin = None
LABELS_BIN = ['Basal', 'Estres']


def get_model():
    global _clf_bin
    if _clf_bin is None:
        _clf_bin = joblib.load(MODEL_BIN_PATH)
    return _clf_bin


def read_bitalino_raw(file_stream, fs=1000.0):
    import pandas as pd
    df = pd.read_csv(file_stream, sep=r'\s+', comment='#', header=None)
    G = 40000
    fp1_raw = ((df.iloc[:, 5] / 1024) - 0.5) * 3.3 / G * 1e6
    fp2_raw = ((df.iloc[:, 6] / 1024) - 0.5) * 3.3 / G * 1e6
    fp1_raw = fp1_raw.values.astype(float)
    fp2_raw = fp2_raw.values.astype(float)
    fp1_filt = p.bandpass_filter(fp1_raw, fs)
    fp2_filt = p.bandpass_filter(fp2_raw, fs)
    return fp1_raw, fp2_raw, fp1_filt, fp2_filt


def decimate(arr, factor):
    return arr[::factor]


def compute_spectrogram(sig, fs, fmax=45.0, target_time_bins=180):
    nperseg = int(fs * 2)
    noverlap = int(nperseg * 0.5)
    f, t, Sxx = scipy_spectrogram(sig, fs=fs, nperseg=nperseg, noverlap=noverlap)
    fmask = f <= fmax
    f = f[fmask]
    Sxx = Sxx[fmask, :]
    Sxx = 10 * np.log10(Sxx + 1e-12)
    if Sxx.shape[1] > target_time_bins:
        step = Sxx.shape[1] // target_time_bins
        Sxx = Sxx[:, ::step]
        t = t[::step]
    return f.tolist(), t.tolist(), np.round(Sxx, 2).tolist()


def signal_quality_epochs(fp1_filt, fp2_filt, fs, epoch_s=4.0):
    win = int(epoch_s * fs)
    n_epochs = len(fp1_filt) // win
    if n_epochs == 0:
        return [], [], []
    pp = []
    for i in range(n_epochs):
        s1 = fp1_filt[i * win:(i + 1) * win]
        s2 = fp2_filt[i * win:(i + 1) * win]
        pp.append(max(np.ptp(s1), np.ptp(s2)))
    pp = np.array(pp)
    mu, sigma = pp.mean(), pp.std() + 1e-8
    z = (pp - mu) / sigma
    score = np.clip(1.0 - np.clip(z, 0, None) / 3.0, 0.0, 1.0)
    flags = ['ruido' if s < 0.4 else ('atencion' if s < 0.7 else 'limpio') for s in score]
    t_centers = [(i + 0.5) * epoch_s for i in range(n_epochs)]
    return t_centers, np.round(score, 3).tolist(), flags


def epochs_to_series(epochs_arr, epoch_s=4.0):
    n = len(epochs_arr)
    t = [(i + 0.5) * epoch_s for i in range(n)]
    names = ['faa', 'tbr', 'alpha_rel', 'beta_rel', 'ab_ratio']
    out = {'t': t}
    for j, name in enumerate(names):
        out[name] = np.round(epochs_arr[:, j], 4).tolist()
    return out


def summary_from_avg(avg):
    names = ['faa', 'tbr', 'alpha_rel', 'beta_rel', 'ab_ratio']
    return {name: (round(float(avg[i]), 4) if avg is not None else None) for i, name in enumerate(names)}


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/api/health')
def api_health():
    return jsonify({'status': 'ok', 'modelo_features': int(get_model().n_features_in_)})


@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    f = request.files.get('file')
    if f is None:
        return jsonify({'error': 'falta el archivo'}), 400
    fs = 1000.0
    fp1_raw, fp2_raw, fp1_filt, fp2_filt = read_bitalino_raw(f.stream, fs=fs)
    duration_s = len(fp1_filt) / fs

    dec_factor = max(1, int(fs // 128))
    fp1_dec = decimate(fp1_filt, dec_factor)
    fp2_dec = decimate(fp2_filt, dec_factor)
    t_wave = (np.arange(len(fp1_dec)) * dec_factor / fs).tolist()

    epochs_list = p.epoch_features(fp1_filt, fp2_filt, fs)
    epochs_arr = np.array(epochs_list) if epochs_list else np.zeros((0, 5))
    avg = p.aggregate(epochs_list)

    f1, t1, Sxx1 = compute_spectrogram(fp1_filt, fs)
    f2, t2, Sxx2 = compute_spectrogram(fp2_filt, fs)

    qt, qscore, qflags = signal_quality_epochs(fp1_filt, fp2_filt, fs)

    return jsonify({
        'duration_s': round(duration_s, 1),
        'fs_decimated': round(fs / dec_factor, 1),
        'waveform': {
            't': [round(x, 3) for x in t_wave],
            'fp1': np.round(fp1_dec, 2).tolist(),
            'fp2': np.round(fp2_dec, 2).tolist(),
        },
        'spectrogram': {
            'fp1': {'f': f1, 't': t1, 'Sxx_db': Sxx1},
            'fp2': {'f': f2, 't': t2, 'Sxx_db': Sxx2},
        },
        'epochs': epochs_to_series(epochs_arr),
        'quality': {'t': qt, 'score': qscore, 'flag': qflags},
        'summary': summary_from_avg(avg),
        'n_epochs': int(len(epochs_list)),
    })


@app.route('/api/classify', methods=['POST'])
def api_classify():
    basal_f = request.files.get('basal')
    target_f = request.files.get('target')
    if basal_f is None or target_f is None:
        return jsonify({'error': 'faltan archivos basal y/o target'}), 400
    clf = get_model()
    fs = 1000.0

    _, _, b1, b2 = read_bitalino_raw(basal_f.stream, fs=fs)
    basal_epochs = np.array(p.epoch_features(b1, b2, fs))
    _, _, t1, t2 = read_bitalino_raw(target_f.stream, fs=fs)
    target_epochs = np.array(p.epoch_features(t1, t2, fs))

    delta = p.baseline_normalize(target_epochs, basal_epochs)
    preds = clf.predict(delta)
    probas = clf.predict_proba(delta)

    windows = []
    for i, (pred, proba) in enumerate(zip(preds, probas)):
        windows.append({
            't': round((i + 0.5) * 4.0, 1),
            'pred': LABELS_BIN[int(pred)],
            'proba_estres': round(float(proba[1]), 3),
        })

    vals, counts = np.unique(preds, return_counts=True)
    distrib = {LABELS_BIN[int(v)]: int(c) for v, c in zip(vals, counts)}
    pred_mayoritaria = LABELS_BIN[int(np.round(preds.mean()))]
    proba_media = {LABELS_BIN[i]: round(float(probas.mean(axis=0)[i]), 3) for i in range(2)}

    return jsonify({
        'basal_summary': summary_from_avg(p.aggregate(list(basal_epochs))),
        'target_summary': summary_from_avg(p.aggregate(list(target_epochs))),
        'windows': windows,
        'pred_mayoritaria': pred_mayoritaria,
        'proba_media': proba_media,
        'distrib': distrib,
    })


@app.route('/api/compare', methods=['POST'])
def api_compare():
    fs = 1000.0
    files = {}
    for key in ['basal', 'estres', 'musica']:
        fobj = request.files.get(key)
        if fobj is not None:
            _, _, c1, c2 = read_bitalino_raw(fobj.stream, fs=fs)
            ep = p.epoch_features(c1, c2, fs)
            files[key] = summary_from_avg(p.aggregate(ep)) if ep else None

    if 'basal' not in files or files['basal'] is None:
        return jsonify({'error': 'se requiere el archivo basal'}), 400

    result = {'conditions': files}

    if files.get('estres') and files.get('musica'):
        def recovery(metric, higher_is_stress):
            b = files['basal'][metric]
            e = files['estres'][metric]
            m = files['musica'][metric]
            span = (e - b)
            if abs(span) < 1e-9:
                return None
            pct = (e - m) / span * 100.0
            return round(float(np.clip(pct, 0, 100)), 1)

        result['recovery_pct'] = {
            'tbr': recovery('tbr', True),
            'ab_ratio': recovery('ab_ratio', False),
        }

    return jsonify(result)


if __name__ == '__main__':
    print('NeuroCalm backend -> http://localhost:5000')
    app.run(host='0.0.0.0', port=5000, debug=False)
