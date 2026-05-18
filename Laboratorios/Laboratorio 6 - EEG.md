# LABORATORIO 6: USO DE BITalino PARA EEG

## Tabla de contenidos
1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Procesamiento y visualización de señales EEG en Python](#4-procesamientoyvisualizacióndeseñalesecgenpython)
5. [Discusión](#5-discusión)
6. [Bibliografía](#6-bibliografía)

# 1. Introducción 
El electroencefalograma (EEG) es una técnica neurofisiológica no invasiva que permite registrar la actividad eléctrica cerebral mediante electrodos colocados sobre el cuero cabelludo [1]. Estas señales son generadas principalmente por la actividad sincronizada de las neuronas corticales y se representan en forma de ondas cerebrales con diferentes frecuencias y amplitudes, las cuales reflejan distintos estados funcionales del cerebro [1].

Las señales EEG se clasifican en diferentes bandas de frecuencia: delta (δ), theta (θ), alfa (α) y beta (β). Cada una de ellas se relaciona con distintos estados fisiológicos y cognitivos. Por ejemplo, las ondas alfa predominan durante estados de relajación con ojos cerrados, mientras que las ondas beta suelen aumentar durante tareas que requieren atención o concentración [2]. Gracias a ello, el EEG es ampliamente utilizado para estudiar procesos relacionados con memoria, emociones, atención y carga cognitiva.

Actualmente, el EEG posee múltiples aplicaciones tanto en investigación como en el ámbito clínico. En medicina, se utiliza para apoyar el diagnóstico de epilepsia, trastornos del sueño, encefalopatías y enfermedades neurodegenerativas [3]. Asimismo, en los últimos años ha cobrado gran importancia en el desarrollo de interfaces cerebro-computadora (BCI), sistemas que permiten controlar dispositivos externos mediante señales cerebrales [4].

### Ventajas y desventajas del EEG

Entre las principales ventajas del EEG destaca su alta resolución temporal, ya que permite registrar cambios cerebrales en escalas de milisegundos. Además, es una técnica relativamente económica, portátil y segura, debido a que no requiere procedimientos invasivos ni utiliza radiación. Estas características facilitan su aplicación tanto en hospitales como en laboratorios de investigación [5].

Sin embargo, el EEG también presenta limitaciones importantes. Una de las principales es su baja resolución espacial, ya que las señales eléctricas pueden distorsionarse al atravesar tejidos como el cráneo y el cuero cabelludo. Asimismo, las señales EEG son sensibles a artefactos generados por parpadeos, movimientos musculares o interferencias eléctricas externas, lo que puede afectar la calidad del registro y dificultar su interpretación [5].

# 2. Objetivos
- Montar y configurar un BITalino (r)evolution Board Kit BLE/BT para registrar señales EEG.
- Identificar las ubicaciones Fp1, Fp2 y O2 del sistema internacional 10‑20 y colocar electrodos correctamente.
- Adquirir segmentos EEG en condiciones: basal (ojos abiertos/cerrados), tarea cognitiva y artefactos controlados.
- Aplicar filtro band‑pass 0.8–48 Hz y reconocer los ritmos δ, θ, α, β. 
- Exportar los datos y generar un informe breve con hallazgos cuantitativos.
  
# 3. Metodología

## 3.1 Materiales y equipos
| Equipo / Material                            | Cantidad por grupo |
|----------------------------------------------|--------------------|
| BITalino (r)evolution Board Kit BLE/BT       | 1                  |
| Laptop con Bluetooth 4.0+                    | 1                  |
| Software OpenSignals (r)evolution            | -                  |
| Electrodos Ag/AgCl desechables (gel)         | 3                  |

## 3.2 Procedimiento

### 3.2.1 Conexión de los electrodos
Antes del inicio del registro EEG, se procedió a la colocación de los electrodos siguiendo el sistema internacional 10–20, adaptado para configuración frontal [3]. Se utilizaron electrodos de tipo Ag/AgCl con gel conductor, asegurando una buena adherencia y baja impedancia de contacto.

El montaje se realizó de la siguiente manera:

- **Electrodo activo:** ubicado en la región Fp1, correspondiente al lóbulo frontal izquierdo.
- **Electrodo de referencia:** colocado en la apófisis mastoide derecha.
- **Electrodo de tierra (GND):** ubicado en Fp2, región frontal derecha.
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/EEG/1.jfif" width="400"/>
</p>

### 3.2.2 Prueba 1 - Ritmo basal
La participante permaneció con los ojos cerrados, evitando movimientos faciales y corporales durante 1 minuto. Esta prueba permitió obtener una señal EEG en estado de reposo basal.
<p align="center">
<img width="548" height="447" alt="image" src="https://github.com/user-attachments/assets/8d98edae-db12-4540-99a7-29fc7024cb7a" />

### 3.2.3 Prueba 2 - Apertura de ojos y fijación visual
La participante abrió los ojos y mantuvo la mirada fija en un punto durante 1 minuto, con el objetivo de evaluar cambios asociados a la estimulación visual.
<p align="center">
<img width="546" height="516" alt="image" src="https://github.com/user-attachments/assets/00a81488-f68e-449a-971f-77b3807899d1" />

### 3.2.4 Prueba 3 - Ritmo basal
Se realizó nuevamente un registro basal de 30 segundos para comparar la estabilidad de la señal EEG respecto a la primera prueba.
<p align="center">
<img width="592" height="462" alt="image" src="https://github.com/user-attachments/assets/a11ac763-098d-4a47-9d23-8e3aa4c78a9f" />


### 3.2.5 Prueba 4 - Parpadeo constante y masticación
La participante realizó parpadeos continuos y movimientos de masticación durante 1 minuto, induciendo artefactos musculares y oculares en la señal EEG.
<p align="center">
![Parpadeo constante](https://raw.githubusercontent.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/main/Multimedia/EEG/WhatsApp%20Video%202026-05-17%20at%2011.05.02%20PM%20(1).gif)


### 3.2.6 Prueba 5 - Ritmo basal
Se efectuó un registro basal adicional de 30 segundos posterior a la generación de artefactos, permitiendo observar la recuperación de la señal.
<p align="center">
<img width="448" height="377" alt="image" src="https://github.com/user-attachments/assets/55731267-5c47-4392-9ab4-c284d0202205" />


### 3.2.7 Prueba 6 - Música relajante
La participante escuchó música durante 30 segundos con el objetivo de inducir a un estado de relajación y evaluar posibles cambios en la actividad cerebral.
<p align="center">
<img width="400" height="600" alt="image" src="https://github.com/user-attachments/assets/00802f22-9e19-40dd-a4ec-6e78abfbcd21" />


### 3.2.8 Prueba 7 - Música estresante
La participante esuchó música ruidosa y estresante durante 30 segundos, buscando generar un estado de incomodidad y comparar las variaciones de la señal EEG respecto a la prueba anterior.
<p align="center">
<img width="400" height="600" alt="image" src="https://github.com/user-attachments/assets/da681182-2cb7-4ab9-8488-d22683831f73" />


## 4. Procesamiento y visualización de señales ECG en Python

Las señales pasaron por filtrado pasabanda 0.8–48 Hz, posterior

### 4.1. Señal 1 - Ritmo basal 1
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/se%C3%B1al%201.png" width="1000" height="400"/>
</p>

En el Ritmo Basal 1, la señal oscila predominantemente entre ±5 y ±15 µV, con picos que alcanzan los ±30 µV a lo largo de los 63 segundos de registro.

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/fft%20se%C3%B1al%201.png" width="1000" height="400"/>
</p>

### 4.2 Señal 2 - Apertura de ojos y fijación visual
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/se%C3%B1al%202.png" width="1000" height="400"/>
</p>

La condición de Apertura de Ojos presenta amplitudes similares (±5–20 µV), aunque se identifica una deflexión negativa pronunciada alrededor del segundo 12, que desciende hasta −40 µV, posiblemente asociada a un movimiento ocular involuntario. 

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/fft%20se%C3%B1al%202.png" width="1000" height="400"/>
</p>

### 4.3. Señal 3 - Ritmo basal 2

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/se%C3%B1al%203.png" width="1000" height="400"/>
</p>

El Ritmo Basal 2 exhibe excursiones de hasta ±25–30 µV con un transitorio abrupto notable en torno al segundo 15.

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/fft%20se%C3%B1al%203.png" width="1000" height="400"/>
</p>

### 4.4. Señal 4 - Parpadeo constante y masticación

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/se%C3%B1al%204.png" width="1000" height="400"/>
</p>

La condición de Artefactos es la más irregular del conjunto: la señal mantiene amplitudes sostenidas de ±10–40 µV con una variabilidad morfológica notablemente mayor que en las condiciones de reposo, y eventos de alta amplitud distribuidos de manera continua a lo largo de los 63 segundos.

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/fft%20se%C3%B1al%204.png" width="1000" height="400"/>
</p>

### 4.5. Señal 5 - Ritmo basal 3

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/se%C3%B1al%205.png" width="1000" height="400"/>
</p>

El Ritmo Basal 3 presenta amplitudes de ±5–20 µV.

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/fft%20se%C3%B1al%205.png" width="1000" height="400"/>
</p>

### 4.6. Señal 6 - Música relajante

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/se%C3%B1al%206.png" width="1000" height="400"/>
</p>

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/fft%20se%C3%B1al%206.png" width="1000" height="400"/>
</p>

### 4.7. Señal 7 - Música estresante

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/se%C3%B1al%207.png" width="1000" height="400"/>
</p>

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/fft%20se%C3%B1al%207.png" width="1000" height="400"/>
</p>

## 5. Discusión

Los resultados obtenidos en este laboratorio muestran que el procesamiento de señales EEG con dispositivos portátiles como el BITalino es una tarea que depende fuertemente de las condiciones de registro y de la ubicación de los electrodos. A lo largo de las distintas fases del experimento, se pudo observar cómo el estado del participante y sus movimientos afectan directamente la calidad de la señal.

En primer lugar, los tres registros de reposo fueron los más limpios y consistentes de toda la sesión. En el Ritmo Basal 1 (señal 1), la señal cruda osciló entre ±10–15 µV con picos esporádicos de hasta ±35 µV, y el espectro mostró un pico dominante cerca de 1–2 Hz con amplitud de ~0.9 µV, que cae rápidamente hacia las bandas superiores. Este patrón de decaimiento tipo 1/f, donde la energía es máxima en Delta y disminuye progresivamente en Theta, Alpha y Beta, es exactamente el comportamiento esperado para un cerebro en reposo. El Ritmo Basal 2 (señal 3) presentó amplitudes algo menores (±10–25 µV) y el mismo perfil espectral, aunque con un pico Delta ligeramente más reducido (~0.85 µV), lo que sugiere que el participante mantuvo un estado de reposo comparable. El Ritmo Basal 3 (señal 5), registrado inmediatamente después de la condición de artefactos, recuperó el mismo perfil con picos de ~1.65 µV en Delta, confirmando que el cese de la actividad muscular fue suficiente para retornar al estado de referencia en apenas 30 segundos. La reproducibilidad de este patrón entre los tres basales valida las comparaciones entre condiciones.

En la condición de ojos abiertos, la señal temporal se mantuvo en un rango de ±10–25 µV, con algunas deflexiones que llegaron a −40 µV, probablemente asociadas al momento de apertura ocular y al fenómeno de Bell, en el que la córnea se aproxima a los electrodos frontales generando una deflexión de gran amplitud. El espectro fue el más limpio de todas las condiciones no basales: el pico Delta alcanzó apenas ~0.7 µV y la energía cayó de forma muy suave hacia las frecuencias mayores, manteniéndose por debajo de −20 dB en toda la banda. Se esperaba observar una supresión del ritmo Alpha (alpha blocking) al comparar con los basales, pero esta no fue visible en el espectro. Esto se debe a que el electrodo no estaba posicionado en la zona occipital (Oz), que es donde dicho ritmo se expresa con mayor amplitud.

Al realizar la actividad de masticación y parpadeo, en el dominio del tiempo, la señal cruda mostró deflexiones repetitivas y sostenidas que alcanzaron los ±40 µV a lo largo de los 63 segundos, con una irregularidad mucho mayor que la de los basales. La señal filtrada también mantuvo amplitudes elevadas de ±20–45 µV, lo que confirma que los artefactos musculares no son eliminados por el filtro pasa banda, ya que su espectro se solapa con las bandas de interés del EEG. En cuanto al espectro FFT, el pico en Delta superó los 2.1 µV en amplitud, siendo el más alto de todas las condiciones, y la energía se distribuyó de forma elevada a lo largo de todo el rango de frecuencias, con niveles entre −10 y −20 dB incluso en las bandas Alpha y Beta. Este comportamiento es la superposición del artefacto de parpadeo, que concentra su energía entre 0 y 12 Hz, y del artefacto de masticación, que genera actividad EMG de banda ancha que comienza desde los 2 Hz y se extiende hasta frecuencias altas, invadiendo todas las bandas relevantes del EEG.

Finalmente, durante la actividad con música, la señal supera el rango dinámico del sensor y recorta la onda. Este fenómeno es más frecuente y sostenido en la Música Estresante (señal 7), donde los episodios de clipping son visibles a lo largo de casi toda la grabación, mientras que en la Música Relajante (señal 6) aparecen de forma más intermitente. Esto es coherente con la mayor tensión muscular facial y cefálica que se espera durante la escucha de un estímulo displacentero. En el espectro, la energía se mantiene distribuida en toda la banda como consecuencia directa de la distorsión armónica generada por el recorte. Esto debido a que se generan armónicos artificiales a múltiplos de la frecuencia original que no existen en la señal real. Por ello, los valores espectrales de las dos señales no reflejan la actividad neural verdadera del participante, sino el comportamiento del sistema de adquisición ante una señal que excede su capacidad. Para poder observar los efectos reales de la música sobre el EEG (como el incremento de Theta frontal ante música placentera documentado en la literatura), sería necesario reducir la ganancia del amplificador, mejorar el contacto de los electrodos y controlar la tensión muscular del participante.

### Preguntas

#### ¿Qué banda de frecuencia predomina al cerrar los ojos?
Al cerrar los ojos se esperaba observar un aumento en la banda alfa (8–13 Hz), fenómeno conocido como alpha blocking, ya que el cerebro tiende a sincronizarse en esa frecuencia cuando se reduce la entrada visual. Sin embargo, este efecto no fue claramente visible en los datos. Esto se debe principalmente a que el electrodo no estaba ubicado en la zona occipital (Oz), que es donde el ritmo alfa se expresa con mayor amplitud. Aun así, el perfil espectral de los basales con ojos cerrados mostró una mayor energía en frecuencias bajas respecto a otras condiciones, lo que es coherente con un estado de mayor relajación.

#### ¿Qué filtro es imprescindible para EEG y por qué?
Para el análisis de EEG, el filtro más importante es el pasa banda, que en este caso se configuró entre 0.8 y 45 Hz. Este filtro permite conservar las frecuencias de interés fisiológico (Delta, Theta, Alpha y Beta) mientras elimina el ruido de muy baja frecuencia (movimientos lentos, deriva de la línea base) y el de alta frecuencia (interferencias eléctricas y artefactos musculares de alta banda). En cuanto al filtro notch a 60 Hz, si bien es útil para eliminar el ruido eléctrico de red en contextos con alta frecuencia de muestreo, en este experimento no fue necesario aplicarlo, ya que con una frecuencia de muestreo de 100 Hz la componente de 60 Hz queda fuera del rango representable por la señal (el límite es 50 Hz, la mitad de la frecuencia de muestreo).

#### ¿Puedes modular conscientemente tu señal EEG? Da un ejemplo.
Sí, es posible influir en la señal EEG de forma consciente, aunque en muchos casos los cambios observados no provienen directamente de la actividad cortical sino de la actividad muscular asociada. En este experimento, el ejemplo más claro fue la condición de artefactos: al parpadear voluntariamente y masticar, la señal aumentó notablemente su amplitud en todo el espectro. De forma más sutil, también se espera que cerrar los ojos e intentar relajarse incremente la actividad en la banda alfa, aunque esto depende de la posición del electrodo para poder detectarlo correctamente.

#### ¿Se observan diferencias entre Fp1 y Fp2? ¿Por qué podrían ocurrir?
En este experimento solo se utilizó un canal (A4), por lo que no fue posible comparar directamente Fp1 y Fp2. Sin embargo, en condiciones normales de registro con ambos electrodos, sí suelen observarse diferencias entre hemisferios. Estas pueden deberse a asimetrías en la actividad cortical (por ejemplo, el procesamiento del lenguaje tiende a concentrarse en el hemisferio izquierdo), a diferencias en la colocación o calidad del contacto de los electrodos, o a movimientos faciales asimétricos como parpadeos o contracciones musculares que afectan más a un lado que al otro.
La condición de artefactos fue la que mostró los cambios más claros y esperados: el parpadeo y la masticación generaron un incremento de energía de 10–15 dB en la banda Delta, extendiéndose también hacia Theta y Alpha. Esto confirma que los músculos de la cara y del cuero cabelludo son una fuente de interferencia difícil de evitar y que pueden enmascarar por completo la actividad cerebral cuando están activos. Por otro lado, las condiciones con música no pudieron analizarse de forma válida, ya que la tensión muscular involuntaria del participante saturó el convertidor del dispositivo, distorsionando el espectro en todas las bandas.

Los registros basales mostraron un comportamiento estable y reproducible a lo largo de la sesión, con un perfil espectral de tipo 1/f dominado por la banda Delta. Esto confirma que el protocolo de reposo fue suficiente para que el participante retornara a un estado de referencia comparable tras cada condición de estimulación.
La ausencia de alpha blocking durante la apertura de ojos se atribuye a la posición subóptima del electrodo, alejado de la región occipital donde el ritmo alfa se expresa con mayor amplitud. Esto evidencia que la selección del montaje de electrodos es una variable crítica que puede impedir la observación de fenómenos neurofisiológicos bien establecidos.
La condición de artefactos fue la más exitosa del protocolo: el parpadeo y la masticación generaron un incremento espectral de 10–15 dB en Delta, extendido hacia Theta y Alpha, confirmando que la actividad muscular cefálica contamina todas las bandas relevantes del EEG.

## 6. Bibliografía


[1] S. Yun, “Advances, challenges, and prospects of electroencephalography-based biomarkers for psychiatric disorders: a narrative review”, J Yeungnam Med Sci, vol. 41, núm. 4, pp. 261–268, sep. 2024, doi: 10.12701/jyms.2024.00668.

[2] C.-S. Chen, S.-H. Chang, C.-W. Liu, y T.-M. Pan, “Exploring the Potential of Electroencephalography Signal-Based Image Generation Using Diffusion Models: Integrative Framework Combining Mixed Methods and Multimodal Analysis”, JMIR Med Inform, vol. 13, p. e72027, jun. 2025, doi: 10.2196/72027.

[3] X.-Y. Liu et al., “Recent applications of EEG-based brain-computer-interface in the medical field”, Mil Med Res, vol. 12, núm. 1, p. 14, mar. 2025, doi: 10.1186/s40779-025-00598-z.

[4] M. S. Khlief y A. K. Idrees, “A comprehensive review of electroencephalography data analytics”, International Journal of Computer Applications in Technology, vol. 71, núm. 1, pp. 78–88, ene. 2023, doi: 10.1504/IJCAT.2023.131066.

[5] S. Sadiya, T. Alhanai, y M. M. Ghassemi, “Artifact Detection and Correction in EEG data: A Review”, en 2021 10th International IEEE/EMBS Conference on Neural Engineering (NER), may 2021, pp. 495–498. doi: 10.1109/NER49283.2021.9441341.


