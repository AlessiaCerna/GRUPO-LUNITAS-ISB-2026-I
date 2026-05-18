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


### 3.2.2 Prueba 1 - Ritmo basal
La participante permaneció con los ojos cerrados, evitando movimientos faciales y corporales durante 1 minuto. Esta prueba permitió obtener una señal EEG en estado de reposo basal.



### 3.2.3 Prueba 2 - Apertura de ojos y fijación visual
La participante abrió los ojos y mantuvo la mirada fija en un punto durante 1 minuto, con el objetivo de evaluar cambios asociados a la estimulación visual.



### 3.2.4 Prueba 3 - Ritmo basal
Se realizó nuevamente un registro basal de 30 segundos para comparar la estabilidad de la señal EEG respecto a la primera prueba.


### 3.2.5 Prueba 4 - Parpadeo constante y masticación
La participante realizó parpadeos continuos y movimientos de masticación durante 1 minuto, induciendo artefactos musculares y oculares en la señal EEG.


### 3.2.6 Prueba 5 - Ritmo basal
Se efectuó un registro basal adicional de 30 segundos posterior a la generación de artefactos, permitiendo observar la recuperación de la señal.

### 3.2.7 Prueba 6 - Música relajante
La participante escuchó música durante 30 segundos con el objetivo de inducir a un estado de relajación y evaluar posibles cambios en la actividad cerebral.

### 3.2.8 Prueba 7 - Música estresante
La participante esuchó música ruidosa y estresante durante 30 segundos, buscando generar un estado de incomodidad y comparar las variaciones de la señal EEG respecto a la prueba anterior.

## 4. Procesamiento y visualización de señales ECG en Python

### 4.1. Señal 1 - Ritmo basal 1


### 4.2 Señal 2 - Apertura de ojos y fijación visual


### 4.3. Señal 3 - Ritmo basal 2


### 4.4. Señal 4 - Parpadeo constante y masticación

### 4.5. Señal 5 - Ritmo basal 3


### 4.6. Señal 6 - Música relajante


### 4.7. Señal 7 - Música estresante

## 5. Discusión
- **¿Qué banda de frecuencia predomina al cerrar los ojos?**  
  Al cerrar los ojos se observó un mayor predominio de la banda alfa, ya que el participante se encontraba en un estado más relajado y con menor estimulación visual.

- **¿Qué filtro es imprescindible para EEG y por qué?**  
  El filtro más importante es el notch de 60 Hz, porque ayuda a eliminar el ruido producido por la corriente eléctrica del ambiente. Sin este filtro, la señal EEG puede verse alterada y dificultar el análisis.

- **¿Puedes modular conscientemente tu señal EEG? Da un ejemplo.**  
  Sí. Por ejemplo, durante las pruebas se notó que al relajarse y cerrar los ojos la señal cambiaba respecto a cuando el participante resolvía preguntas o realizaba tareas que requerían más concentración.

- **¿Se observan diferencias entre Fp1 y Fp2? ¿Por qué podrían ocurrir?**  
  Sí, aunque las diferencias no fueron muy marcadas. Estas variaciones pueden deberse a movimientos musculares, parpadeos, diferencias en la colocación de los electrodos o a la actividad propia de cada hemisferio cerebral.
## 6. Bibliografía


[1] S. Yun, “Advances, challenges, and prospects of electroencephalography-based biomarkers for psychiatric disorders: a narrative review”, J Yeungnam Med Sci, vol. 41, núm. 4, pp. 261–268, sep. 2024, doi: 10.12701/jyms.2024.00668.

[2] C.-S. Chen, S.-H. Chang, C.-W. Liu, y T.-M. Pan, “Exploring the Potential of Electroencephalography Signal-Based Image Generation Using Diffusion Models: Integrative Framework Combining Mixed Methods and Multimodal Analysis”, JMIR Med Inform, vol. 13, p. e72027, jun. 2025, doi: 10.2196/72027.

[3] X.-Y. Liu et al., “Recent applications of EEG-based brain-computer-interface in the medical field”, Mil Med Res, vol. 12, núm. 1, p. 14, mar. 2025, doi: 10.1186/s40779-025-00598-z.

[4] M. S. Khlief y A. K. Idrees, “A comprehensive review of electroencephalography data analytics”, International Journal of Computer Applications in Technology, vol. 71, núm. 1, pp. 78–88, ene. 2023, doi: 10.1504/IJCAT.2023.131066.

[5] S. Sadiya, T. Alhanai, y M. M. Ghassemi, “Artifact Detection and Correction in EEG data: A Review”, en 2021 10th International IEEE/EMBS Conference on Neural Engineering (NER), may 2021, pp. 495–498. doi: 10.1109/NER49283.2021.9441341.

[6]

[7]

