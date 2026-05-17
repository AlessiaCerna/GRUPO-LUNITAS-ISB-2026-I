# LABORATORIO 6: USO DE BITalino PARA EEG

## Tabla de contenidos
1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Procesamiento y visualización de señales EEG en Python](#4-procesamientoyvisualizacióndeseñalesecgenpython)
5. [Discusión](#5-discusión)
6. [Bibliografía](#6-bibliografía)

# 1. Introducción 
El electroencefalograma (EEG) es una técnica neurofisiológica no invasiva que permite registrar la actividad eléctrica de las neuronas corticales mediante electrodos ubicados en el cuero cabelludo. Esta actividad se manifiesta en forma de ondas cerebrales, caracterizadas por su frecuencia y amplitud, parámetros que reflejan los distintos estados funcionales del cerebro [1].

Las principales bandas de frecuencia del EEG son: delta (δ), theta (θ), alfa (α) y beta (β), cada una asociada a condiciones específicas como el sueño profundo, la relajación, el reposo vigilante o la actividad cognitiva intensa. Aunque el EEG no permite evaluar directamente la actividad de estructuras profundas como el tronco encefálico o el cerebelo, constituye una herramienta esencial para el estudio de la dinámica cortical, tanto en condiciones de reposo como durante la ejecución de tareas [1].

Además de su valor en la investigación neurocientífica, el EEG tiene una amplia aplicación clínica, ya que permite detectar alteraciones en la actividad cerebral que pueden contribuir al diagnóstico de epilepsia, trastornos convulsivos, encefalopatías y otras disfunciones neurológicas [2].

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

### 3.2.7 Prueba 6 - Actividad cognitiva básica
Se realizaron preguntas sencillas durante 30 segundos con el objetivo de inducir una carga cognitiva leve y evaluar posibles cambios en la actividad cerebral.

### 3.2.8 Prueba 7 - Actividad cognitiva compleja
Se realizaron preguntas de mayor dificultad durante 30 segundos, buscando generar una mayor carga cognitiva y comparar las variaciones de la señal EEG respecto a la prueba anterior.




## 4. Procesamiento y visualización de señales ECG en Python



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


[1] 

[2]

[3]

[4]

[5]

[6]

[7]

