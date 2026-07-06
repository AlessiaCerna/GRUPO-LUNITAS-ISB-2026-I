# LABORATORIO ICA

El electroencefalograma (EEG) constituye una técnica clave y no invasiva para el estudio y registro de la actividad bioeléctrica cerebral con una excelente resolución temporal [1]. Sin embargo, un desafío persistente en el análisis clínico y de investigación es la alta susceptibilidad de las señales registradas en el cuero cabelludo a contaminarse por fuentes exógenas y endógenas, conocidas como artefactos. Entre los artefactos biológicos más críticos se encuentra la actividad electromiográfica (EMG), generada por la activación de los músculos craneofaciales y del cuello.
Dado que las frecuencias de los artefactos musculares se solapan significativamente con los ritmos cerebrales de interés (especialmente en las bandas beta y gamma), los filtros lineales tradicionales resultan insuficientes, destruyendo información cortical valiosa. En este contexto, el Análisis de Componentes Independientes (ICA) se establece como una herramienta matemática de Separación Ciega de Fuentes (BSS) indispensable para descomponer la señal multicanal en componentes estadísticamente independientes, permitiendo aislar y remover el ruido preservando la integridad de los datos cerebrales [2].

## METODOLOGÍA

La metodología de este laboratorio consistió en el preprocesamiento digital, la descomposición por ICA y la clasificación cuantitativa de los componentes obtenidos.

### Preprocesamiento

Se acondicionó la señal cruda para eliminar tendencias de baja frecuencia e interferencias de la red eléctrica, empleando los siguientes filtros digitales lineales:

- Filtro Pasa-Banda (Butterworth): Se configura típicamente un filtro de orden 4 con frecuencias de corte entre 0.5 Hz y 45 Hz (o rangos más amplios según el objetivo). Se utiliza un método de filtrado bidireccional (como filtfilt en Python) para asegurar que la distorsión de fase sea exactamente cero, preservando la alineación temporal de los eventos neurofisiológicos.
- Filtro Notch (Rechaza-Banda): Diseñado específicamente para atenuar la interferencia de la línea eléctrica (50 Hz o 60 Hz según la región geográfica) mediante un filtro notch de fase mínima (iirnotch).

### Modelo Matemático y Algoritmos ICA

El modelo matemático subyacente asume que las señales observadas en los electrodos son mezclas lineales instantáneas de fuentes independientes distribuidas en la corteza y la periferia del cráneo. Tres algoritmos principales se destacan en la literatura especializada para resolver este problema: 

#### FastICA: 
Implementa un enfoque de punto fijo iterativo que maximiza la no-gaussianidad de las proyecciones mediante aproximaciones de la negentropía. Destaca por su convergencia matemática cúbica o cuadrática, lo que se traduce en una alta eficiencia computacional.
#### Extended Infomax: 
Basado en el principio de optimización de la información, busca maximizar la entropía conjunta de una red neuronal alimentada con las señales. La extensión "Extended" permite modelar tanto fuentes con distribuciones sub-gaussianas como super-gaussianas (esencial para separar simultáneamente
parpadeos y ritmos estables). 
#### JADE (Joint Approximate Diagonalization of Eigenmatrices): 
Emplea un enfoque puramente algebraico basado en matrices de cúmulos de cuarto orden. Mediante rotaciones ortogonales de Jacobi, busca la diagonalización conjunta de estas matrices para identificar las fuentes independientes. 

### Métricas Cuantitativas para la Discriminación de Componentes
Para automatizar la separación de señales puramente cerebrales frente a artefactos de tipo muscular, se calculan tres métricas fundamentales sobre las propiedades espectrales y topográficas de la matriz de separación:

## RESULTADOS

El procesamiento aplicado combinó una descomposición modal empírica (EMD) previa a la aplicación de FastICA sobre las funciones modales intrínsecas (IMFs), asimismo, se utilizó la curtosis (|curtosis| > 5) como un criterio para identificar artefactos que tienden a presentar distribuciones más leptocúrticas que la actividad neural de fondo. 

Los resultados muestran un comportamiento heterogéneo, ya que en los registros de reposo (ritmo basal 1 y ritmo basal 2) y en la de parpadeo/masticación, la señal reconstruida se superpone casi por completo a la original, lo que indica que ninguna o muy pocas componentes superaron el umbral de curtosis fijado. Esto es inesperado e ilógico para el registro de parpadeo/masticación, pues se esperaba encontrar impulsos de alta curtosis asociados a artefactos oculares y de movimeintos faciales. De esa manera, se deduce que el umbral de curtosis=5 pudo ser demasiado conservador para este conjunto de datos, o que la descomposición EMD no logró aislar completamente esas fuentes en IMFs independientes antes de aplicar ICA. Por el contrario, en la señal de apertura de ojos sí se observa picos de gran amplitud (asociados con parpadeos), lo que valida parcialmente el método. Finalmente, en las condiciones de música relajante y música estresante se observa una divergencia más marcada entre la señal original y reconstruida, pues la curva reconstruida se presenta como una versión atenuada de la original. Esto podría reflejar que varias componentes con alta curtosis en estos registros correspondían en realidad a actividad neural, como respuestas naturales por el estímulo auditivo, y no exclusivamente a artefactos, lo cual constituye una limitación conocida de los criterios basados en un únicamente la curtosis.

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/Captura%20de%20pantalla%202026-07-05%20165051.png" height="200" width="800">
</p>

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/Captura%20de%20pantalla%202026-07-05%20165057.png" height="200" width="800">
</p>

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/Captura%20de%20pantalla%202026-07-05%20165104.png" height="200" width="850">
</p>

## CONCLUSIONES

Estos hallazgos son consistentes porque ninguna medida aislada, ya sea la pendiente espectral, la periferalidad o, en este caso, la curtosis, logra una discriminación perfecta entre componentes neurales y artefactuales [3]. En este caso, el uso exclusivo de la curtosis como criterio de exclusión resultó efectivo para señales con artefactos impulsivos claros como los parpadeos aislados, pero insuficiente en registros con mayor complejidad espectral, como los de estimulación musical. POr lo que, para trabajos futuros se debe incorporar medidas complementarias como la pendiente espectral y topografía espacial de las componentes, empleando un sensor con más canales, y ajustar el umbral de curtosis de forma específica para cada tipo de tarea, con el fin de optimizar la razón entre preservación de actividad neural y remoción de artefactos.


## REFERENCIAS

[1] M. Gavaret, A. Iftimovici, and E. Pruvost-Robieux, “EEG: Current relevance and promising quantitative analyses,” Revue Neurologique, vol. 179, no. 4, pp. 352–360, Mar. 2023, Available: 10.1016/j.neurol.2022.12.008.

[2] T. Radüntz, J. Scouten, O. Hochmuth, and B. Meffert, “EEG artifact elimination by extraction of ICA-component features using image processing algorithms,” Journal of Neuroscience Methods, vol. 243, pp. 84–93, Feb. 2015, Available: 10.1016/j.jneumeth.2015.01.030.

[3] D. Dharmaprani, H. K. Nguyen, T. W. Lewis, D. DeLosAngeles, J. O. Willoughby, and K. J. Pope, "A comparison of independent component analysis algorithms and measures to discriminate between EEG and artifact components," in Proc. 38th Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. (EMBC), Orlando, FL, USA, 2016, pp. 825–828. Available: 10.1109/EMBC.2016.7590828. 
