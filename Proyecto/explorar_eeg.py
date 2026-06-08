import os
import mne
import pandas as pd
import numpy as np

CARPETAS = {
    "Trier Mental Challenge Test (TMCT)": 1,       # estrés
    "Participants Listening to Relaxing Music": 0  # relajación
}

CANALES_EEG = ['AF3', 'T7', 'Pz', 'T8', 'AF4']

VENTANA_SEG = 10
SOLAPE_SEG = 5

def potencia_banda(data, freqs, fmin, fmax):
    idx = (freqs >= fmin) & (freqs <= fmax)
    return data[:, idx].mean(axis=1)  # potencia por canal

def calcular_features_por_ventanas(archivo, etiqueta):
    raw = mne.io.read_raw_edf(archivo, preload=True, verbose=False)
    raw.pick(CANALES_EEG)

    raw.filter(1, 40, verbose=False)
    raw.notch_filter(60, verbose=False)

    fs = raw.info["sfreq"]
    duracion = raw.times[-1]

    filas_archivo = []

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

        fila = {
            "archivo": os.path.basename(archivo),
            "inicio_s": inicio,
            "fin_s": fin,
            "clase": etiqueta
        }

        for i, canal in enumerate(CANALES_EEG):
            fila[f"theta_{canal}"] = theta[i]
            fila[f"alpha_{canal}"] = alpha[i]
            fila[f"beta_{canal}"] = beta[i]
            fila[f"alpha_beta_{canal}"] = alpha[i] / beta[i] if beta[i] != 0 else np.nan

        fila["theta_prom"] = theta.mean()
        fila["alpha_prom"] = alpha.mean()
        fila["beta_prom"] = beta.mean()
        fila["alpha_beta_prom"] = fila["alpha_prom"] / fila["beta_prom"]

        filas_archivo.append(fila)

        inicio += SOLAPE_SEG

    return filas_archivo

filas = []

for carpeta, etiqueta in CARPETAS.items():
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".edf"):
            ruta = os.path.join(carpeta, archivo)
            print("Procesando:", ruta)
            filas.extend(calcular_features_por_ventanas(ruta, etiqueta))

df = pd.DataFrame(filas)
df.to_csv("features_eeg.csv", index=False)

print("\nTabla creada:")
print(df.head())
print("\nNúmero total de ventanas:", len(df))
print("Archivo guardado como features_eeg.csv")