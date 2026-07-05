# LABORATORIO ICA

El electroencefalograma (EEG) constituye una técnica clave y no invasiva para el estudio y registro de la actividad bioeléctrica cerebral con una excelente resolución temporal. Sin embargo, un desafío persistente en el análisis clínico y de investigación es la alta susceptibilidad de las señales registradas en el cuero cabelludo a contaminarse por fuentes exógenas y endógenas, conocidas como artefactos. Entre los artefactos biológicos más críticos se encuentra la actividad electromiográfica (EMG), generada por la activación de los músculos craneofaciales y del cuello.
Dado que las frecuencias de los artefactos musculares se solapan significativamente con los ritmos cerebrales de interés (especialmente en las bandas beta y gamma), los filtros lineales tradicionales resultan insuficientes, destruyendo información cortical valiosa. En este contexto, el Análisis de Componentes Independientes (ICA) se establece como una herramienta matemática de Separación Ciega de Fuentes (BSS) indispensable para descomponer la señal multicanal en componentes estadísticamente independientes, permitiendo aislar y remover el ruido preservando la integridad de los datos cerebrales.

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




## CONCLUSIONES

## REFERENCIAS

