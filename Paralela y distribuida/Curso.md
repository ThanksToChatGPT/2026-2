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

