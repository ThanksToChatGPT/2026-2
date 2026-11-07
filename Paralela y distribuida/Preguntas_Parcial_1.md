# Guía de Preguntas y Respuestas: Parcial 1

> **Materia**: Computación Paralela y Distribuida  
> **Documentos de Referencia**: 02.Siete_modelos_de_concurrencia.pdf, 03.Parallel_Patterns_2026.pdf, 04.Paralelismo_a_nivel_de_Tarea_2026.pdf, 06.Work-Stealing_2026_Parte1_de_5.pdf, 06.Work-Stealing_2026_Parte2_de_5.pdf, 06.Work-Stealing_2026_Parte3_de_5.pdf, Seven_Concurrency_Models_in_Seven_Weeks_2014.pdf, The Recursive Book of Recursion (Al Sweigart, 2022), Que_es_la_recursividad_2026.pdf.

---

### 1. Concurrencia vs. Paralelismo (Charla de Rob Pike: Concurrency is not Parallelism)

- **Referencia**: 02.Siete_modelos_de_concurrencia.pdf
- **Respuesta**:
  - **Concurrencia (*Concurrency*)**: Trata sobre la **estructura y composición** de un programa. Es la capacidad de descomponer un problema en piezas lógicas independientes que pueden manejarse de forma desacoplada (*dealing with lots of things at once*). Es una propiedad del diseño de software.
  - **Paralelismo (*Parallelism*)**: Trata sobre la **ejecución simultánea física** de múltiples cómputos en hardware con múltiples unidades de procesamiento (*doing lots of things at once*). Es una propiedad del hardware y de la ejecución en tiempo de ejecución.
  - **Relación clave**: *"La concurrencia no es paralelismo, aunque lo habilita"*. Un diseño concurrente puede ejecutarse de forma secuencial en un solo núcleo (intercalando tareas en el tiempo) o en paralelo si existen múltiples núcleos disponibles, sin alterar la estructura lógica del software.
  - **Analogía de los Gophers**: Quemar libros obsoletos en un incinerador. Un gopher con una carretilla es secuencial. Dos gophers (uno cargando y otro incinerando con una pila intermedia) forman una estructura **concurrente**. Si se tiene una sola CPU, ambos alternan el trabajo; si se agregan dos CPUs o más carretillas, el sistema escala automáticamente a **paralelo** sin necesidad de reprogramar la lógica.

---

### 2. Dimensiones de la Movilidad en Sistemas Distribuidos

- **Referencia**: 02.Siete_modelos_de_concurrencia.pdf
- **Respuesta**:
  | Dimensión | Definición Técnica | Manifestación en la Práctica |
  |:---|:---|:---|
  | **Movilidad de Código (*Code Mobility*)** | Capacidad del código ejecutable de trasladarse a través de la red hacia el nodo de destino para ser procesado localmente. | Carga dinámica de scripts/applets, agentes móviles, o adaptación automática de la lógica según el ancho de banda y latencia del canal. |
  | **Movilidad de Datos (*Data Mobility*)** | La información se genera en nodos remotos o periféricos y migra entre repositorios o nodos de procesamiento. | Datos capturados por sensores en camiones/IoT; el sistema implementa almacenamiento local (*caching/store-and-forward*) y sincronización asíncrona al restablecer conexión. |
  | **Movilidad de Dispositivos (*Device / Host Mobility*)** | Desplazamiento físico de terminales con conectividad intermitente y topología de red dinámica. | Celulares, vehículos o wearables que entran y salen de cobertura, alternan entre interfaces (Wi-Fi $\leftrightarrow$ 4G/5G) y sufren cortes por consumo de batería. |
  | **Movilidad de Usuarios (*User / Session Mobility*)** | Capacidad del usuario de trasladarse e interactuar con el sistema a través de múltiples terminales sin perder el estado de su sesión. | Iniciar un trámite o trabajo en la computadora de escritorio y continuar en el celular dentro del transporte público en el punto exacto donde se dejó. |

---

### 3. ¿Por qué es necesaria la movilidad?

- **Referencia**: 02.Siete_modelos_de_concurrencia.pdf
- **Respuesta**:
  - La computación moderna ha abandonado el modelo estático de terminales fijas conectadas por redes estables y cableadas.
  - Diseñar sistemas con soporte nativo de movilidad es imperativo porque:
    1. **Tolerancia a fallos e intermitencia**: La conectividad en redes móviles es inherently inestable (pérdidas de paquetes, caídas de señal, fluctuación de latencia). El sistema debe operar en modo desconectado y sincronizar de forma eventual.
    2. **Desacoplamiento temporal y espacial**: Permite que productores y consumidores de información interactúen sin coincidir en tiempo real ni en la misma ubicación geográfica.
    3. **Continuidad y resiliencia del servicio**: El servicio debe mantenerse ininterrumpido a pesar de la conmutación de interfaces de red, migraciones de procesos o cambios de dispositivo por parte del usuario.

---

### 4. ¿Por qué algunos autores no comparten esa clasificación de distribución a nivel de tareas?

- **Referencia**: 03.Parallel_Patterns_2026.pdf y Structured Parallel Programming (McCool, Robison y Reinders, Cap. 2)
- **Respuesta**:
  - Los autores consideran que el término **paralelismo basado en tareas (*task parallelism*)** es **ambiguo e impreciso** cuando se contrasta con el paralelismo de datos (*data parallelism*), debido a que:
    1. Una **tarea** (*task*) es simplemente una unidad básica de trabajo potencialmente paralela con un flujo de control independiente; tanto el paralelismo funcional como el paralelismo de datos se ejecutan en última instancia mediante tareas planificadas sobre hilos.
    2. Clasificar como "de datos" o "de tareas" confunde el concepto de unidad de cómputo con la estructura del problema.
  - En su lugar, proponen una clasificación basada en el **Grado de Regularidad**:
    - **Paralelismo Regular**: Las tareas son similares u homogéneas entre sí y las dependencias de datos y control entre ellas son estáticas y predecibles (facilita la asignación determinista, particionado regular y vectorización/SIMD).
    - **Paralelismo Irregular**: Las tareas no son similares (heterogéneas en tamaño y función) y generan dependencias complejas o impredecibles en tiempo de ejecución (requiere balanceo dinámico de carga, grafos de tareas o algoritmos adaptativos como *work-stealing*).

---

### 5. Actores

- **Referencia**: 02.Siete_modelos_de_concurrencia.pdf y Seven_Concurrency_Models_in_Seven_Weeks_2014.pdf (Cap. 5)
- **Respuesta**:
  - **Paradigma Central**: Modelo de concurrencia basado en entidades autónomas de cómputo denominadas **Actores** (formalizado por Carl Hewitt en 1973).
  - **Principios Operativos Fundamentales**:
    1. **Aislamiento absoluto de memoria**: No existe memoria compartida mutable entre actores. Cada actor posee su propio estado privado.
    2. **Paso de mensajes asíncrono**: La única forma de comunicación entre actores es mediante el envío de mensajes asíncronos no bloqueantes.
    3. **Buzón secuencial (*Mailbox*)**: Cada actor cuenta con una cola de entrada (*mailbox*). Los mensajes entrantes se procesan de manera **estrictamente secuencial**, eliminando de raíz las condiciones de carrera dentro del actor.
    4. **Comportamiento dinámico**: En respuesta a un mensaje, un actor puede:
       - Modificar su estado interno.
       - Enviar un número finito de mensajes a otros actores conocidos.
       - Crear nuevos actores hijos.
  - **Filosofía de Tolerancia a Fallos (*"Let it Crash"*)**:
    - Los actores no intentan capturar defensivamente todas las excepciones críticas. Si un actor falla, se deja morir.
    - Se organizan en **árboles de supervisión**: un actor supervisor monitorea a sus hijos y decide la estrategia de recuperación (reiniciar con estado limpio, abortar o escalar el fallo).
  - **Metáfora vehicular**: **Vehículo Rentado**. Si el automóvil rentado sufre un desperfecto mecánico grave en el camino, no se intenta desarmar el motor en la carretera; se entrega a la agencia y se reemplaza por uno nuevo e idéntico.
  - **Plataformas de Referencia**: Erlang/Elixir (sobre la máquina virtual BEAM), Akka (Scala/Java).

---

### 6. Que_es_la_recursividad_2026.pdf: ¿Qué opina el autor del libro sobre el TCO?

- **Referencia**: The Recursive Book of Recursion (Al Sweigart, 2022) y Que_es_la_recursividad_2026.pdf
- **Respuesta**:
  - **1. ¿Qué es una Llamada de Cola (*Tail Call*) y TCO?**:
    - Una **llamada de cola (*tail call*)** ocurre cuando la llamada recursiva a una función es la **última acción estricta** que ejecuta la función invocadora antes de retornar su valor. No queda ninguna operación pendiente (ni sumas, multiplicaciones ni transformaciones lógicas) que deba ejecutarse tras el retorno de la llamada.
    - **TCO (*Tail Call Optimization* / Optimización de Llamada de Cola)**: Es una optimización en tiempo de compilación o interpretación donde el entorno de ejecución, al reconocer una llamada de cola, **reutiliza el marco de pila (*stack frame*) actual** en lugar de apilar uno nuevo, transformando la recursión en un salto iterativo que consume memoria espacial constante $O(1)$ y previene el desbordamiento de pila (*stack overflow*).
  - **2. Rol de la Función Invocadora (*Caller*) y la Función Invocada (*Callee*)**:
    - **Función Invocadora (*Caller*)**:
      - *En recursión tradicional (no de cola)*: La función invocadora efectúa la llamada recursiva pero **aún tiene trabajo pendiente por hacer** con el valor devuelto. Por ejemplo, en `return n * factorial(n - 1)`, la multiplicación por `n` solo puede realizarse *después* de que la función invocada retorne su resultado. Por lo tanto, la función invocadora está obligada a quedarse suspendida en memoria conservando sus variables locales y su estado.
      - *En recursión de cola (*tail recursion*)*: La función invocadora delega directamente el resultado en la invocada: `return factorial_tail(n - 1, acc * n)`. La invocadora ya finalizó todo su cómputo propio; su única función restante es traspasar de inmediato el valor que le entregue la función invocada (*passthrough*).
    - **Función Invocada (*Callee*)**:
      - Recibe los argumentos actualizados (que en recursión de cola típicamente incluyen un parámetro acumulador que arrastra los resultados parciales calculados hasta el momento).
      - Cuando la función invocada alcanza el caso base, el valor generado es **la respuesta final completa y definitiva del problema**, la cual no requiere ninguna modificación ni cómputo posterior por parte de las funciones invocadoras que la precedieron.
  - **3. Comportamiento del Frame Invocador y del Frame Invocado en la Pila (*Call Stack*)**:
    - **Comportamiento Estándar (Sin TCO)**:
      - Cada vez que se realiza una llamada, se asigna un nuevo marco de activación (**stack frame**) en la cima de la pila (*call stack*) para la función invocada.
      - El **frame invocador** almacena sus variables locales, argumentos y la **dirección de retorno (*return address*)** hacia donde debe retornar el procesador. No puede liberarse porque debe completar las operaciones pendientes (como la multiplicación por `n`).
      - El **frame invocado** se apila encima del frame invocador.
      - Al encadenarse $N$ llamadas recursivas, coexisten $N$ marcos simultáneos en memoria, produciendo un consumo de espacio lineal **$O(N)$**. Si $N$ supera el límite de memoria asignado a la pila, el sistema colapsa en un **desbordamiento de pila (*Stack Overflow* o `RecursionError`)**.
    - **Comportamiento Optimizado (Con TCO)**:
      - El compilador/intérprete detecta que la función invocadora no tiene ninguna operación pendiente y que ninguna de sus variables locales volverá a ser leída tras la llamada.
      - Por lo tanto, el **frame invocador es descartado o sobrescrito directamente en la cima de la pila** por los nuevos parámetros del **frame invocado**.
      - No se asigna memoria adicional: el **frame invocado reutiliza (recicla) exactamente el mismo marco físico del frame invocador**.
      - La dirección de retorno del marco reciclado se mantiene apuntando a la función que originó la primera llamada (el invocador inicial).
      - El tamaño de la pila permanece estrictamente constante en **un solo marco ($O(1)$ de espacio)**, permitiendo ejecutar llamadas recursivas indefinidamente sin consumir memoria extra ni riesgo de desbordamiento.
  - **4. Contraste en Pseudocódigo: Recursión Tradicional vs. Recursión de Cola**:
    ```text
    // Recursión Tradicional (NO de cola: el frame invocador debe esperar la multiplicación)
    funcion factorial(n):
        si n <= 1: retornar 1
        retornar n * factorial(n - 1)  // La multiplicación se realiza AL VOLVER

    // Recursión de Cola (Apta para TCO: retorno directo, el cálculo viaja en el acumulador)
    funcion factorial_tail(n, acc = 1):
        si n <= 1: retornar acc
        retornar factorial_tail(n - 1, acc * n)  // Sin operaciones pendientes al retornar
    ```
  - **5. Postura Crítica de Al Sweigart en *The Recursive Book of Recursion* (2022)**:
    - En su libro, Al Sweigart aborda el TCO con una visión escéptica y pragmática, desmitificando su supuesta condición de "solución mágica" para la recursión:
      1. **Pérdida de Legibilidad y Claridad Intuitiva**: Para hacer que una función sea recursiva de cola se exige obligatoriamente introducir parámetros acumuladores auxiliares (`acc`). Sweigart señala que esto complica la interfaz de la función, enreda el flujo lógico y destruye la elegancia y naturalidad matemática del pensamiento recursivo declarativo.
      2. **Falta de Soporte en Lenguajes Populares**: La mayoría de lenguajes masivos (como Python y prácticamente todos los motores de JavaScript) no implementan TCO. En particular, Guido van Rossum (creador de Python) rechazó expresamente el soporte de TCO para **preservar íntegras las trazas de pila (*tracebacks / stack traces*)**, ya que contar con el historial completo de cada marco con sus variables locales es fundamental para la depuración (*debugging*) y el diagnóstico forense de fallos.
      3. **La Conclusión de Sweigart sobre los Bucles Iterativos**: Dado que lo que hace TCO bajo el capó es transformar la recursión en un ciclo iterativo al reciclar el mismo marco de pila, Sweigart sostiene que **"si un algoritmo se puede formular mediante recursión de cola, es mucho más limpio, directo y recomendable escribir directamente un bucle iterativo (`for` o `while`)"**. La recursión realmente solo se justifica cuando la estructura del problema es intrínsecamente ramificada o de árbol (árboles, grafos, algoritmos de *backtracking* o divide y vencerás), escenarios en los cuales, por haber múltiples llamadas recursivas por nivel, el TCO ni siquiera es aplicable.

---

### 7. ¿Qué es Work, qué es Span, qué es Speedup?

- **Referencia**: 04.Paralelismo_a_nivel_de_Tarea_2026.pdf
- **Respuesta**:
  - **Trabajo (*Work*, $T_1$ o $WORK(G)$)**:
    - Es el número total de operaciones o tiempo total de ejecución de **todos los nodos** del grafo computacional.
    - Equivale al tiempo necesario para completar el programa sobre un único procesador ($P = 1$):
      $$WORK(G) = T_1 = \sum_{v \in V} \text{time}(v)$$
    - Satisface la **Ley del Trabajo**: $T_P \ge \frac{T_1}{P}$.
  - **Extensión / Tramo Crítico (*Span*, $T_\infty$ o $SPAN(G)$)**:
    - Es la longitud temporal del **camino dirigido más largo** en el grafo de dependencias acíclico (DAG).
    - Equivale al tiempo que tomaría ejecutar el programa en un sistema con **infinitos procesadores** ($P = \infty$).
    - Representa el límite físico infranqueable impuesto por las dependencias de datos seriales; satisface la **Ley de la Extensión**:
      $$T_P \ge T_\infty$$
  - **Aceleración (*Speedup*, $S_p$)**:
    - Razón entre el tiempo de ejecución en un procesador y el tiempo en $p$ procesadores:
      $$S_p = \frac{T_1}{T_p}$$
    - **Límite Teórico Absoluto (Paralelismo Ideal)**:
      $$S_p \le \frac{WORK(G)}{SPAN(G)} = \frac{T_1}{T_\infty}$$
    - **Speedup Lineal**: $S_p = p$ (escalabilidad ideal).
    - **Speedup Superlineal**: $S_p > p$, alcanzable en sistemas reales gracias a la multiplicación de memoria caché ($L1/L2/L3$) de los múltiples núcleos, reduciendo drásticamente los fallos de acceso a RAM.

---

### 8. Tramo Computacional (Diagramas, tiempos, forks)

- **Referencia**: 04.Paralelismo_a_nivel_de_Tarea_2026.pdf
- **Respuesta**:
  - **Definición**: Un cómputo multihilo se modela formalmente como un **Grafo Dirigido Acíclico (DAG)** $G = (V, E)$, que define un conjunto parcialmente ordenado (POSET) de instrucciones:
    - **Vértices ($V$)**: Representan tareas o pasos elementales de cómputo. Cada nodo $v \in V$ posee un tiempo de duración $\text{time}(v)$.
    - **Arcos ($E$)**: Representan relaciones de dependencia temporal o precedencia causal:
      - **Arcos de continuación (`continue`)**: Conectan pasos secuenciales consecutivos dentro de la **misma tarea**.
      - **Arcos de bifurcación (`fork` / `spawn`)**: Conectan una instrucción generadora con la primera instrucción de la **tarea hija**.
      - **Arcos de unión (`join` / `sync`)**: Conectan la terminación de una tarea con el punto de sincronización de la **tarea padre**.
  - **Cálculo de Tiempos y Caminos**:
    - La duración de un camino dirigido $C = (v_1, v_2, \dots, v_k)$ es la suma de los tiempos de sus vértices: $\text{length}(C) = \sum_{v \in C} \text{time}(v)$.
    - El **tramo computacional crítico (*critical path*)** es el camino con mayor duración total: $SPAN(G) = \max_C \text{length}(C)$.
    - **Holgura (*Slack*)**: Tareas que están fuera del tramo crítico disponen de holgura temporal y pueden demorarse o postergarse sin incrementar el tiempo global de ejecución, siempre que haya procesadores disponibles.

---

### 9. Finish, Async, Paralelismo, Pseudolenguaje

- **Referencia**: 04.Paralelismo_a_nivel_de_Tarea_2026.pdf
- **Respuesta**:
  - Primitivas estructuradas de control paralelo utilizadas en la notación algorítmica:
    - **`async { S }`**: Primitiva de bifurcación (*fork*). Lanza el bloque de instrucciones `S` como una nueva tarea asíncrona concurrente. El hilo que invoca `async` no se detiene; continúa de inmediato con la siguiente instrucción.
    - **`finish { ... }`**: Primitiva de sincronización y unión de ámbito (*join scope*). Delimita un bloque de instrucciones compuesto. El flujo de ejecución no puede salir del bloque `finish` hasta que **todas** las tareas generadas dinámicamente con `async` dentro de su cuerpo hayan finalizado completamente.
  - **Ventajas del modelo estructurado frente a hilos libres**:
    - Previene la fuga de tareas e hilos huérfanos (*orphan tasks*).
    - Facilita el análisis modular del grafo de dependencias y la garantía formal de que todo subárbol de computación concluye antes de continuar.

---

### 10. ¿Condiciones de Coffman?

- **Referencia**: 04.Paralelismo_a_nivel_de_Tarea_2026.pdf
- **Respuesta**:
  - Para que ocurra un **interbloqueo (*deadlock*)** en un sistema concurrente, deben cumplirse **simultáneamente las cuatro condiciones de Coffman** (Edward G. Coffman Jr., 1971):
    1. **Exclusión Mutua (*Mutual Exclusion*)**: Al menos un recurso debe ser retenido en un modo no compartible (solo un hilo o proceso a la vez puede utilizarlo).
    2. **Retención y Espera (*Hold and Wait*)**: Un hilo retiene al menos un recurso asignado mientras espera activamente la adquisición de otros recursos adicionales retenidos por otros hilos.
    3. **No Expropiación (*No Preemption*)**: Los recursos asignados no pueden ser arrebatados forzosamente por el sistema; solo pueden ser liberados de manera voluntaria por el hilo que los retiene al culminar su operación.
    4. **Espera Circular (*Circular Wait*)**: Existe una cadena circular cerrada de hilos $\{T_0, T_1, \dots, T_n\}$ tal que $T_0$ espera un recurso retenido por $T_1$, $T_1$ espera a $T_2$, ..., y $T_n$ espera un recurso retenido por $T_0$.
  - **Estrategia de prevención**: Romper o invalidar **al menos una** de estas cuatro condiciones hace imposible la ocurrencia de un interbloqueo (por ejemplo, imponer un ordenamiento global estricto en la adquisición de cerrojos elimina la espera circular).

---

### 11. Paul Butcher: Metáforas de Carreteras y Carros (Siete Modelos de Concurrencia)

- **Referencia**: 02.Siete_modelos_de_concurrencia.pdf y Seven_Concurrency_Models_in_Seven_Weeks_2014.pdf
- **Respuesta**:
  | # | Modelo de Concurrencia | Metáfora Vehicular de Paul Butcher | Significado Técnico |
  |:---:|:---|:---|:---|
  | **1** | **Hilos y Cerrojos** (*Threads & Locks*) | **Ford Modelo T** | Primitivo, tosco, peligroso y sin comodidades modernas; puede volcarse si no se conduce con extremo rigor, pero fue el que motorizó la industria y sustenta la base de la máquina física. |
  | **2** | **Programación Funcional** | **Celdas de Combustible de Hidrógeno** | Limpio, eficiente, avanzado y libre de emisiones contaminantes (sin mutabilidad ni efectos secundarios), aunque su adopción generalizada aún afronta barreras en la industria masiva. |
  | **3** | **La Manera Clojure** | **Vehículo Híbrido** | Combina dos tecnologías distintas: separa la **identidad** mutable del **estado** inmutable mediante referencias administradas (*Atoms*, *STM*). |
  | **4** | **Actores** | **Vehículo Rentado** | Si sufre una falla en ruta, no te detienes a repararlo pieza por pieza: se devuelve y se cambia por otro nuevo (*filosofía "Let it crash"* con supervisores jerárquicos). |
  | **5** | **CSP** (*Communicating Sequential Processes*) | **Red de Carreteras e Infraestructura** | La fluidez y eficiencia del transporte no depende de las prestaciones del automóvil, sino de la infraestructura de canales y autopistas por donde fluyen los mensajes. |
  | **6** | **Paralelismo de Datos** | **Autopista Multicarril** | No importa que los vehículos individuales avancen a velocidad moderada; tener cientos de carriles paralelos permite transportar una cantidad gigantesca de datos homogéneos simultáneamente (GPUs/SIMD). |
  | **7** | **Arquitectura Lambda** | **Camión de 18 ruedas + Flota de camionetas** | El camión pesado transporta volúmenes colosales en trayectos largos con latencia (*Capa Batch histórica*); las camionetas entregan pedidos urgentes en tiempo real (*Capa Speed de streaming*). |

---

### 12. Ley de Amdahl

- **Referencia**: 04.Paralelismo_a_nivel_de_Tarea_2026.pdf
- **Respuesta**:
  - Modela la ganancia máxima de aceleración (*speedup*) al incrementar el número de procesadores $p$ sobre un problema de **tamaño fijo (carga constante)** (Gene Amdahl, 1967):
    $$S_p = \frac{1}{q + \frac{1 - q}{p}} = \frac{1}{(1 - P) + \frac{P}{p}} \le \frac{1}{q}$$
    - $q$: Fracción estrictamente serial / no paralelizable del programa ($q = 1 - P$).
    - $P$: Fracción paralelizable del programa.
    - $p$: Número de procesadores.
  - **Límite Asintótico Infranqueable**:
    $$\lim_{p \to \infty} S_p = \frac{1}{q}$$
  - **Conclusión Práctica**: La porción serial impone un cuello de botella infranqueable. Por ejemplo:
    - Si el $10\%$ del programa es secuencial ($q = 0.1$), el speedup máximo teórico jamás superará $10\times$ ($\frac{1}{0.1} = 10$), aun si se utilizan $10.000$ núcleos.
  - **Vínculo con el Grafo Computacional**:
    $$q \approx \frac{SPAN(G)}{WORK(G)}$$

---

### 13. Sobrecarga (Overhead): Significado del Trabajo Adicional de Inicio y Sincronización

- **Referencia**: 04.Paralelismo_a_nivel_de_Tarea_2026.pdf
- **Respuesta**:
  - **Sobrecarga (*Overhead*)**: Es el tiempo de procesamiento y consumo de recursos que no realiza trabajo computacional útil del problema, sino que se invierte en gestionar el paralelismo:
    - Creación y destrucción de tareas e hilos.
    - Encolado, desencolado y planificación (*scheduling*).
    - Costos de sincronización (barreras, contención de cerrojos, resolución de `finish`/`join`).
    - Comunicación y mantenimiento de coherencia de memoria caché.
  - **Representación Gráfica en Diagramas de Ejecución**:
    - **Barras Azules**: Tiempo de ejecución del cómputo productivo útil.
    - **Barras Amarillas**: **Sobrecarga de gestión y sincronización (*overhead*)**.
  - **Principio de Granularidad**: Si las tareas son de grano demasiado fino, la sobrecarga acumulada (tiempo amarillo) superará al cómputo útil (azul), haciendo que el programa paralelo tarde más que la versión secuencial. Se mitiga mediante árboles de bifurcación/reducción ($O(\log p)$) o agrupamiento en bloques de granularidad adecuada.

---

### 14. ¿Qué es un Algoritmo Online?

- **Referencia**: 06.Work-Stealing_2026_Parte2_de_5.pdf
- **Respuesta**:
  - Un algoritmo de planificación paralela se clasifica formalmente como **Online (*Online Algorithm*)** (Blumofe & Leiserson, 1999) si en cada paso discreto de tiempo $t$:
    1. Ha calculado y ejecutado los primeros $t-1$ pasos del cómputo.
    2. Para tomar la decisión de qué instrucción ejecutar en el paso $t$, utiliza **únicamente la información observada y disponible hasta el paso $t-1$**.
    3. **Cero omnisciencia / Sin conocimiento del futuro**: Desconoce por completo qué instrucciones vendrán después, cuántas tareas hijas se engendrarán en subárboles no expandidos o cuánto durará cada subcómputo.
  - Refleja el funcionamiento real de los planificadores dinámicos en tiempo de ejecución (*runtimes* como Java ForkJoin, Cilk u OpenMP), a diferencia de los planificadores *offline* que requieren conocer el grafo completo por anticipado.

---

### 15. Reglas de Hojas Ocupadas (Busy-Leaves)

- **Referencia**: 06.Work-Stealing_2026_Parte2_de_5.pdf
- **Respuesta**:
  - Algoritmo de Hojas Ocupadas (*Busy-Leaves*) sobre Pool Global Centralizado (Blumofe & Leiserson):
  1. **Regla 1: Spawns (Creación)**:
     - Si el hilo activo $a$ ejecuta una instrucción `spawn` engendrando un hijo $b$:
     - El procesador concluye el paso devolviendo al padre $a$ al pool global.
     - En el siguiente paso, el procesador **toma de inmediato al hijo $b$** y comienza a ejecutarlo.
     - *Propósito*: $b$ pasa a ser la nueva hoja del subárbol y queda inmediatamente ocupada por el procesador.
  2. **Regla 2: Stalls (Postergaciones / Bloqueo)**:
     - Si el hilo activo $a$ se posterga o suspende (a la espera de un dato de un arco de unión no resuelto):
     - El procesador devuelve $a$ al pool global.
     - El procesador inicia el siguiente paso en estado **ocioso** (listo para retirar otra tarea lista del pool).
     - *Invariante crítica*: En computaciones estrictas, **un hilo hoja nunca se suspende**; únicamente se suspenden ancestros esperando descendientes.
  3. **Regla 3: Dies (Finalizaciones)**:
     - Si el hilo activo $b$ completa su última instrucción y muere:
     - El procesador inspecciona el estado de su hilo padre $a$:
       - **Caso a (Padre liberado)**: Si el padre $a$ **no tiene ningún otro hijo vivo** y ningún otro procesador lo está ejecutando, el procesador extrae a $a$ del pool y **lo retoma en el siguiente paso**.
       - **Caso b (Padre retenido)**: Si el padre $a$ aún posee otros hijos vivos o ya está siendo ejecutado por otro procesador, el procesador actual **inicia el siguiente paso ocioso**.

---

### 16. Reglas de Work-Stealing (Ready Deques Distribuidas)

- **Referencia**: 06.Work-Stealing_2026_Parte3_de_5.pdf
- **Respuesta**:
  - Cada procesador gestiona una cola doblemente terminada (**Ready Deque**):
    - **Bottom**: Extremo privado para el procesador local (opera como **pila / LIFO**, maximizando la localidad temporal de caché).
    - **Top**: Extremo público accesible a ladrones (opera como **cola / FIFO**, robando tareas antiguas de grano grueso cerca de la raíz).
  - **Las Cuatro Reglas Operativas**:
    1. **Regla 1: Spawn (Bifurcación)**:
       - Si el hilo activo $a$ ejecuta un `spawn` creando al hijo $b$:
       - El padre $a$ se inserta (`push`) en el **bottom** de la *ready deque* local.
       - El procesador pasa a ejecutar de inmediato al hijo $b$ en el siguiente paso.
    2. **Regla 2: Stall (Postergación)**:
       - Si el hilo activo $a$ se posterga por una dependencia no resuelta:
       - El procesador inspecciona su *ready deque* local:
         - Si tiene hilos: extrae (`pop`) del **bottom** y continúa cómputo.
         - Si está vacía: pasa a rol de **ladrón (*thief*)** y roba del **top** de la deque de una víctima elegida al azar de manera uniforme.
    3. **Regla 3: Die (Finalización)**:
       - Si el hilo activo $a$ concluye su última instrucción y muere:
       - Aplica **exactamente la misma lógica de la Regla 2 (Stall)**: extrae del *bottom* local o roba del *top* de una víctima al azar.
    4. **Regla 4: Enable (Habilitación de Hilo Postergado)**:
       - Si la instrucción del hilo $a$ satisface la última dependencia pendiente de un hilo postergado $b$ (que en computaciones completamente estrictas es siempre su padre):
       - El hilo habilitado $b$ se coloca en el **bottom** de la *ready deque* local.
       - *Propiedad estructural*: Esto **solo puede ocurrir cuando la deque local está vacía ($k=0$)**, ya que si tuviera hilos ($k > 0$), el padre ya estaría en el *bottom* en estado `ready` y no habría podido estar postergado (*stalled*).
  - **Regla de Prioridad para Eventos Simultáneos**:
    - Si un hilo habilita a otro y en el mismo paso se posterga o muere:
    - Se despacha **primero la Regla 4 (Enable)** y **posteriormente la Regla 2 (Stall) o 3 (Die)**. Esto asegura que el hilo padre habilitado quede registrado en la deque antes de que el procesador quede desocupado o pase a robar.

---

### 17. Prueba del Lema 4

- **Referencia**: 06.Work-Stealing_2026_Parte3_de_5.pdf
- **Respuesta**:
  - **Contexto**: El Lema 4 es el lema estructural central que vincula la disciplina de colas dobles locales con las propiedades topológicas del árbol de generación en **computaciones completamente estrictas** (Blumofe & Leiserson, 1999).
  - **Enunciado Formal del Lema 4**:
    Sea un procesador $p$ que en un instante ejecuta al hilo $\Gamma_0$, y sean $\Gamma_1, \Gamma_2, \dots, \Gamma_k$ los $k$ hilos alojados en su *ready deque* ordenados desde el **Bottom** ($\Gamma_1$) hacia el **Top** ($\Gamma_k$). Si $k > 0$, se satisfacen rigurosamente dos propiedades:
    1. **Propiedad 1 ("Ser el hilo padre")**: Para todo $i = 1, 2, \dots, k$, el hilo $\Gamma_i$ es el **padre directo** del hilo $\Gamma_{i-1}$ en el árbol de generación ($\Gamma_1$ es padre de $\Gamma_0$; $\Gamma_2$ es padre de $\Gamma_1$; $\dots$).
    2. **Propiedad 2 ("Padre no procesado")**: Si $k > 1$, para todo $i = 1, 2, \dots, k-1$, el hilo $\Gamma_i$ **no ha sido procesado** desde que engendró a su hijo $\Gamma_{i-1}$.
  - **Demostración por Inducción Matemática sobre los pasos de tiempo $t$**:
    - **Caso Base ($t=0$)**: Al inicio, el hilo raíz está en la deque de un solo procesador y las demás están vacías. No hay hilos en ejecución con $k > 0$ en colas locales. Se cumple trivialmente por vacuidad.
    - **Hipótesis Inductiva**: Antes del paso actual, la propiedad se cumple para todo procesador con $k$ hilos en su deque.
    - **Paso Inductivo ($t \to t+1$) por análisis de casos según la regla ejecutada**:
      1. **Regla 1 (Spawn)**:
         - $\Gamma_0$ engendra a $\Gamma_{hijo}$. $\Gamma_0$ entra al bottom ($\Gamma'_1 = \Gamma_0$) y el nuevo hilo en ejecución es $\Gamma'_0 = \Gamma_{hijo}$. Los hilos previos se desplazan: $\Gamma'_j = \Gamma_{j-1}$ para $j = 2, \dots, k+1$.
         - *Propiedad 1*: $\Gamma'_1$ es padre directo de $\Gamma'_0$ por la semántica del spawn. Para $j \ge 2$, $\Gamma'_j$ es padre de $\Gamma'_{j-1}$ por hipótesis inductiva previa.
         - *Propiedad 2*: Para $j=1$, $\Gamma'_1$ no ha sido procesado tras crear a $\Gamma'_0$ porque el spawn acaba de ocurrir en este instante exacto. Para $j \ge 2$, se preserva de la hipótesis inductiva previa.
      2. **Reglas 2 (Stall) y 3 (Die)**:
         - Si $k = 0$: La deque estaba vacía; el procesador pasa a robar. Al robar una tarea, la ejecuta de inmediato como único hilo activo sin elementos en deque ($k'=0$), cumpliéndose trivialmente.
         - Si $k > 0$: El procesador extrae $\Gamma_1$ del *bottom* como nuevo hilo activo ($\Gamma'_0 = \Gamma_1$), reduciendo la deque a $k' = k-1$.
         - *Propiedad 1*: El nuevo $\Gamma'_1$ (antiguo $\Gamma_2$) es padre del nuevo $\Gamma'_0$ (antiguo $\Gamma_1$), y los ancestros superiores preservan su relación.
         - *Propiedad 2*: El nuevo rango $i \in [1, k'-1]$ corresponde al rango $[2, k-1]$ previo, el cual no fue alterado y ya satisfacía la hipótesis intacta.
      3. **Regla 4 (Enable)**:
         - En una computación completamente estricta, los arcos de unión van **únicamente al padre directo**. Por tanto, $\Gamma_0$ solo puede habilitar a su propio padre.
         - *Condición ineludible*: La deque forzosamente debe estar vacía ($k = 0$). Si fuera $k > 0$, por la Propiedad 1 el padre sería $\Gamma_1$ en el *bottom* de su propia deque en estado `ready`, lo que contradice que estuviera postergado (*stalled*).
         - Al habilitar al padre, este entra al *bottom* ($\Gamma'_1 = \text{padre}$), con lo que $k' = 1$.
         - *Propiedad 1*: $\Gamma'_1$ es el padre de $\Gamma'_0$.
         - *Propiedad 2*: No impone condiciones para $k'=1$.
      4. **Robo por un procesador ladrón**:
         - Un procesador ocioso roba del *top* el hilo $\Gamma_k$.
         - En la víctima, la deque se acorta a $k' = k-1$. Los hilos $\Gamma_1 \dots \Gamma_{k-1}$ conservan intactas sus posiciones y relaciones genealógicas.
      - **Conclusión de la inducción**: Ambas propiedades se mantienen invariantes en todo paso $t$. $\blacksquare$
  - **Consecuencia Crítica (Teorema 5 - Cota de Espacio)**:
    - Como todos los hilos en cualquier *ready deque* son ancestros directos del hilo en ejecución $\Gamma_0$, todos ellos tienen descendientes vivos en el cómputo.
    - Por lo tanto, **ningún hilo en ninguna ready deque es una hoja**.
    - Esto demuestra que **todas las hojas vivas del cómputo están forzosamente en ejecución en los procesadores** (se satisface la propiedad de *Busy-Leaves*).
    - Por el Lema 2, cualquier algoritmo con *Busy-Leaves* garantiza una cota de espacio de memoria de:
      $$S \le S_1 \cdot P$$
      *(donde $S_1$ es la profundidad de pila de la ejecución serial y $P$ el número de procesadores)*.


---

### 18. Paralelismo Ideal

- **Referencia**: 04.Paralelismo_a_nivel_de_Tarea_2026.pdf
- **Respuesta**:
  - **Definición Formal**:
    $$\text{Paralelismo Ideal} = \frac{WORK(G)}{SPAN(G)} = \frac{T_1}{T_\infty}$$
  - **Significado Físico y Matemático**:
    - Representa el **límite superior teórico absoluto** del factor de aceleración (*speedup*) para un cómputo multihilo:
      $$S_p \le \frac{WORK(G)}{SPAN(G)}$$
    - Expresa el **número promedio de procesadores** que el algoritmo es capaz de mantener continuamente ocupados de forma productiva si se contara con infinitos recursos de hardware ($P = \infty$).
    - Es una métrica intrínseca del **grafo computacional del algoritmo**; no depende del procesador físico, del sistema operativo ni de la arquitectura de la máquina.
  - **Relación con la Holgura (*Slackness*)**:
    $$\text{Slackness} = \frac{\text{Paralelismo Ideal}}{p} = \frac{T_1}{p \cdot T_\infty}$$
    - Si $\text{Slackness} < 1$, el paralelismo inherente al problema es insuficiente para saturar $p$ procesadores, por lo que es **imposible** alcanzar speedup lineal sobre esa cantidad de núcleos.
    - Si $\text{Slackness} \gg 1$, existe suficiente paralelismo disponible para amortizar costos de planificación y alcanzar un speedup casi lineal.

---

### 19. Inicio y Terminación de Tareas: Caso de Estudio del Procedimiento de la Cena

- **Referencia**: 04.Paralelismo_a_nivel_de_Tarea_2026.pdf
- **Respuesta**:
  - **Mecanismos de Inicio y Terminación de Tareas**:
    - **Inicio de Tarea (`async` / `fork` / `spawn`)**: Dispara una instrucción o bloque de trabajo como un flujo de ejecución concurrente e independiente. El hilo invocador no se detiene; continúa inmediatamente con la siguiente sentencia.
    - **Terminación y Sincronización de Tarea (`finish` / `join` / `sync`)**: Delimita un bloque de ámbito. El hilo de control no puede avanzar más allá del cierre del bloque `finish` hasta que **todas** las subtareas iniciadas concurrentemente dentro de dicho ámbito hayan culminado totalmente su ciclo de vida.
  - **Modelado en el Procedimiento de la Cena**:
    - **Actividades del Grafo**:
      - $S_0$: Diseñar menú ($5\text{ min}$)
      - $S_1$: Compra aperitivo, vino, medallones ($25\text{ min}$)
      - $S_2$: Compra puré, ensalada, postre ($20\text{ min}$)
      - $S_3$: Arreglar ingredientes ($10\text{ min}$)
      - $S_4$: Organizar cocina ($2\text{ min}$)
      - $S_5$: Preparar medallones ($40\text{ min}$)
      - $S_6$: Preparar ensalada ($5\text{ min}$)
      - $S_7$: Preparar puré ($10\text{ min}$)
      - $S_8$: Preparar crema de pollo ($15\text{ min}$)
      - $S_9$: Organizar comedor ($10\text{ min}$)
      - $S_{10}$: Servir la cena ($60\text{ min}$)
    - **Inicio de tareas concurrentes**:
      - Tras diseñar el menú ($S_0$), se **inician** dos tareas concurrentes para compras: $S_1$ y $S_2$.
      - Tras organizar la cocina ($S_4$), se **inician** tareas culinarias en paralelo: la cocción de medallones ($S_5$) corre concurrente a la cadena $S_6 \to S_7 \to S_8$.
    - **Terminación y barreras de sincronización**:
      - $S_3$ no puede **iniciar** hasta que **terminen** tanto $S_1$ como $S_2$ (sincronización `join` de compras).
      - $S_9$ no puede **iniciar** hasta que **terminen** todas las preparaciones culinarias ($S_5$, $S_6$, $S_7$, $S_8$).
  - **Pseudocódigo Estructurado con `async` / `finish`**:
    ```text
    S0
    finish {
        async { S1 }
        S2
    }
    S3
    S4
    finish {
        async { S5 }
        S6
        S7
        S8
    }
    S9
    S10
    ```
  - **Cálculo de Métricas en el Grafo de la Cena**:
    - **Trabajo Total ($WORK$)**: Suma de todas las actividades:
      $$WORK = 5 + 25 + 20 + 10 + 2 + 40 + 5 + 10 + 15 + 10 + 60 = 202\text{ min}$$
    - **Tramo Crítico ($SPAN$)**: Ruta más larga ($S_0 \to S_1 \to S_3 \to S_4 \to S_5 \to S_9 \to S_{10}$):
      $$SPAN = 5 + 25 + 10 + 2 + 40 + 10 + 60 = 152\text{ min}$$
    - **Paralelismo Ideal de la Cena**:
      $$\text{Paralelismo Ideal} = \frac{WORK}{SPAN} = \frac{202}{152} \approx 1.33$$
      *(Indica que, aun disponiendo de cocineros o procesadores ilimitados, el procedimiento de la cena no puede acelerarse más allá de $1.33\times$, pues el tiempo mínimo insuperable es de $152\text{ min}$)*.


---

### 20. Cota de Tiempo Esperado de Work-Stealing y Computaciones Estrictas

- **Referencia**: 06.Work-Stealing_2026_Parte1_de_5.pdf y 06.Work-Stealing_2026_Parte2_de_5.pdf
- **Respuesta**:
  - **1. Cota de Tiempo de Ejecución Esperado en Work-Stealing**:
    - Para cualquier computación multihilo con trabajo total $T_1$ y tramo crítico $T_\infty$, el algoritmo de Work-Stealing aleatorizado ejecutado sobre $P$ procesadores garantiza un tiempo de ejecución esperado acotado por:
      $$\text{E}[T_P] \le \frac{T_1}{P} + O(T_\infty)$$
    - **Interpretación del Teorema de Blumofe & Leiserson (1999)**:
      - El término $\frac{T_1}{P}$ representa el tiempo en el que los procesadores ejecutan trabajo útil (escalabilidad lineal).
      - El término $O(T_\infty)$ acota el tiempo total invertido por procesadores ociosos en intentos de robo (*work-stealing attempts*) y sincronización.
      - Si la holgura de paralelismo satisface $\frac{T_1}{T_\infty} = \Omega(P)$, el término $\frac{T_1}{P}$ domina asintóticamente sobre $O(T_\infty)$, logrando **speedup lineal esperado**.
  - **2. Definición Formal de Computación Multihilo Estricta**:
    - En una **computación multihilo estricta**, los **arcos de unión (*join edges*)** que salen de cualquier hilo van dirigidos exclusivamente a un **ancestro** de dicho hilo en el árbol de generación (*spawn tree*).
    - **Diferencia frente a Computación Completamente Estricta**:
      | Tipo de Computación | Destino de los Arcos de Unión (*Join*) |
      |:---|:---|
      | **Computación Estricta** | A **cualquier ancestro** en el árbol de generación. |
      | **Computación Completamente Estricta** | Exclusivamente al **hilo padre directo**. |
    - **Propiedad Fundamental de las Computaciones Estrictas**:
      - En toda computación estricta, un hilo hoja en el subárbol vivo **nunca se suspende (*stall*)**; únicamente pueden suspenderse los ancestros a la espera de datos generados por sus descendientes.
