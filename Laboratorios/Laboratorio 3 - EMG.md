# LABORATORIO 3: USO DE BITalino PARA EMG

## Tabla de contenidos
1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Procesamiento y visualización de señales EMG en Python](#4-procesamientoyvisualizacióndeseñalesemgenpython)
5. [Discusión](#5-discusión)
6. [Bibliografía](#6-bibliografía)

---

# 1. Introducción  

La electromiografía (EMG) es una técnica utilizada para registrar la actividad eléctrica generada por los músculos durante su contracción, ya sea voluntaria o involuntaria. Esta señal refleja la activación de las unidades motoras y puede adquirirse mediante electrodos invasivos insertados directamente en el músculo o mediante electrodos colocados sobre la superficie de la piel, esto es conocido como electromiografía de superficie (sEMG). Mientras que la EMG intramuscular la cual ofrece una alternativa no invasiva que registra la actividad global del músculo [1].

### Ventajas
- Permite evaluar la actividad muscular en tiempo real.  
- Aplicable en rehabilitación, análisis de movimiento. 
- La sEMG es no invasiva. 
- Electrodos de bajo costo y accesibles.  

### Desventajas
- La EMG intramuscular es invasiva  
- Las EMG solo mide músculos superficiales  
- Susceptibilidad al ruido e interferencias  
- La señal puede verse afectada por los tejidos [2]

En este laboratorio se emplea el sistema BITalino para la adquisición de señales EMG, permitiendo analizar la actividad muscular de manera práctica y accesible.

# 2. Objetivos
- Adquirir señales biomédicas de EMG
- Configuración correcta del sistema BiTalino para adquisición electromiográfica.  .  
- Extraer la información de las señales EMG utilizando la plataforma OpenSignals (r)evolution para realizar el procesamiento y análisis de datos.

# 3. Metodología

## 3.1 Materiales y equipos
| Modelo       | Descripción   | Cantidad |
|:------------:|:-------------:|:--------:|
| (R)EVOLUTION | Kit BITalino  |    1     |
| -            | Laptop o PC   |    1     |

## 3.2 Procedimiento: Bícep

### 3.2.1. Prueba 1 (Prueba Basal)
En primer lugar, se registró la señal electromiográfica (EMG) de la participante en condición de reposo, con el fin de establecer una línea base para posteriores comparaciones.  

|**Conexión correcta**|**Conexión real**|
|:------------------|:--------------------|
|<img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/image003.jpg" width="400"> | <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/Captura%20de%20pantalla%202026-04-24%20193330.png" width="400">|
> **Electrodo rojo (+):** bíceps (zona activa)<br> **Electrodo negro (–):** bíceps (zona pasiva)<br> **Electrodo blanco (REF):** espina ilíaca antero-superior (referencia) 

### 3.2.2. Prueba 2 (Flexión de bícep) 
La participante realizó flexión del brazo derecho durante un intervalo de 20 segundos, seguido de un período de reposo de 15 segundos. Este procedimiento fue repetido en múltiples ciclos consecutivos con el fin de evaluar la variación de la señal EMG entre estados de reposo y contracción.  

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/Video%20Project%20(1).gif" alt="GIF de prueba" width="500" height="500"/>
</p>

### 3.2.3. Prueba 3  (Flexión de bícep con contrapeso)
La participante efectuó flexión del brazo izquierdo contra una carga externa de 2 kg, con el objetivo de analizar la respuesta electromiográfica ante un esfuerzo mayor. Posteriormente, se consideró un período de reposo. Este protocolo se repitió en varios ciclos para garantizar la consistencia de los resultados.

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/Video%20Project_peso.gif" width="500" height="500"/>
</p>

### 3.2.4. Prueba 4
Se registró la señal electromiográfica (EMG) de la participante en condición de reposo, con el fin de establecer una línea base para posteriores comparaciones.

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/Video%20Project_basal.gif" alt="GIF de prueba" width="500" height="500"/>
</p>

### 3.2.5. Prueba 5
Se registró la señal electromiográfica (EMG) de la participante ejerciendo fuerza contra otra persona.

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/Video%20Project_basal%20(1).gif" alt="GIF de prueba" width="500" height="500"/>
</p>

## 3.2 Procedimiento: Gastrocnemio

### 3.2.6. Prueba 1
Se registró la señal electromiográfica (EMG) de la participante en condición de reposo, con el fin de establecer una línea base para posteriores comparaciones. Las señales captadas provienen del músculo gastrocnemio.

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/Video%20Project_basal_pierna.gif" alt="GIF de prueba" width="500" height="500"/>
</p>

### 3.2.7. Prueba 2
La participante realizó flexión plantar del tobillo durante un intervalo de 10 segundos, seguido de un período de reposo de 20 segundos. Este procedimiento fue repetido en múltiples ciclos consecutivos con el fin de evaluar la variación de la señal EMG entre estados de reposo y contracción.

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/Video%20Project_pierna.gif" alt="GIF de prueba" width="500" height="500"/>
</p>

# 4. Procesamiento y visualización de señales EMG en Python

## 4.1. Experimento 1: Bíceps

### 4.1.1. Prueba 1 (Señal EMG en reposo)
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.55.14.jpeg" 
       alt="b_reposo" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.55.14%20(1).jpeg" 
       alt="b_reposo" width="800" height="400">
</p>

### 4.1.2. Prueba 2 (Flexión de brazo)

- Toma 1:
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.56.51.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.57.02.jpeg" width="800" height="400">
</p>

- Toma 2:

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.57.39.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.57.47.jpeg" width="800" height="400">
</p>

###  4.1.3. Prueba 3 (Flexión de brazo con contrapeso)

- Toma 1:

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.58.48.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.58.48%20(1).jpeg" width="800" height="400">
</p>

- Toma 2:

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.59.47.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.59.47%20(1).jpeg" width="800" height="400">
</p>

### 4.1.4. Prueba 4 (Basal de fuerzas)
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.00.54.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.00.54%20(1).jpeg" width="800" height="400">
</p>

### 4.1.5. Prueba 5

- Toma 1:
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.01.35.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.00.54%20(1).jpeg" width="800" height="400">
</p>

- Toma 2: 
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.03.10.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.03.23.jpeg" width="800" height="400">
</p>

## 4.2. Experimento 2: Gastrocnemio

### 4.2.1. Prueba 1 (Basal)
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.04.17.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.04.17%20(1).jpeg" width="800" height="400">
</p>

### 4.2.2. Prueba 2 
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.05.00.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.05.06.jpeg" width="800" height="400">
</p>

### 4.2.3. Prueba 3
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.05.41.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.05.41%20(1).jpeg" width="800" height="400">
</p>

# 5. Discusión
La señal electromiográfica de superficie presenta su mayor contenido espectral significativo dentro de un rango de 5 a 500 Hz con la mayor concentración de potencia entre los 20 y 250 Hz [3]. Rangos que no serían idénticos para todos los músculos del cuerpo, esto debido a que depende de múltiples factores, tales como la fibra muscular, el tamaño del músculo, la profundidad de las fibras y la cantidad de tejido adiposo que se pueda encontrar entre el músculo y el electrodo. En este caso se analiza en un primer momento al bíceps braquial, el cual al ser un músculo grande, superficial y con una alta proporción de fibras tipo II, su contenido espectral significativo se distribuye entre 20 a 450 Hz, reconociendo que la mayor potencia concentrada se da entre 50 y 150 Hz durante las contracciones voluntarias y una frecuencia mediana ubicada entre 80 y 120 Hz. En un segundo momento se analizó el comportamiento del gastrocnemio, el cual cuenta con una mayor proporción de fibras tipo I y estar parcialmente cubierto por tejido subcutáneo, presenta un espectro ligeramente desplazado hacia frecuencias más bajas, con una frecuencia mediana menor entre 40 a 100 Hz. Estos valores serían distintos para áreas tales como la fácil, donde al ser músculos pequeños y superficiales producen contracciones de baja amplitud, cuyo rango óptimo de adquisición se sitúa entre 15 a 25 Hz como corte inferior y 400 a 500 Hz como corte superior [4]. Estas diferencias demuestran que aunque la banda general de la EMG sea similar, la distribución espectral e incluso la manera de procesar las señales varían según la región anatómica. 
</p>
Es importante señalar que para el procesamiento de las señales, el sensor EMG del BITalino ya realiza un acondicionamiento analógico de la señal a nivel de hardware antes de que se llegue al ADC, motivo por el cual la señal exportada desde OpenSignals no es una señal cruda. De hecho el sensor incluye un amplificador de instrumentación con ganancia cercana a 1000x, un filtro pasa banda analógico integrado y un alto rechazo en modo común que atenuaría significativamente la interferencia eléctrica [5]. Es debido a ello que en el procesamiento realizado en python para este laboratorio fue suficiente con eliminar la componente DC y aplicar una Transformada Rápida de Fourier para analizar el contenido espectral, sin necesidad de aplicar un filtro pasa banda adicional ni un filtro Notch a 60 Hz para suprimir la interferencia de la red eléctrica del Perú.
</p>
Respecto a la amplitud de la señal EMG, esta estaría directamente relacionada con el número de unidades motoras reclutadas y su frecuencia de disparo, variando según la intensidad de la contracción y el músculo estudiado. Durante el experimento del bíceps braquial durante la Prueba 1, reposo basal, se mostró amplitudes muy bajas cercanas a la línea base y confirmando de esta manera la ausencia de actividad eléctrica ; en la Prueba 2, flexión sin carga, se observa una clara actividad EMG con amplitudes moderadas; en la Prueba 3, flexión con contrapeso de 2 kg, la amplitud aumentó notablemente respecto a la Prueba 2; en la Prueba 5, fuerza isométrica contra otra persona, se observaron las amplitudes más altas del experimento, ya que una contracción isométrica máxima sostenida implica el reclutamiento de prácticamente todas las unidades motoras disponibles. Para el experimento del gastrocnemio, la Prueba 1 se realizó con la participante en bipedestación normal lo que permitió registrar una línea base con amplitudes bajas, ya que en esta postura el gastrocnemio actúa principalmente como estabilizador postural sin requerir un reclutamiento masivo de unidades motoras; en la Prueba 2, la participante se mantuvo en posición de flexión plantar isométrica sostenida soportando todo el peso corporal, lo que generó una amplitud EMG considerablemente alta y mantenida durante todo el intervalo, esto evidencia el reclutamiento masivo de unidades motoras necesario para sostener el peso del cuerpo contra la gravedad; en la Prueba 3 se realizaron ciclos repetidos de flexión plantar isométrica sostenida seguido de la bajada a posición de bipedestación, incrementando progresivamente el tiempo en que se sostenía la posición de flexión plantar, es debido a esto que se puede observar en la  señal, un patrón característico de amplitudes altas alternadas con caídas a la línea base durante las bajadas. Estos experimentos nos demuestran la existencia de diferencias importantes en la amplitud entre distintas localizaciones corporales, ya que el tejido subcutáneo actúa como filtro pasa bajas y atenuador, por lo que en un músculo profundo o cubierta por grasa, producirá una señal de menor amplitud aunque el reclutamiento de fibras sea similar.
</p>
Finalmente, es oportuno señalar que la amplitud de la EMG no es igual a la cantidad de fuerza que un músculo puede generar, a pesar de que ambas variables están correlacionadas mediante una relación monotónica creciente pero no necesariamente lineal. En las pruebas con bíceps se evidencia que al pasar de la Prueba 2 a la Prueba 3, la amplitud aumentó y aún más en la Prueba 5, reflejando el principio de reclutamiento de Henneman. De forma similar, en el experimento del gastrocnemio se evidenció que el paso de la bipedestación normal a la posición de flexión plantar isométrica sostenida implicó un aumento notable de la amplitud EMG, ya que el músculo debió soportar todo el peso corporal. Sin embargo, esta relación no es de igualdad directa, ya que en contracciones dinámicas la relación entre EMG y fuerza se vuelve no lineal, debido a que ante la fatiga, la amplitud EMG puede aumentar mientras la fuerza disminuye; la fuerza articular neta depende de múltiples músculos sinergistas y estas no quedan registradas por el electrodo de un solo músculo. Factores como el tejido adiposo o el *crosstalk* distorsionan la amplitud registrada sin afectar la fuerza real. Es por ello que la EMG debe ser considerada como un indicador de activación neuromuscular más no como una medida directa de fuerza.

# 6. Bibliografía 
[1] B. Chan, I. Saad, N. Bolong, y K. E. Siew, “A Review of Surface EMG in Clinical Rehabilitation Care Systems Design”, en 2021 IEEE 19th Student Conference on Research and Development (SCOReD), nov. 2021, pp. 371–376. doi: 10.1109/SCOReD53546.2021.9652736.
</p>
[2] M. Boyer, L. Bouyer, J.-S. Roy, y A. Campeau-Lecours, “Reducing Noise, Artifacts and Interference in Single-Channel EMG Signals: A Review”, Sensors, vol. 23, núm. 6, p. 2927, ene. 2023, doi: 10.3390/s23062927.
</p>
[3] Konrad, P. (2005). The ABC of EMG: A Practical Introduction to Kinesiological Electromyography. Noraxon U.S.A., Inc.
</p>
[4] Van Boxtel, A. (2001). Optimal signal bandwidth for the recording of surface EMG activity of facial, jaw, oral, and neck muscles. Psychophysiology, 38(1), 22–34.
</p>
[5] PLUX-Wireless Biosignals, S.A. (2020). Electromyography (EMG) Sensor Datasheet BITalino (r)evolution. http://bitalino.com/datasheets/REVOLUTION_EMG_Sensor_Datasheet.pdf

