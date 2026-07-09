# MindBalance: Clasificación del Estrés a partir de Biomarcadores EEG

## Introducción

El estrés se define como la respuesta general de activación del organismo ante estímulos que pueden percibirse como un desafío o una amenaza [1]. Desde el punto de vista fisiológico, el estrés involucra la activación del sistema nervioso central y estructuras del sistema límbico que envían señales al hipotálamo para regular al eje hipotálamo-hipófisis-suprarrenal (HPA) y al sistema nervioso simpático (SNS). De esta manera, se generan respuestas para mantener la homeostasis del organismo [2, 3]. El principal efector del eje HPA es el cortisol, conocido como la hormona del estrés, cuya concentración permite evaluar su activación fisiológica; sin embargo, cuando la demanda externa es persistente, el cuerpo recurre a la alostasis como un mecanismo de adaptación dinámica que altera diversos parámetros biológicos para alcanzar un nuevo equilibrio. Si esta respuesta se mantiene en el tiempo, se produce un fenómeno de carga alostática que representa un continuo de desgaste neuroendocrino, lo cual favorece procesos inflamatorios sistémicos y compromete la plasticidad cerebral [2, 3].
Esto último se traduce en una reducción de la conectividad neuronal y de la capacidad del cerebro para generar nuevas redes, lo que dificulta el aprendizaje y la regulación emocional. En esa instancia, el estrés crónico presenta efectos documentados sobre la salud cardiovascular, cognitiva y mental. 

<p align="center">
  <img src="https://github.com/AlessiaCerna/GRUPO-LUNITAS-ISB-2026-I/blob/main/Multimedia/Captura%20de%20pantalla%202026-04-05%20202407.png">
</p>

> Figura 1. Hormona del estrés: cortisol. Recuperado de [4].

## Problemática

A nivel mundial, la OMS ha reportado que alrededor del 40% de la población mundial sufre de estrés de forma continua o crónica, clasificándose como la epidemia de salud del siglo XXI [5]. En Perú, se ha reportado que 3 de cada 10 peruanos presenta un alto nivel de estrés [6]. Asimismo, el 85% de la comunidad educativa de 21 universidades reporta problemas de salud mental, de los cuales, la ansiedad con 82% y el estrés con 79% son más recurrentes [7]. Por lo que su detección temprana y objetiva es de interés tanto clínico como en contextos cotidianos, ya sean educativos o laborales. 
Los  métodos tradicionales de evaluación del estrés dependen predominantemente de autorreportes y cuestionarios psicométricos, los cuales son susceptibles a sesgos subjetivos y no permiten un monitoreo continuo o en tiempo real [8]. El electroencefalograma (EEG) ofrece una alternativa objetiva, no invasiva y de alta resolución temporal para caracterizar estados de activación cortical asociados al estrés [9]. Sin embargo, la mayoría de los estudios en la literatura se basan en datasets adquiridos con un único dispositivo y protocolo experimental, lo que limita la generalización de los modelos resultantes a otros contextos de adquisición. Adicionalmente, la calidad de señal, la densidad de electrodos y la ubicación de las referencias, genera una heterogeneidad topográfica difícil de armonizar mediante técnicas de normalización estándar [10]. 
En consecuencia, existe una necesidad de explorar si los biomarcadores EEG de estrés son suficientemente robustos como para generalizar entre dispositivos de distinta naturaleza y distintas configuraciones de electrodos. Por este motivo, en el presente trabajo se 
## Propuesta solución

Se propone diseñar un pipeline DSP reproducible para extraer TBR, Alpha/Beta, Alpha global, Beta global y FAA a partir de formatos de datos heterogéneos (EDF, CSV comprimido, TXT de OpenSignals).
De esa manera, integrar cuatro datasets EEG de distintos dispositivos bajo un esquema común de clasificación en niveles de estrés y evaluar dos estrategias de normalización — StandardScaler poblacional y baseline normalization. Por último, validar el sistema en hardware portátil de bajo costo (NeuroBIT/BITalino) y cuantificar el domain shift entre dispositivos.


## Plan de actividades

| Fase | Actividades | Semana | 
| :-------: | :-------: |  :-------: | 
| Fase 1: Revisión bibliográfica | Búsqueda y análisis de artículos científicos sobre estrés académico, EEG y estímulos sonoros. | 1 – 2  | 
| Fase 2: Diseño metodológico | Definición del protocolo experimental, variables, métricas EEG y selección de instrumentos de medición (encuestas). | 3 – 4 | 
| Fase 3: Preparación experimental | Configuración del sistema EEG y herramientas de software. Desarrollo de pruebas piloto. |5 – 6|
|Fase 4: Validación inicial| Aplicación del experimento a un grupo reducido de estudiantes. Identificación de posibles errores en el procedimiento, tiempos o registro de señales. | 7|
|Fase 5: Recolección de datos| Aplicación del experimento a los participantes. Registro de señales EEG y aplicación de encuestas.| 8 – 10|
|Fase 6: Procesamiento de señales|Preprocesamiento de EEG (filtrado, eliminación de artefactos). Organización de la base de datos.| 11 – 12|
|Fase 7: Análisis de datos| Extracción de características (biomarcadores EEG) y análisis comparativo entre condiciones. | 13|
|Fase 8: Interpretación de resultados|Integración de resultados EEG y autorreporte. Discusión de hallazgos.|14|
|Fase 9: Informe final y presentación|Redacción del informe final, conclusiones y preparación de la exposición.|15 - 16|



## Referencias
[1] K. Sotelo Castillo and C. Recabarren Jimenez, “Factores asociados al estrés académico en estudiantes universitarios: una revisión crítica,” Universidad Peruana Cayetano Heredia, 2025. [Online]. Available: https://hdl.handle.net/20.500.12866/17582
[2] A. Agorastos and G. P. Chrousos, “The neuroendocrinology of stress: the stress-related continuum of chronic disease development,” Molecular Psychiatry, vol. 27, no. 1, pp. 502–513, Jul. 2021, doi: 10.1038/s41380-021-01224-9. 

[3] B. Chu, K. Marwaha, T. Sanvictores, and D. Ayers, “Physiology, stress reaction,” StatPearls, Jul. 2019, [Online]. Available: https://pubmed.ncbi.nlm.nih.gov/31082164/ 

[4] “Hormona del estrés: cortisol: funciones y enfermedades en las que participa-getein.com.” https://es.getein.com/blog/stress-hormone-cortisol-the-roles-and-diseases-it-takes-part-in_b20

[5] World Health Organization: WHO, “Trastornos mentales,” Sep. 30, 2025. https://www.who.int/es/news-room/fact-sheets/detail/mental-disorders 

[6]“Estrés afecta a más del 30% de limeños,” Noticias - Ministerio De Salud - Plataforma Del Estado Peruano. https://www.gob.pe/institucion/minsa/noticias/43525-estres-afecta-a-mas-del-30-de-limenos 

[7] “Minedu y el Minsa trabajan con 21 universidades públicas en el cuidado de la salud mental,” Noticias - Ministerio De Educación - Plataforma Del Estado Peruano. https://www.gob.pe/institucion/minedu/noticias/52741-minedu-y-el-minsa-trabajan-con-21-universidades-publicas-en-el-cuidado-de-la-salud-mental

[8] A. Arsalan, M. Majid, I. F. Nizami, W. Manzoor, S. M. Anwar, and J. Ryu, “Human Stress Assessment: a comprehensive review of methods using wearable sensors and non-wearable techniques,” arXiv (Cornell University), Feb. 2022, doi: 10.48550/arxiv.2202.03033.

[9] A. Hag, D. Handayani, T. Pillai, T. Mantoro, M. H. Kit, and F. Al-Shargie, “EEG Mental stress assessment using hybrid Multi-Domain feature sets of functional connectivity network and Time-Frequency features,” Sensors, vol. 21, no. 18, p. 6300, Sep. 2021, doi: 10.3390/s21186300.

[10] D. Mikhaylov, M. Saeed, M. H. Alhosani, and Y. F. A. Wahedi, “Comparison of EEG Signal Spectral Characteristics Obtained with Consumer- and Research-Grade Devices,” Sensors, vol. 24, no. 24, p. 8108, Dec. 2024, doi: 10.3390/s24248108. 

