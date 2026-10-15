# Pagina: https://arcesio.net/paralela/private_libros

# Notas
- Tareas y quices 30%
- Parcial 1 15%
- Parcial 2 15%
- Parcial 3 15%
- Sustentacion 5%*5

## Apuntes del Curso
- [02. Siete Modelos de Concurrencia - Paul Butcher](./Apuntes/02_Siete_Modelos_de_Concurrencia.md): `concurrencia`, `paralelismo`, `hilos y cerrojos`, `actores`, `csp`, `paralelismo de datos`, `gpgpu`, `arquitectura lambda`, `kappa`, `inmutabilidad`.
- [03. Patrones Paralelos - McCool et al.](./Apuntes/03_Patrones_Paralelos.md): `fork-join`, `barrier`, `map`, `stencil`, `reduction`, `scan`, `recurrence`, `scatter`, `gather`, `pipeline`, `nesting pattern`.
- [04. Paralelismo a Nivel de Tarea](./Apuntes/04_Paralelismo_a_Nivel_de_Tarea.md): `grafo computacional`, `work`, `span`, `speedup`, `costo`, `slackness`, `ley de amdahl`, `ley de gustafson-barsis`, `deadlock`, `condiciones de coffman`, `livelock`, `data race`.
- [05. Hilos y Cerrojos (Dia 1) - Paul Butcher](./Apuntes/05_Hilos_y_Cerrojos_Dia1.md): `hilos vs procesos`, `exclusion mutua`, `synchronized`, `jmm`, `reordenamiento`, `visibilidad`, `cena de los filosofos`, `metodos alienigenas`.
- [05. Hilos y Cerrojos (Dia 2) - Paul Butcher](./Apuntes/05_Hilos_y_Cerrojos_Dia2.md): `reentrantlock`, `lockinterruptibly`, `trylock`, `timeouts`, `livelock`, `hand-over-hand locking`, `lock coupling`, `condition variables`, `await`, `signal`, `atomicinteger`, `cas`, `spurious wakeup`, `fairness`, `reentrantreadwritelock`, `atomicintegerfieldupdater`.
- [06. Algoritmo de Work-Stealing (Parte 1 de 5)](./Apuntes/06_Work_Stealing_Parte1.md): `work stealing`, `work sharing`, `blumofe-leiserson`, `cormen clrs`, `mimd`, `activation frame`, `stack depth`, `expansion lineal del espacio`, `spawn tree`, `arcos de continuacion`, `arcos de creacion`, `arcos de juntura`, `hilos vivos`, `hilos postergados`, `hilos ready`, `complejidad asintotica`, `cota de tiempo esperado`, `cota de espacio`, `greedy scheduling`, `online algorithm`, `busy leaves`.
- [06. Algoritmo de Work-Stealing (Parte 2 de 5)](./Apuntes/06_Work_Stealing_Parte2.md): `programa vs computacion multihilo`, `determinismo`, `computacion estricta`, `computacion completamente estricta`, `work`, `span`, `trayecto critico`, `planificador codicioso`, `greedy scheduler`, `teorema 1 de greedy`, `speedup lineal`, `propiedad de hojas ocupadas`, `busy leaves`, `algoritmo online`, `pool global centralizado`, `reglas de transicion`, `spawns stalls dies`, `lema 2 cota de espacio`, `teorema 3 tiempo y espacio`, `induccion de hojas ocupadas`, `cuello de botella centralizado`.
- [06. Algoritmo de Work-Stealing (Parte 3 de 5)](./Apuntes/06_Work_Stealing_Parte3.md): `work stealing aleatorizado`, `ready deque`, `bottom`, `top`, `lifo vs fifo`, `thief`, `victim`, `reglas de ejecucion`, `spawn`, `stall`, `die`, `enable`, `computacion completamente estricta`, `lema 4`, `propiedad de ser hilo padre`, `hilo padre no procesado`, `deque edges`, `teorema 5 cota de espacio`, `preservacion de hojas ocupadas`, `expansion lineal del espacio`.

# Preguntas parcial 1:
Algo del video: https://www.youtube.com/watch?v=oV9rvDllKEg
¿Por que movilidad?
El código: Los programas viajan por internet para ejecutarse en tu equipo o se adaptan automáticamente si la conexión se pone lenta.
Los datos: La información nace lejos (como en sensores de un camión) y el sistema debe guardarla y sincronizarla en cuanto recupere la señal.
Los dispositivos: Aparatos como celulares o autos que a cada rato entran y salen de la red, cambian de Wi-Fi a datos, o se quedan sin batería de golpe.
Los usuarios: Tú puedes empezar a hacer algo en la computadora de tu casa y terminarlo en el celular mientras vas en el bus, y el sistema recuerda exactamente dónde te quedaste.
¿Por qué es necesaria la movilidad?
Porque el mundo ya no está atado a un escritorio. Diseñar pensando en movilidad es aceptar que el internet va a fallar, que la gente cambia de pantalla constantemente y que los aparatos se mueven, pero el servicio nunca debe interrumpirse.

Por que algunos autores no comparten esa clasificacion de disribucion a nivel de tareas?
Actores
Que_es_la_recursividad_2026.pdf: El autor del libro que opina del TCO?
Que es work, que es span, que es speedup
Tramo computacional(Diagramas, tiempos, forks)
Finish, async, paralelismo, pseudolenguaje
Condiciones de coofman?
Paul Butcher libro de carreteras y carros (2.0 Siete modelos de concurrencia)
Ley de ahmdal
Sobrecarga, lo amarillo es el trabajo adicional para iniciar y sincronizar tareas
Que es online?: antes del paso t, el algoritmo ha computado y ejecutado los pasos hasta t-1, y solo usa esa informacion, no usa nada del futuro
Reglas de hojas ocupadas:
1. Spawns: si el hilo a genera a b, el procesador regresa "a" a la pool y agarra b en el siguiente paso
2. Stalls: Si a se posterga o suspende, el procesador retorna a al pool e inicia el siguiente paso ocioso
3. Dies: Si b muere, el prosesador revisa si el padre a tiene algun otro hijo vivo. Si no hay hermanos y ningun procesador tiene a a, sigue con a. En otro caso, el siguiente paso oscioso 

Reglas de Work-Stealing (Ready Deques distribuidas):
1. Spawns: Si a genera a b, el padre a va al bottom de la ready deque local; el procesador ejecuta b.
2. Stalls: Si a se posterga, saca del bottom de la deque local; si está vacía, pasa a ladrón (thief) y roba del top de una víctima al azar.
3. Dies: Igual que la regla 2 (Stalls).
4. Enable: Si a habilita un hilo postergado b (que en computación completamente estricta es su padre), b se coloca en el bottom de la deque local (solo ocurre con deque vacía, k=0).
* Si un hilo habilita y se posterga/muere en el mismo paso: primero se aplica Enable (Regla 4) y luego Stall/Die (Regla 2 o 3).
Lema 4: En la ready deque de un procesador, Γ1 (bottom) a Γk (top) son ancestros de Γ0 (en ejecución); cada Γi es padre de Γi-1 y ninguno (salvo posiblemente Γk) ha sido procesado tras crearlo.
Teorema 5: Ninguna hoja viva reside en una ready deque (todas tienen procesador asignado), preservando Busy-Leaves y garantizando espacio S <= S1 * P.



# Primera sustentacion: Fork Join
Sin comentarios en el codigo
PRIMERA SUSTENTACION: FORK JOIN
Que hace el codigo
Como se esta ejecutando el codigo, que se usa para editar y compilar
Como compilar como ejecutar
SUSTENTACION: Que enfoque de paralelismo
Que es maven
Que significa POM

Speedup <= work/span
No cumplio con el speedup esperado
Que es recursive action, cual es la diferencia con con el hermano (uno retorna, el otro no)
Que es override
Donde esta compute originalmente: recursive action
Que es reciprocalarraysumtask
SABER QUE HACE CADA METODO Y CADA OBJETO
Donde se construyen los datos de prueba del ejercicio
Mostrar como el helper hace el calculo del speedup y comparar con la teoria

Recursive Action javadoc
Hermana de recursive action = RecursiveTask, RecursiveTask retorna algo



# Segunda sustentacion:
Paralelismo funcional

