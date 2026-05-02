# LABORATORIO 4: USO DE BITalino PARA ECG

## Tabla de contenidos
1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Procesamiento y visualización de señales EcG en Python](#4-procesamientoyvisualizacióndeseñalesemgenpython)
5. [Discusión](#5-discusión)
6. [Bibliografía](#6-bibliografía)

---

# 1. Introducción 
El electrocardiograma (ECG) es una prueba no invasiva y de rápida ejecución que registra la actividad eléctrica del corazón, generada en cada latido cuando las señales eléctricas recorren el músculo cardíaco y permiten la contracción de sus cámaras. Esta señal constituye una herramienta fundamental en el análisis biomédico, ya que permite evaluar el ritmo cardíaco y detectar posibles alteraciones como arritmias u otras enfermedades cardiovasculares. En la literatura científica, el ECG ha sido ampliamente utilizado en aplicaciones que van desde la estimación de la frecuencia cardíaca hasta el reconocimiento de emociones y la identificación biométrica. Su procesamiento puede involucrar diversas etapas, como el preprocesamiento, la extracción y selección de características, su transformación y, finalmente, la clasificación de la información obtenida [1].

# 2. Objetivos
- Adquirir señales biomédicas de ECG en condiciones basal, hiperventilación y ejercicio.
- Configurar correctamente el sistema BiTalino para la adquisición de señales electrocardiográficas.
- Procesar y analizar las señales ECG utilizando Python y la plataforma OpenSignals (r)evolution.
# 3. Metodología

## 3.1 Materiales y equipos
| Modelo       | Descripción   | Cantidad |
|:------------:|:-------------:|:--------:|
| (R)EVOLUTION | Kit BITalino  |    1     |
| -            | Laptop o PC   |    1     |

## 3.2 Procedimiento
### 3.2.1 
### 3.2.2 
### 3.2.3 
### 3.2.4 
### 3.2.5 
### 3.2.6 
### 3.2.7
# 4. Procesamiento y visualización de señales EMG en Python

## 4.1. Basal:
### 4.1.1 Derivación 1

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P0_Basal_D1_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P0_Basal_D1_fft_db.png" width="45%">
</p>

### 4.1.2 Derivación 2

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P0_Basal_D2_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P0_Basal_D2_fft_db.png" width="45%">
</p>

### 4.1.3 Derivación 3

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P0_Basal_D3_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P0_Basal_D3_fft_db.png" width="45%">
</p>

## 4.2. P1:
### 4.2.1 Derivación 1

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P1_D1_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P1_D1_fft_db.png" width="45%">
</p>

### 4.2.2 Derivación 2

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P1_D2_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P1_D2_fft_db.png" width="45%">
</p>

### 4.2.3 Derivación 3

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P1_D3_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P1_D3_fft_db.png" width="45%">
</p>

## 4.3. P2:
### 4.3.1 Derivación 1

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P2_D1_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P2_D1_fft_db.png" width="45%">
</p>

### 4.3.2 Derivación 2

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P2_D2_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P2_D2_fft_db.png" width="45%">
</p>

### 4.3.3 Derivación 3

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P2_D3_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P2_D3_fft_db.png" width="45%">
</p>

## 4.4. P3:
### 4.4.1 Derivación 1

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P3_Basal_D1_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P3_Basal_D1_fft_db.png" width="45%">
</p>

### 4.4.2 Derivación 2

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P3_Basal_D2_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P3_Basal_D2_fft_db.png" width="45%">
</p>

### 4.4.3 Derivación 3

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P3_Basal_D3_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P3_Basal_D3_fft_db.png" width="45%">
</p>

## 4.5. P4:
### 4.5.1 Derivación 1

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P4_D1_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P4_D1_fft_db.png" width="45%">
</p>

### 4.5.2 Derivación 2

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P4_D2_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P4_D2_fft_db.png" width="45%">
</p>

### 4.5.3 Derivación 3
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P4_D3_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P4_D3_fft_db.png" width="45%">
</p>

## 4.6. P5:
### 4.6.1 Derivación 1

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P5_D1_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P5_D1_fft_db.png" width="45%">
</p>

### 4.6.2 Derivación 2

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P5_D2_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P5_D2_fft_db.png" width="45%">
</p>

### 4.6.3 Derivación 3

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P5_D3_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P5_D3_fft_db.png" width="45%">
</p>

## 4.7. P6: 
### 4.7.1 Derivación 1

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P6_D1_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P6_D1_fft_db.png" width="45%">
</p>

### 4.7.2 Derivación 2

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P6_D2_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P6_D2_fft_db.png" width="45%">
</p>

### 4.7.3 Derivación 3

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P6_D3_tiempo_mV.png" width="45%">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/ECG/P6_D3_fft_db.png" width="45%">
</p>

