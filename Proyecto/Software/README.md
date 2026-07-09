# MindBalance

Código y modelo final del clasificador binario de estrés académico a partir de biomarcadores EEG (Basal vs. Estrés), con normalización por basal individual para superar el domain shift entre dispositivos.

Resultado del modelo final: **72.4% ± 6.0%** accuracy por ventana (AUC 0.801 ± 0.032, F1-macro 0.707 ± 0.053), **82.4% (56/68)** por grabación completa, validado con GroupKFold agrupado por sujeto (sin fuga de datos) y confirmado con hardware real de bajo costo (NeuroBIT/BITalino).

## Archivos

**`pipeline.py`**
Pipeline de procesamiento digital de señales: filtro Butterworth pasa-banda 1–45 Hz, segmentación en ventanas de 4 s, cálculo de PSD (Welch), extracción de los 5 biomarcadores (FAA, TBR, Alpha_rel, Beta_rel, AB_ratio) y normalización por basal individual (`baseline_normalize`). Incluye lectura de los formatos heterogéneos de los datasets (EDF, CSV/ZIP, TXT de OpenSignals/BITalino). El parámetro opcional `overlap` permite generar ventanas solapadas solo para aumentar datos de entrenamiento; la inferencia en vivo sigue usando ventanas sin solape.

**`proyecto.py`**
Script de entrenamiento y validación. Contiene la construcción del dataset binario (`build_delta_dataset`) y el entrenamiento del Random Forest binario (`train_delta_classifier`) con validación GroupKFold agrupada por sujeto. También conserva las funciones del enfoque multiclase original (`build_dataset`), documentado como enfoque descartado (ver el paper para el porqué).

**`app.py`** / **`interfaz_backend.py`**
Backend que envuelve `pipeline.py` y el modelo entrenado para servir predicciones a la interfaz web.

**`probar_bitalino.py`**
Script de validación end-to-end con datos reales de hardware NeuroBIT/BITalino (participante S01), usado para confirmar que el modelo generaliza a un dispositivo de 2 canales no visto en el entrenamiento.

**`MindBalance_interfaz.html`**
Interfaz web standalone (HTML/JS, sin servidor) con el motor DSP embebido: sube una grabación, calcula los biomarcadores, corre el modelo y muestra la clasificación Basal/Estrés junto con un gradiente de intensidad continuo (derivado de la misma probabilidad del modelo binario, no un modelo de 3 niveles aparte — ese enfoque no logró validarse con los datos disponibles). Incluye pestañas de Análisis, Clasificación, Música (protocolo de control) y Validación (resultados out-of-fold).

**`modelo_binario_delta_basal_v2_mejorado.pkl`**
Modelo final: Random Forest binario (`max_depth=8`, `n_estimators=300`, `class_weight='balanced'`), entrenado sobre 3395 ventanas (aumentadas por ventaneo solapado al 50% desde las 1729 ventanas originales de 34 sujetos) y con hiperparámetros ajustados por búsqueda en grilla validada con GroupKFold.

## Qué no se incluye aquí

El enfoque multiclase (clasificación en niveles Bajo/Moderado/Alto con normalización poblacional StandardScaler) se exploró primero pero se descartó como resultado principal: validado correctamente por sujeto, apenas superaba el azar (44–56% de accuracy contra 33% de azar, AUC de la clase "Alto" por debajo de 0.5). Los artefactos de esa versión (`modelo_estres_multiclase*.pkl`, `scaler_estres_v2.pkl`) no se suben aquí para no confundirlos con el sistema binario validado, que es el que se reporta en el poster y el paper del proyecto.
