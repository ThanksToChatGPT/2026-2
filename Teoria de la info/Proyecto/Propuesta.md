# Interfaz Cerebro-Computador (BCI) mediante SSVEP

## Idea de proyecto
**Controlar 4 comandos en un computador mirando a 4 puntos específicos**

Para este propósito, se utilizan **Potenciales Evocados Visuales de Estado Estable** (SSVEP, por sus siglas en inglés: *Steady-State Visual Evoked Potentials*) y se construye una **interfaz cerebro-computador** (BCI, *Brain-Computer Interface*).

La arquitectura inicial plantea utilizar dos módulos **AD8232** con electrodos de copa ($\text{Ag/AgCl}$) situados en la región occipital para captar las señales bioeléctricas cerebrales, atenuar ruidos biológicos (musculares y de piel) y preamplificar las microtensiones. Estas señales analógicas se conectan a un convertidor analógico-digital (ADC) **ADS1115** de 16 bits, el cual amplifica las señales mediante su amplificador de ganancia programable (PGA) interno y las digitaliza con alta resolución. Posteriormente, las muestras se transmiten vía $\text{I}^2\text{C}$ hacia un microcontrolador **ESP32**, el cual reenvía los datos en tiempo real hacia una computadora (mediante puerto serie o comunicación inalámbrica). En el computador se procesan las señales en el dominio frecuencial (por ejemplo, mediante la Transformada Rápida de Fourier - FFT o correlación canónica - CCA) para identificar el estímulo observado y traducirlo en comandos directos sobre el sistema operativo.

## Conceptos clave
### Actividad bioeléctrica cerebral y escala de tensiones
El cerebro posee miles de millones de neuronas que se comunican mediante potenciales de acción electroquímicos y corrientes postsinápticas sincronizadas. En la superficie del cuero cabelludo, estas fluctuaciones de potencial eléctrico se encuentran típicamente en la escala de **$10\text{ }\mu\text{V}$ a $100\text{ }\mu\text{V}$** (microvoltios) y en un ancho de banda fisiológico de **$0.5\text{ Hz}$ a $50\text{ Hz}$** (ritmos delta, theta, alfa, beta y gamma). En comparación con fuentes cotidianas de bajo voltaje, como una pila común AA de **$1.5\text{ V}$** (un millón de veces más intensa), o con la actividad cardíaca del ECG (del orden de **$1\text{ mV}$**, unas 10 a 100 veces superior), las ondas cerebrales son extraordinariamente **débiles**, lo que exige una elevada amplificación analógica, bajo piso de ruido y un aislamiento riguroso frente a interferencias externas.

### Respuesta cortical a estímulos visuales periódicos
Cuando el sistema visual humano observa estímulos luminosos o patrones que parpadean a frecuencias periódicas estables comprendidas entre **$4\text{ Hz}$ y $30\text{ Hz}$** (con mayor intensidad de respuesta en la banda de **$8\text{ Hz}$ a $15\text{ Hz}$**), la corteza visual primaria (área V1, en el lóbulo occipital) sincroniza su actividad neural respondiendo exactamente a la misma frecuencia del estímulo y a sus armónicos superiores. Esto se debe a la resonancia y sincronización de las poblaciones neuronales de la vía visual retinogeniculada ante la estimulación fótica continua [1], [3].

### Electroencefalografía (EEG)
La **electroencefalografía (EEG)** consiste en el registro no invasivo de la actividad bioeléctrica cerebral a lo largo del tiempo, capturada mediante electrodos colocados sobre el cuero cabelludo (generalmente siguiendo el sistema internacional 10-20). En entornos clínicos e investigación médica, esto se realiza mediante gorros con electrodos de plata/cloruro de plata ($\text{Ag/AgCl}$), gel conductor para reducir la impedancia de contacto y equipos de adquisición de grado médico con alto rechazo al modo común ($\text{CMRR} > 100\text{ dB}$) y digitalizadores de 24 bits para aislar señales biológicas de microvoltios sin distorsión ni interferencias de la red eléctrica [2].

### Potenciales Evocados Visuales de Estado Estable (SSVEP)
El **SSVEP** (por sus siglas en inglés, *Steady-State Visual Evoked Potential*) consiste en la respuesta periódica continua de la corteza cerebral provocada por una estimulación visual repetitiva a una frecuencia fija. A diferencia de las respuestas transitorias aisladas, al repetirse el estímulo con rapidez las respuestas individuales se superponen y generan una onda periódica cuasi-estacionaria en la zona occipital. En una interfaz cerebro-computador (BCI), este fenómeno permite presentar simultáneamente varios objetivos en pantalla parpadeando a frecuencias diferenciadas (por ejemplo: $9\text{ Hz}$, $11\text{ Hz}$, $13\text{ Hz}$ y $15\text{ Hz}$); al identificar mediante procesamiento espectral cuál frecuencia domina en la señal EEG del usuario, el sistema determina a qué comando se está prestando atención sin requerir un entrenamiento prolongado por parte del usuario [1], [7].

### Módulo AD8232
El **AD8232** de *Analog Devices* es un circuito integrado de front-end analógico concebido principalmente para el acondicionamiento de señales biopotenciales cardíacas (ECG). Incorpora un amplificador de instrumentación con ganancia fija ($\sim 100\text{ V/V}$), un filtro pasabanda activo de dos polos (con frecuencias de corte ajustables mediante componentes externos, típicamente de $0.5\text{ Hz}$ a $40\text{ Hz}$), restauración rápida de línea base y un circuito de accionamiento de pierna derecha (*Right Leg Drive* - RLD) que reduce el ruido de modo común de la red eléctrica ($\text{CMRR} \approx 80\text{ dB}$) [4].

**Integración en el proyecto:** Aunque está diseñado para ECG, su amplificación y filtro analógico pasabanda cubren la banda de interés del SSVEP ($8\text{ Hz} - 20\text{ Hz}$). En este proyecto se emplean dos módulos AD8232 como preamplificadores analógicos de dos canales occipitales bipolares ($O_1$ y $O_2$, con referencia/tierra en el mastoides o lóbulo de la oreja), extrayendo las microtensiones y atenuando el ruido muscular antes de digitalizar.

### Módulo ADS1115
El **ADS1115** de *Texas Instruments* es un convertidor analógico-digital (ADC) de **16 bits** de precisión tipo delta-sigma ($\Delta\Sigma$), con 4 canales multiplexados (o 2 diferenciales), interfaz $\text{I}^2\text{C}$, referencia de tensión interna de alta estabilidad y un amplificador de ganancia programable (PGA) que ofrece rangos de escala desde $\pm 0.256\text{ V}$ hasta $\pm 6.144\text{ V}$, alcanzando una resolución de hasta $7.8125\text{ }\mu\text{V}$ por LSB [5].

**Integración en el proyecto:** Debido a que las ondas cerebrales preamplificadas por el AD8232 aún conservan variaciones de amplitud muy sutiles, el conversor interno del microcontrolador (de 10 o 12 bits, con problemas de linealidad y ruido) no es suficiente. El ADS1115 proporciona la sensibilidad de 16 bits y el sobremuestreo necesarios para digitalizar con alta fidelidad y bajo piso de ruido los dos canales bioeléctricos.

### ESP32
El **ESP32** de *Espressif Systems* es un microcontrolador SoC de 32 bits de doble núcleo Tensilica Xtensa LX6 operando hasta a 240 MHz, con memoria SRAM de 520 KB y conectividad integrada Wi-Fi (802.11 b/g/n) y Bluetooth v4.2 / BLE [6].

**Integración en el proyecto:** Actúa como la unidad embebida de adquisición y enlace. Se encarga de muestrear periódicamente el convertidor ADS1115 mediante el bus $\text{I}^2\text{C}$ a una tasa constante de muestreo (por ejemplo, $128\text{ Hz}$ o $250\text{ Hz}$, respetando el criterio de Nyquist), empaquetar las muestras en tramas estructuradas y transmitirlas en tiempo real a la computadora vía puerto serie USB o inalámbricamente por Wi-Fi (UDP/TCP). La transmisión inalámbrica añade, además, aislamiento galvánico de la red eléctrica, mejorando la seguridad del usuario y disminuyendo el acoplamiento de ruido de $60\text{ Hz}$.

## Viabilidad
Aunque el proyecto emplea módulos AD8232 pensados comercialmente para electrocardiogramas (biopotenciales cardíacos), la física de su amplificador de instrumentación y su ancho de banda activo cubren el rango de frecuencias de las ondas cerebrales de interés en SSVEP ($8\text{ Hz} - 20\text{ Hz}$). Las señales se recolectarán empleando electrodos de copa $\text{Ag/AgCl}$ fijados con gel conductor para reducir la impedancia cutánea por debajo de $10\text{ k}\Omega$; por su parte, el módulo ADS1115 resuelve el requerimiento de sensibilidad analógica mediante sus 16 bits de resolución y ganancia programable.

Con el objetivo de mitigar riesgos técnicos en la ejecución y demostración del proyecto, se contemplan los siguientes planes de contingencia:
1. **Plan B (Reducción de complejidad espectral):** Si la relación señal-a-ruido (SNR) dificulta discernir con suficiente fiabilidad cuatro frecuencias parpadeantes simultáneamente, se simplificará el clasificador a **dos frecuencias bien separadas** (por ejemplo, $10\text{ Hz}$ y $15\text{ Hz}$) para gobernar dos comandos binarios (ej. avanzar / detener o selección izquierda / derecha).
2. **Plan C (Contingencia ante ruido electromagnético severo):** En el caso de que el ruido ambiental en el aula de clases (múltiples computadores, fuentes conmutadas y líneas de $60\text{ Hz}$) supere la capacidad de filtrado del sistema e impida aislar las microtensiones del EEG, se recurrirá a registrar **electrocardiografía (ECG)** con exactamente la misma cadena de hardware (AD8232 + ADS1115 + ESP32). En dicho escenario, se identificarán las ondas del complejo QRS y la variabilidad de la frecuencia cardíaca (HRV) frente a distintos estímulos auditivos, visuales o ejercicio físico leve, validando plenamente las competencias del curso en acondicionamiento, muestreo, filtrado y análisis de señales biológicas en tiempo real.

## Posibles aplicaciones en el mundo real
En un espectro amplio, el registro y procesamiento de biopotenciales eléctricos es un estándar fundamental en medicina, telemetría clínica y bioingeniería: cualquier fenómeno electrofisiológico que involucre despolarización celular —muscular (electromiografía - EMG), cardíaco (electrocardiografía - ECG) o cerebral (electroencefalografía - EEG)— puede cuantificarse y analizarse mediante estas etapas de acondicionamiento y tratamiento digital.

En un contexto más específico, la electroencefalografía y las tecnologías BCI tienen un impacto directo en diversas áreas:
- **Diagnóstico médico neurológico:** Identificación, monitoreo y localización de focos en crisis epilépticas, análisis de trastornos del sueño (apnea, insomnio, narcolepsia), evaluación de encefalopatías, control de profundidad anestésica en cirugía y evaluación del estado de coma.
- **Tecnología asistencial e inclusión motora:** Como se aborda en este trabajo, los sistemas BCI basados en SSVEP constituyen un canal de comunicación alternativo y aumentativo vital para pacientes con parálisis motora severa (afectados por Esclerosis Lateral Amiotrófica - ELA, síndrome de cautiverio o lesiones medulares). Permiten controlar sillas de ruedas eléctricas, prótesis robóticas o redactar texto mediante teclados virtuales únicamente dirigiendo la mirada hacia opciones parpadeantes, sin requerir control muscular voluntario.
- **Neurociencia cognitiva y factores humanos:** Evaluación objetiva de la fatiga mental, estados de alerta, estrés y atención sostenida en pilotos, controladores aéreos u operadores industriales.
- **Interacción humano-máquina (HMI) y entretenimiento:** Control directo de entornos inmersivos en videojuegos, aplicaciones en realidad virtual y sistemas de neurorrehabilitación motora asistida tras accidentes cerebrovasculares (ACV).

## Referencias

[1] X. Gao, M. Xu, M. Cheng, and S. Gao, "A Review on Steady-State Visual Evoked Potential-Based Brain-Computer Interfaces," *IEEE Transactions on Human-Machine Systems*, vol. 51, no. 6, pp. 565–576, 2021. doi: 10.1109/THMS.2021.3112241.

[2] E. Niedermeyer and F. H. Lopes da Silva, *Electroencephalography: Basic Principles, Clinical Applications, and Related Fields*, 5th ed. Philadelphia: Lippincott Williams & Wilkins, 2005.

[3] F.-B. Vialatte, M. Maurice, J. Dauwels, and A. Cichocki, "Steady-state visually evoked potentials: Focus on essential paradigms and future perspectives," *Progress in Neurobiology*, vol. 90, no. 4, pp. 418–438, 2010. doi: 10.1016/j.pneurobio.2009.11.005.

[4] Analog Devices, "AD8232: Single-Lead, Heart Rate Monitor Front End Data Sheet," Analog Devices, Inc., Norwood, MA, Rev. D, 2020. [Online]. Disponible en: https://www.analog.com/media/en/technical-documentation/data-sheets/ad8232.pdf

[5] Texas Instruments, "ADS111x Ultra-Small, Low-Power, 16-Bit Analog-to-Digital Converter with Internal Reference and Oscillator Data Sheet," Texas Instruments Inc., Dallas, TX, SBAS444D, 2018. [Online]. Disponible en: https://www.ti.com/lit/ds/symlink/ads1115.pdf

[6] Espressif Systems, "ESP32 Series Datasheet," Espressif Systems Co., Ltd., Shanghai, China, V4.4, 2024. [Online]. Disponible en: https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf

[7] D. Zhu, J. Bieger, G. Garcia Molina, and R. M. Aarts, "A Survey of Stimulation Methods Used in SSVEP-Based BCIs," *Computational Intelligence and Neuroscience*, vol. 2010, Art. ID 702357, 2010. doi: 10.1155/2010/702357.


[1] X. Gao, M. Xu, M. Cheng, and S. Gao, "A Review on Steady-State Visual Evoked Potential-Based Brain-Computer Interfaces," *IEEE Transactions on Human-Machine Systems*, vol. 51, no. 6, pp. 565–576, 2021. doi: 10.1109/THMS.2021.3112241.

[2] E. Niedermeyer and F. H. Lopes da Silva, *Electroencephalography: Basic Principles, Clinical Applications, and Related Fields*, 5th ed. Philadelphia: Lippincott Williams & Wilkins, 2005.

[3] F.-B. Vialatte, M. Maurice, J. Dauwels, and A. Cichocki, "Steady-state visually evoked potentials: Focus on essential paradigms and future perspectives," *Progress in Neurobiology*, vol. 90, no. 4, pp. 418–438, 2010. doi: 10.1016/j.pneurobio.2009.11.005.

[4] Analog Devices, "AD8232: Single-Lead, Heart Rate Monitor Front End Data Sheet," Analog Devices, Inc., Norwood, MA, Rev. D, 2020. [Online]. Disponible en: https://www.analog.com/media/en/technical-documentation/data-sheets/ad8232.pdf

[5] Texas Instruments, "ADS111x Ultra-Small, Low-Power, 16-Bit Analog-to-Digital Converter with Internal Reference and Oscillator Data Sheet," Texas Instruments Inc., Dallas, TX, SBAS444D, 2018. [Online]. Disponible en: https://www.ti.com/lit/ds/symlink/ads1115.pdf

[6] Espressif Systems, "ESP32 Series Datasheet," Espressif Systems Co., Ltd., Shanghai, China, V4.4, 2024. [Online]. Disponible en: https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf

[7] D. Zhu, J. Bieger, G. Garcia Molina, and R. M. Aarts, "A Survey of Stimulation Methods Used in SSVEP-Based BCIs," *Computational Intelligence and Neuroscience*, vol. 2010, Art. ID 702357, 2010. doi: 10.1155/2010/702357.