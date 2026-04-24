# LABORATORIO 4: USO DE BITalino PARA EMG

## Tabla de contenidos
1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Discusión](#4-discusión)

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

## 3.2 Procedimiento  

### 3.2.1. Prueba 1  
En primer lugar, se registró la señal electromiográfica (EMG) de la participante en condición de reposo, con el fin de establecer una línea base para posteriores comparaciones.  

![Conexión correcta](https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/image003.jpg) 
> **Electrodo rojo (+):** bíceps (zona activa)<br>- **Electrodo negro (–):** bíceps (zona pasiva)<br>- **Electrodo blanco:** espina ilíaca antero-superior (referencia) 


### 3.2.2. Prueba 2  
La participante realizó flexión del brazo izquierdo durante un intervalo de -- segundos, seguido de un período de reposo de -- segundos. Este procedimiento fue repetido en múltiples ciclos consecutivos con el fin de evaluar la variación de la señal EMG entre estados de reposo y contracción.  

### 3.2.3. Prueba 3  
La participante efectuó flexión del brazo izquierdo contra una carga externa de 2 kg, con el objetivo de analizar la respuesta electromiográfica ante un esfuerzo mayor. Posteriormente, se consideró un período de reposo. Este protocolo se repitió en varios ciclos para garantizar la consistencia de los resultados.

### 3.2.4. Prueba 4
Se registró la señal electromiográfica (EMG) de la participante en condición de reposo, con el fin de establecer una línea base para posteriores comparaciones. Las señales captadas provienen del músculo gastrocnemio.

### 3.2.4. Prueba 5
La participante realizó flexión plantar del tobillo durante un intervalo de -- segundos, seguido de un período de reposo de -- segundos. Este procedimiento fue repetido en múltiples ciclos consecutivos con el fin de evaluar la variación de la señal EMG entre estados de reposo y contracción.

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

### 4.1.2. Prueba 2
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.56.51.jpeg" 
       width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.57.02.jpeg" width="800" height="400">
</p>

### 4.1.3. Prueba 3
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.57.39.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.57.47.jpeg" width="800" height="400">
</p>

### 4.1.4. Prueba 4
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.58.48.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.58.48%20(1).jpeg" width="800" height="400">
</p>

### 4.1.5. Prueba 5
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.59.47.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2011.59.47%20(1).jpeg" width="800" height="400">
</p>

### 4.1.6. Prueba 6 (Basal de fuerzas)
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.00.54.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.00.54%20(1).jpeg" width="800" height="400">
</p>

### 4.1.7. Prueba 7
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.01.35.jpeg" width="800" height="400">
</p>
<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/WhatsApp%20Image%202026-04-24%20at%2012.01.35%20(1).jpeg" width="800" height="400">
</p>

### 4.1.8. Prueba 8
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

### 4.2.2. Prueba 2 (Basal)
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
