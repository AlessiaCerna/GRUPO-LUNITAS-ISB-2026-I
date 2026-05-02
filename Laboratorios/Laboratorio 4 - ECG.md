# LABORATORIO 4: USO DE BITalino PARA ECG

## Tabla de contenidos
1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Procesamiento y visualización de señales ECG en Python](#4-procesamientoyvisualizacióndeseñalesecgenpython)
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
### 3.2.1 Conexión de los electrodos
En este experimento, para la adquisición de la señal electrocardiográfica (ECG), se emplearon distintas configuraciones de colocación de electrodos basadas en la disposición de Einthoven. En la primera configuración, el electrodo rojo se ubicó en el lado izquierdo, el electrodo negro en el lado derecho y el electrodo blanco (referencia) en la región ilíaca. En la segunda, el electrodo blanco se colocó en el lado izquierdo, el rojo en la región ilíaca y el negro en el lado derecho. Finalmente, en la tercera configuración, el electrodo rojo se posicionó en el lado izquierdo, el blanco en el lado derecho y el negro en la región ilíaca.
Estas disposiciones permitieron registrar la actividad eléctrica del corazón desde diferentes vectores de diferencia de potencial, mientras que el electrodo de referencia contribuyó a estabilizar la señal y atenuar el ruido generado por interferencias externas o movimientos del participante. De esta manera, fue posible obtener registros más claros y confiables, adecuados para el análisis posterior.
### 3.2.2 Basal 1:
Se registró la señal de ECG del participante en estado de reposo con el propósito de obtener una línea base estable y representativa de la actividad cardíaca sin influencia de esfuerzo físico. Esta referencia inicial es esencial, ya que permite comparar posteriormente los cambios en la señal y evaluar con mayor precisión las variaciones generadas bajo distintas condiciones fisiológicas.
### 3.2.3 Prueba 1: Hiperventilación
Se registró la señal de ECG durante una fase de hiperventilación controlada, en la cual el participante realizó 3 ciclos de inspiración profunda, mantener la respiración y espiración. El objetivo de esta etapa fue inducir cambios en la oxigenación y en la regulación del sistema nervioso autónomo, permitiendo evaluar su efecto sobre la actividad eléctrica cardíaca.
### 3.2.4 Prueba 2: Hiperventilación
Nuevamente, se registró la señal de ECG durante una fase de hiperventilación controlada como en la prueba 2, con el fin de observar la reproducibilidad de la respuesta electrocardiovascular y comparar posibles variaciones entre ambos intentos.
### 3.2.5 Basal 2
Se registró nuevamente la señal de ECG en estado de reposo tras la fase de hiperventilación, con el propósito de evaluar la recuperación del sistema cardiovascular y establecer una nueva línea base luego del estímulo respiratorio previo.
### 3.2.6 Prueba 4: Post ejercicio
Se registró la señal de ECG inmediatamente después de que el participante realizara actividad física consistente en subir y bajar escaleras durante 8 minutos. Esta medición tuvo como objetivo analizar la respuesta cardiovascular ante el esfuerzo, incluyendo variaciones en la frecuencia cardíaca y posibles cambios en la morfología de la señal.
### 3.2.7 Prueba 5: Hipoventilación
Se registró la señal de ECG mientras el participante mantenía la respiración el mayor tiempo posible. Esta fase permitió evaluar la respuesta del sistema cardiovascular ante condiciones de apnea voluntaria y su efecto sobre la actividad eléctrica cardíaca.
### 3.2.8 Prueba 6: Hipoventilación
Se realizó un segundo registro de la señal de ECG bajo las mismas condiciones de apnea voluntaria, con el fin de observar la reproducibilidad de la respuesta cardiovascular y comparar posibles variaciones entre ambos intentos.
# 4. Procesamiento y visualización de señales ECG en Python

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

## 4.2. Hiperventilación 1
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

## 4.3. Hiperventilación 2
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

## 4.4. Basal 2 (post hiperventilación)
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

## 4.5. Post ejercicio (subir y bajar escaleras)
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

## 4.6. Hipoventilación 1
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

## 4.7. Hipoventilación 2
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

# 5. Discusión

La señal electrocardiográfica registrada permitió analizar la actividad eléctrica cardíaca desde la superficie corporal, considerando que el ECG representa los cambios eléctricos generados por la despolarización y repolarización del miocardio. En términos fisiológicos, la onda P se relaciona con la despolarización auricular, el complejo QRS con la despolarización ventricular y la onda T con la repolarización ventricular [1]. En este sentido, el análisis de las siete pruebas realizadas permitió observar que la señal ECG no permanece completamente constante, sino que varía según la respiración, el ejercicio, el movimiento corporal, la ubicación de los electrodos y la derivación utilizada.

En primer lugar, durante la condición basal se obtuvo una señal más estable, con menor presencia de artefactos y con complejos QRS más distinguibles. Esto era esperable debido a que la participante se encontraba en reposo, con respiración normal y menor actividad muscular. Esta prueba permitió establecer una referencia inicial para comparar las demás condiciones. En la segunda toma basal, realizada después de las pruebas de hiperventilación, se esperaría que la señal tienda nuevamente hacia un patrón más regular; sin embargo, es posible que todavía se observen ligeras variaciones en la frecuencia cardíaca o en la línea base, debido al efecto residual de la respiración acelerada sobre el sistema cardiovascular.

Respecto a las fuentes de ruido, las más relevantes en la adquisición ECG fueron la deriva de línea base, la interferencia eléctrica, el ruido muscular y los artefactos por movimiento. La deriva de línea base se relaciona principalmente con la respiración, el desplazamiento del tórax y los cambios en la impedancia electrodo-piel. Por ello, durante las pruebas de hiperventilación e hipoventilación se pudieron presentar oscilaciones más evidentes de la línea base. La interferencia eléctrica puede estar asociada a la red eléctrica o a dispositivos cercanos, mientras que el ruido muscular aparece por contracciones involuntarias o tensión corporal durante la toma. Asimismo, los artefactos por movimiento se vuelven más notorios cuando el sujeto cambia de postura, respira de forma forzada o realiza actividad física previa al registro [2]. Debido a ello, el HomeGuide recomienda colocar los electrodos en zonas de baja actividad muscular, preferentemente sobre regiones óseas, para reducir la contaminación por activación muscular y movimiento [1].

En relación con las derivaciones I, II y III, las diferencias observadas en la amplitud y forma del ECG se explican porque cada derivación registra una proyección distinta del vector eléctrico cardíaco. La derivación I mide la diferencia de potencial entre brazo derecho y brazo izquierdo; la derivación II entre brazo derecho y pierna izquierda; y la derivación III entre brazo izquierdo y pierna izquierda [1]. Por lo tanto, aunque el evento eléctrico del corazón sea el mismo, la morfología registrada puede cambiar según el ángulo desde el cual se mide. Si el vector eléctrico se dirige hacia el electrodo positivo, la deflexión tiende a ser positiva y de mayor amplitud; en cambio, si el vector se aleja del electrodo positivo, la amplitud puede disminuir o incluso invertirse. Esto explica por qué el complejo QRS puede observarse con mayor amplitud en una derivación que en otra. En general, la derivación II suele mostrar una señal más clara, debido a que se alinea mejor con el eje eléctrico medio del corazón.

Respecto a la ubicación corporal de los electrodos, se evidencian diferencias importantes entre registros obtenidos en muñecas, clavículas o zonas más cercanas al tórax. Cuando los electrodos se colocan cerca del corazón, la señal suele presentar mejor relación señal-ruido y los componentes P-QRS-T se distinguen con mayor facilidad. En cambio, al registrar desde zonas más distales, como las muñecas, la señal puede presentar menor amplitud o mayor susceptibilidad al movimiento de las extremidades. Esto se debe a que la distancia respecto a la fuente eléctrica aumenta y, además, pueden intervenir otros tejidos que atenúan o modifican la señal captada. Por ello, era esperable encontrar cambios en la amplitud y calidad de la señal según la localización de los electrodos.

Durante las pruebas de hiperventilación, se esperaría un aumento de la frecuencia cardíaca y una mayor variabilidad en la línea base. Esto ocurre porque la respiración rápida y profunda modifica el movimiento torácico, la distancia relativa entre el corazón y los electrodos, y también la actividad autonómica cardiovascular. En consecuencia, los picos R pueden presentar ligeras variaciones de amplitud y los intervalos R-R pueden reducirse si aumenta la frecuencia cardíaca. Además, la guía señala que la respiración puede influir en el ECG debido a que el movimiento del tórax cambia la distancia entre los electrodos ubicados en la piel y el corazón, pudiendo incluso estimarse la frecuencia respiratoria a partir de variaciones en la amplitud de los picos R [1].

En las pruebas de hipoventilación, la señal pudo mostrar un comportamiento distinto al de la hiperventilación. Al disminuir la frecuencia respiratoria o mantener parcialmente la respiración, se reduciría el movimiento torácico periódico, por lo que podría observarse una menor oscilación mecánica de la línea base. Sin embargo, esto no significa que la señal sea completamente estable, ya que la retención o reducción de la ventilación también puede generar respuestas autonómicas, modificando transitoriamente la frecuencia cardíaca y la variabilidad de los intervalos R-R. Por tanto, la hipoventilación puede disminuir ciertos artefactos asociados al movimiento respiratorio, pero al mismo tiempo puede generar cambios fisiológicos en el ritmo cardíaco.

En la prueba post ejercicio, realizada luego de subir y bajar escaleras, se asumió un aumento de la amplitud y una reducción del intervalo R-R, lo cual indicaría un incremento de la frecuencia cardíaca. Este resultado es fisiológicamente esperable porque, después del ejercicio, el organismo requiere aumentar el gasto cardíaco para cubrir la mayor demanda metabólica de los músculos activos. No obstante, es importante señalar que la amplitud del ECG no debe interpretarse como una medida directa de fuerza cardíaca. A diferencia de la EMG, donde la amplitud se relaciona con el reclutamiento de unidades motoras, en el ECG la amplitud depende de la orientación del vector eléctrico, la ubicación de los electrodos, la respiración, la impedancia de la piel y la presencia de movimiento. Por ello, el aumento de amplitud observado después del ejercicio puede deberse tanto a cambios fisiológicos como a factores externos, tales como sudoración, respiración acelerada, movimiento residual o tensión muscular.

Finalmente, para detectar bradicardia o taquicardia en una señal ECG, el parámetro principal no es la amplitud, sino la distancia temporal entre los picos R. Para ello, se identifican los complejos QRS y se calcula el intervalo R-R. A partir de este intervalo se puede estimar la frecuencia cardíaca mediante la relación: Frecuencia cardíaca = 60 / intervalo R-R en segundos

Si los intervalos R-R son prolongados y la frecuencia cardíaca es menor a 60 latidos por minuto en reposo, se considera bradicardia. En cambio, si los intervalos R-R son cortos y la frecuencia cardíaca supera los 100 latidos por minuto en reposo, se considera taquicardia [3]. En este laboratorio, sería esperable que la condición basal presente valores dentro de un rango normal, mientras que la condición post ejercicio y posiblemente las pruebas de hiperventilación presenten una frecuencia cardíaca mayor. Sin embargo, para afirmar la presencia de bradicardia o taquicardia sería necesario calcular los BPM en cada segmento y verificar que los picos R detectados no correspondan a artefactos.

# 6. Bibliografía

[1] PLUX Wireless Biosignals. (2021). *BITalino Home Guide #2: Electrocardiography ECG*. PLUX – Wireless Biosignals, S.A.

[2] Clifford, G. D., Azuaje, F., & McSharry, P. E. (2006). *Advanced Methods and Tools for ECG Data Analysis*. Artech House.

[3] Hall, J. E. (2021). *Guyton and Hall Textbook of Medical Physiology* (14th ed.). Elsevier.

[4] Sörnmo, L., & Laguna, P. (2005). *Bioelectrical Signal Processing in Cardiac and Neurological Applications*. Elsevier Academic Press.

[5] Task Force of the European Society of Cardiology and the North American Society of Pacing and Electrophysiology. (1996). Heart rate variability: Standards of measurement, physiological interpretation, and clinical use. *Circulation, 93*(5), 1043–1065.

# 6. Bibliografía 
[1] “A survey on ECG analysis”, Biomedical Signal Processing and Control, vol. 43, pp. 216–235, may 2018, doi: 10.1016/j.bspc.2018.03.003.

