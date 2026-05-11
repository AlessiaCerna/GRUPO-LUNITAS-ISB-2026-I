# Análisis y Clasificación de Filtros Digitales para el Procesamiento de Señales Biomédicas (ECG, EEG, EMG)
## 1. Introducción
El procesamiento de señales biomédicas presenta desafíos críticos debido a la naturaleza estocástica de los biopotenciales y la presencia inevitable de diversos tipos de ruido. Las señales de Electrocardiografía (ECG), Electroencefalografía (EEG) y Electromiografía (EMG) suelen estar contaminadas por interferencias de la red eléctrica (50/60 Hz), artefactos de movimiento, deriva de la línea base y ruido instrumental. La implementación de filtros digitales no solo busca mejorar la Relación Señal-Ruido (SNR), sino garantizar que la morfología de la señal —crucial para el diagnóstico clínico— permanezca inalterada [1].
## 2. Clasificación y Análisis de Filtros Implementados
### 2.1. Filtros Especializados en Eliminación de Interferencia de Red
#### 2.1.1. Filtro IIR Notch (Ranura) Adaptativo
Se trata de un filtro digital diseñado para la eliminación del ruido eléctrico en señales biomédicas. A diferencia de los filtros convencionales, este tipo se adapta de forma automática ante variaciones temporales en la frecuencia del ruido. 
Su aplicación principal se da en señales ECG y EEG, donde la interferencia de la red eléctrica es frecuente. En particular, este filtro suprime el ruido de 50 o 60 Hz, sus variaciones en el rango de 55.2 a 64.8 Hz, así como armónicos de 120 Hz y 180 Hz. Dicha interferencia puede enmascarar variaciones fisiológicas de pequeña magnitud, lo cual dificulta la detección precisa de actividad cardíaca o cerebral [2]. 

| Ventajas | Desventajas |
| :---: | :---:|
|Menor complejidad computacional que FIR| Puede presentar errores de convergencia si el ruido cambia rápidamente|
|Menor número de coeficientes|
| Seguimiento de frecuencias variables en tiempo real| 

### 2.2. Filtros de Estructura Lineal (FIR e IIR)
#### 2.2.1. Filtro Butterworth Pasa-Bajo
Es un filtro lineal de respuesta infinita al impulso (IIR) que se caracteriza por una respuesta en frecuencia maximalmente plana en la banda de paso, sin ondulaciones. Esta propiedad lo convierte en una opción preferida cuando la preservación de la forma de la señal es prioritaria.
Se emplea en el preprocesamiento de señales ECG para eliminar componentes de alta frecuencia no deseados. Con una frecuencia de corte de 20 Hz, alcanza un SNR de 12.24 dB y un MSE de 0.00577, lo que lo posiciona como el mejor filtro lineal dentro del estudio comparativo. Asimismo, su variante pasa banda, con cortes en 10 Hz y 200 Hz, se aplica en bases de datos como MIT-BIH para el análisis del ritmo sinusal normal [1].

| Ventajas | Desventajas |
| :---: | :---:|
|Respuesta en frecuencia suave y sin distorsión en la banda de paso.|Caída menos pronunciada en comparación con filtros Chebyshev o Elíptico, lo que puede permitir el paso de algunas frecuencias no deseadas cercanas al corte.|
|Balance óptimo entre reducción de ruido y preservación de detalles de la señal.| Su diseño asume condiciones de ruido estacionarias, por lo que su rendimiento disminuye ante señales con ruido variable en el tiempo.|
|Amplia validación en literatura científica y bases de datos estándar como MIT-BIH.|


#### 2.2.2. Filtro FIR Pasa-Bajo
Es un filtro sin retroalimentación, estable por naturaleza y de fácil implementación en hardware como FPGA, lo que lo convierte en una opción ampliamente utilizada en el procesamiento de señales biomédicas.
Se emplea principalmente en señales EMG con el fin de analizar la activación muscular. Su acción filtrante elimina el ruido de alta frecuencia generado durante la adquisición de la señal, así como interferencias de origen electromagnético. Ambas interferencias impiden la identificación precisa del inicio de la activación muscular [3].

| Ventajas | Desventajas |
| :---: | :---:|
|Extracción clara de la envolvente EMG | Mayor número de coeficientes comparado con IIR|
|Alta estabilidad|
|Implementación eficiente en hardware|

### 2.3. Técnicas de Convolución y Ventanas Geométricas
#### 2.3.1. Filtro Pasa-Bajos por Convolución (Geométrico)
Esta técnica de procesamiento se fundamenta en la distribución matemática de una función discreta, mediante la operación de convolución sobre la señal original. Para ello, recurre al uso de ventanas con estructuras geométricas simples, entre las que destacan la gaussiana, la cuadrática, la triangular y la trigonométrica.
Se aplica en señales ECG con el propósito de mejorar aquellas señales afectadas por ruido. De manera específica, suprime el ruido de alta frecuencia, el aliasing y los errores de digitalización. El aliasing, en particular, puede distorsionar ondas de relevancia clínica como la P, el complejo QRS y la onda T [4]. 

| Ventajas | Desventajas |
| :---: | :---:|
|Implementación sencilla|Su eficacia es altamente dependiente del parámetro de control matemático (B); si este parámetro es muy pequeño, la ventana se deforma hacia una función escalón de bajo rendimiento|
|Procesamiento rápido|
|Buena reducción de ruido con ventanas gaussianas|

### 2.4. Filtros de Selección de Banda Fisiológica
#### 2.4.1. Filtro Pasa-Banda (20–500 Hz)
El filtro pasa banda representa una de las técnicas más relevantes en el preprocesamiento de señales EMG, dado que preserva los componentes espectrales con relevancia fisiológica para la actividad muscular. El rango de frecuencias de trabajo se establece entre 20 y 500 Hz.
La frecuencia de corte inferior, fijada en 20 Hz, cumple la función de bloquear la interferencia en la interfaz piel-electrodo y los artefactos de movimiento de baja frecuencia, como los asociados a la respiración. Por su parte, la frecuencia de corte superior, establecida en 500 Hz, actúa sobre el ruido de alta frecuencia proveniente de dispositivos electrónicos del entorno. Ambos límites de corte garantizan que la señal resultante refleje, con fidelidad, la actividad muscular de interés clínico [5, 6].
|Ventajas|Desventajas|
|:---:|:---:|
|Preservación selectiva de la banda fisiológicamente relevante (20–500 Hz), lo que permite un análisis espectral preciso de la actividad muscular.|Las frecuencias de corte son fijas, por lo que el filtro no se adapta ante variaciones en el tipo o nivel de ruido durante la adquisición.|
|Eliminación simultánea de ruido en ambos extremos del espectro, sin necesidad de aplicar múltiples filtros en cascada.|Una selección inadecuada de los límites de corte puede atenuar componentes musculares de baja frecuencia relevantes en contracciones débiles o fatigadas.|
|Amplia validación en literatura científica; el estudio de Menaceur et al. (2024) confirma su uso con cortes en 20 y 500 Hz sobre bases de datos EMG estándar.|En implementaciones IIR, puede introducir distorsión de fase no lineal, lo que afecta la precisión temporal en el análisis de la activación muscular.|

### 2.5. Procesamiento No Lineal y Robusto
#### 2.5.1. Filtro de Mediana Adaptivo
Es un filtro no lineal que ajusta de forma dinámica el tamaño de su ventana de procesamiento en función de las características locales de la señal. A diferencia del filtro de mediana convencional, su capacidad de adaptación le permite responder a variaciones en el nivel de ruido a lo largo del tiempo.
Su aplicación principal se orienta hacia señales ECG con niveles de ruido no uniformes o con componentes de amplitud variable. En particular, elimina el ruido impulsivo, los artefactos de movimiento y las interferencias de línea base, sin comprometer la morfología de ondas clínicas como la P, el complejo QRS y la onda T [1].

|Ventajas|Desventajas|
|:---:|:---:|
|Mayor SNR (17.85 dB) y menor MSE (0.00158) en comparación con todos los demás filtros del estudio, según pruebas sobre la base de datos MIT-BIH.|Mayor costo computacional en comparación con el filtro de mediana estático.|
|Capacidad de adaptación ante señales con ruido dinámico y no uniforme.|Su rendimiento depende del ajuste adecuado del tamaño inicial de la ventana.|
|Preservación de las características morfológicas esenciales de la señal.|

## 3. Referencias

[1] “Adaptive Filtering Strategies for ECG Signal Enhancement: A Comparative study,” IEEE Conference Publication | IEEE Xplore, Apr. 24, 2024. https://ieeexplore.ieee.org/abstract/document/10541144

[2] J. Vega-Pineda, J. L. Durán-Gómez, y D. R. López-Flores, "Evaluación de filtros digitales IIR adaptivos para seguimiento de frecuencia y armónicas asociadas," Revista Electro, vol. 44, pp. 162–168, oct. 2022. [En línea]. Disponible en: https://itchihuahua.mx/revista_electro/2022/SUB-5048.pdf

[3] A. López Del Peso, "DISEÑO E IMPLEMENTACIÓN DEL FILTRADO DE SEÑALES EMG MEDIANTE HERRAMIENTAS DE SÍNTESIS DE ALTO NIVEL BASADAS EN FPGA," Tesis de maestría, 2024. [Online]. Available: https://hdl.handle.net/10115/31583

[4] M. Mora González, F. J. Casillas Rodríguez, J. Muñoz Maciel, J. C. Martínez Romo, F. J. Luna Rosas, C. A. de Luna Ortega, G. Gómez Rosas, y F. G. Peña Lecona, "Reducción de ruido digital en señales ECG utilizando filtraje por convolución," Investigación y Ciencia, vol. 16, núm. 40, pp. 26–32, ene.–abr. 2008. [En línea]. Disponible en: https://www.redalyc.org/pdf/674/67404005.pdf

[5] J.-H. Sul, L. Piyathilaka, D. Moratuwage, S. Dunu Arachchige, A. Jayawardena, G. Kahandawa, y D. M. G. Preethichandra, "Electromyography Signal Acquisition, Filtering, and Data Analysis for Exoskeleton Development," Sensors, vol. 25, núm. 13, art. 4004, jun. 2025, doi: 10.3390/s25134004.

[6] M. J. Hambly, A. C. C. De Sousa, and C. Pizzolato, “Comparison of filtering methods for real-time extraction of the volitional EMG component in electrically stimulated muscles,” Biomedical Signal Processing and Control, vol. 87, p. 105471, Sep. 2023, doi: 10.1016/j.bspc.2023.105471.


