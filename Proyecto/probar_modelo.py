import mne
import joblib
import pandas as pd
import numpy as np

CANALES_EEG = ['AF3', 'T7', 'Pz', 'T8', 'AF4']
VENTANA_SEG = 10
SOLAPE_SEG = 5

archivo = r"Participants Listening to Relaxing Music\001 (15).edf"
# archivo = r"Trier Mental Challenge Test (TMCT)\3 (1).edf"

modelo = joblib.load("modelo_estres_eeg.pkl")

def potencia_banda(data, freqs, fmin, fmax):
    idx = (freqs >= fmin) & (freqs <= fmax)
    return data[:, idx].mean(axis=1)

raw = mne.io.read_raw_edf(archivo, preload=True, verbose=False)
raw.pick(CANALES_EEG)
raw.filter(1, 40, verbose=False)
raw.notch_filter(60, verbose=False)

duracion = raw.times[-1]
filas = []

inicio = 0
while inicio + VENTANA_SEG <= duracion:
    fin = inicio + VENTANA_SEG
    segmento = raw.copy().crop(tmin=inicio, tmax=fin)

    psd = segmento.compute_psd(fmin=1, fmax=40, verbose=False)
    data = psd.get_data()
    freqs = psd.freqs

    theta = potencia_banda(data, freqs, 4, 8)
    alpha = potencia_banda(data, freqs, 8, 13)
    beta = potencia_banda(data, freqs, 13, 30)

    fila = {}

    for i, canal in enumerate(CANALES_EEG):
        fila[f"theta_{canal}"] = theta[i]
        fila[f"alpha_{canal}"] = alpha[i]
        fila[f"beta_{canal}"] = beta[i]
        fila[f"alpha_beta_{canal}"] = alpha[i] / beta[i] if beta[i] != 0 else np.nan

    fila["theta_prom"] = theta.mean()
    fila["alpha_prom"] = alpha.mean()
    fila["beta_prom"] = beta.mean()
    fila["alpha_beta_prom"] = fila["alpha_prom"] / fila["beta_prom"]

    filas.append(fila)
    inicio += SOLAPE_SEG

X = pd.DataFrame(filas)

predicciones = modelo.predict(X)
probabilidades = modelo.predict_proba(X)

porcentaje_relajacion = (predicciones == 0).mean() * 100
porcentaje_estres = (predicciones == 1).mean() * 100

prob_relajacion_prom = probabilidades[:, 0].mean()
prob_estres_prom = probabilidades[:, 1].mean()

print("\nArchivo analizado:")
print(archivo)

print("\nPredicción por ventanas:")
print(f"Ventanas como relajación: {porcentaje_relajacion:.2f}%")
print(f"Ventanas como estrés: {porcentaje_estres:.2f}%")

print("\nProbabilidad promedio:")
print(f"Relajación: {prob_relajacion_prom:.2f}")
print(f"Estrés: {prob_estres_prom:.2f}")

if porcentaje_estres > porcentaje_relajacion:
    print("\nResultado final: ESTRÉS")
else:
    print("\nResultado final: RELAJACIÓN")