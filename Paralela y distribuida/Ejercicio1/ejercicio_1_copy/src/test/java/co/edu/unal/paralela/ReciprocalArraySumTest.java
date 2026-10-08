package co.edu.unal.paralela;

import java.util.Random;

import junit.framework.TestCase;

/**
 * Suite de pruebas unitarias y de rendimiento para la clase {@link ReciprocalArraySum}.
 *
 * Utiliza el framework JUnit 3 para validar dos aspectos críticos del programa paralelo:
 * 1. Corrección numérica: comprueba que el valor calculado concurrentemente
 *    coincida con la solución secuencial exacta dentro de una tolerancia de error (err < 1E-2).
 * 2. Desempeño y Escalabilidad (Speedup): mide el tiempo promedio secuencial (T_1)
 *    frente al tiempo paralelo (T_p) sobre múltiples repeticiones para calcular el Speedup:
 *    Speedup = T_1 / T_p, verificando que supere los umbrales mínimos teóricos esperados.
 */
public class ReciprocalArraySumTest extends TestCase {

    /**
     * Número de repeticiones para cada medición de tiempo secuencial y paralela.
     *
     * Permite:
     * - "Calentar" la Máquina Virtual de Java (calentamiento de la JIT / Just-In-Time compiler),
     *   asegurando que el código esté compilado a código máquina nativo y optimizado.
     * - Reducir el ruido generado por la planificación del Sistema Operativo, pausas de GC
     *   (Garbage Collector) y fluctuaciones de frecuencia de la CPU mediante el promedio aritmético.
     */
    final static private int REPEATS = 60;

    /**
     * Determina la cantidad de núcleos lógicos disponibles en el entorno de ejecución actual.
     *
     * @return El número de procesadores o hilos lógicos de hardware reportados por la JVM
     */
    private static int getNCores() {
        return Runtime.getRuntime().availableProcessors();
    }

    /**
     * Genera un arreglo sintético de números reales de tamaño N para las pruebas.
     * Utiliza una semilla fija (314) para asegurar que los datos generados sean deterministas
     * y reproducibles en cada ejecución del test suite.
     *
     * @param N Cantidad de elementos double a generar en el arreglo
     * @return Arreglo double de longitud N inicializado con valores en el rango [1, 99]
     */
    private double[] createArray(final int N) {
        final double[] input = new double[N];
        final Random rand = new Random(314);

        for (int i = 0; i < N; i++) {
            input[i] = rand.nextInt(100);
            // Evita ceros en el arreglo para prevenir indeterminaciones de división por cero (1.0 / 0.0)
            if (input[i] == 0.0) {
                i--;
            }
        }

        return input;
    }

    /**
     * Implementación secuencial de referencia independiente dentro de la suite de pruebas.
     * Actúa como un "oráculo" que provee el resultado canónico para comparar contra
     * las implementaciones paralelas, protegiendo las pruebas de alteraciones accidentales en el código fuente principal.
     *
     * @param input Arreglo de entrada para calcular secuencialmente la suma de los recíprocos
     * @return Suma exacta de los recíprocos de la entrada
     */
    private double seqArraySum(final double[] input) {
        double sum = 0;

        // Calcula la suma secuencial acumulando 1 / input[i]
        for (int i = 0; i < input.length; i++) {
            sum += 1 / input[i];
        }

        return sum;
    }

    /**
     * Función auxiliar (test harness) que orquesta la verificación funcional y la medición de desempeño.
     *
     * Flujo de trabajo:
     * 1. Fase de Validación Funcional:
     *    - Genera el arreglo sintético aleatorio con N elementos.
     *    - Obtiene la respuesta correcta ejecutando el método secuencial de referencia (oráculo).
     *    - Ejecuta la versión paralela correspondiente (2 tareas o numTasks tareas).
     *    - Comprueba que la diferencia absoluta sea estrictamente menor a la tolerancia permitida:
     *      |sum_paralela - sum_secuencial| < 0.01 (1E-2).
     *
     * 2. Fase de Medición de Desempeño (Benchmark):
     *    - Mide el tiempo total de ejecutar REPEATS veces la versión secuencial para obtener seqTime (T_1).
     *    - Mide el tiempo total de ejecutar REPEATS veces la versión paralela para obtener parTime (T_p).
     *    - Calcula y retorna el factor de aceleración: Speedup = seqTime / parTime.
     *
     * @param N Tamaño del arreglo utilizado para las pruebas
     * @param useManyTaskVersion true para evaluar parManyTaskArraySum, false para parArraySum (2 tareas)
     * @param ntasks Número de tareas concurrentes a ejecutar
     * @return El factor de mejora en rapidez alcanzado (Speedup = T_1 / T_p)
     */
    private double parTestHelper(final int N, final boolean useManyTaskVersion, final int ntasks) {
        // 1. Crea un arreglo de entrada sintético de forma determinista
        final double[] input = createArray(N);

        // 2. Calcula el resultado exacto mediante la versión secuencial
        final double correct = seqArraySum(input);

        // 3. Ejecuta la implementación paralela evaluada
        double sum;
        if (useManyTaskVersion) {
            sum = ReciprocalArraySum.parManyTaskArraySum(input, ntasks);
        } else {
            assert ntasks == 2;
            sum = ReciprocalArraySum.parArraySum(input);
        }

        // 4. Verificación de corrección numérica con tolerancia para errores de punto flotante
        final double err = Math.abs(sum - correct);
        final String errMsg = String.format("No concuerda el resultado para N = %d, valor esperado = %f, valor calculado = %f, error " +
                "absoluto = %f", N, correct, sum, err);
        assertTrue(errMsg, err < 1E-2);

        /*
         * 5. Fase de Benchmark:
         * Ejecuta múltiples repeticiones de la versión secuencial y paralela para amortizar
         * efectos transitorios de la JVM y obtener mediciones de tiempo estables y confiables.
         */
        final long seqStartTime = System.currentTimeMillis();
        for (int r = 0; r < REPEATS; r++) {
            seqArraySum(input);
        }
        final long seqEndTime = System.currentTimeMillis();

        final long parStartTime = System.currentTimeMillis();
        for (int r = 0; r < REPEATS; r++) {
            if (useManyTaskVersion) {
                ReciprocalArraySum.parManyTaskArraySum(input, ntasks);
            } else {
                assert ntasks == 2;
                ReciprocalArraySum.parArraySum(input);
            }
        }
        final long parEndTime = System.currentTimeMillis();

        // Tiempo promedio por ejecución (en milisegundos)
        final long seqTime = (seqEndTime - seqStartTime) / REPEATS;
        final long parTime = (parEndTime - parStartTime) / REPEATS;

        // Speedup = T_1 / T_p (aceleración respecto al tiempo secuencial)
        return (double)seqTime / (double)parTime;
    }

    /**
     * Prueba 1: Implementación de 2 tareas con 2 millones de elementos (N = 2,000,000).
     *
     * Valida que la versión simple de dos mitades logre un speedup mínimo de 1.5x
     * (con 2 núcleos el máximo teórico es 2.0x; se exige al menos 75% de eficiencia paralela).
     */
    public void testParSimpleTwoMillion() {
        final double minimalExpectedSpeedup = 1.5;
        final double speedup = parTestHelper(2_000_000, false, 2);
        final String errMsg = String.format("Se esperaba que la implementación de dos tareas en paralelo pudiera ejecutarse " +
                " %fx veces más rápido, pero solo alcanzo a mejorar la rapidez (speedup) %fx veces", minimalExpectedSpeedup, speedup);
        assertTrue(errMsg, speedup >= minimalExpectedSpeedup);
    }

    /**
     * Prueba 2: Implementación de 2 tareas con 200 millones de elementos (N = 200,000,000).
     *
     * Al procesar una carga de trabajo masiva, el costo de sobrecarga (overhead) de bifurcación
     * y sincronización se vuelve insignificante frente al tiempo de cómputo útil,
     * garantizando un speedup robusto >= 1.5x.
     */
    public void testParSimpleTwoHundredMillion() {
        final double speedup = parTestHelper(200_000_000, false, 2);
        final double minimalExpectedSpeedup = 1.5;
        final String errMsg = String.format("Se esperaba que la implementación de dos tareas en paralelo pudiera ejecutarse " +
                "%fx veces más rápido, pero solo alcanzo a mejorar la rapidez (speedup) %fx veces", minimalExpectedSpeedup, speedup);
        assertTrue(errMsg, speedup >= minimalExpectedSpeedup);
    }

    /**
     * Prueba 3: Implementación de múltiples tareas con 2 millones de elementos (N = 2,000,000).
     *
     * Utiliza un número de tareas igual al número de núcleos lógicos de la máquina (ncores).
     * Exige una aceleración mínima del 60% de la capacidad teórica de los núcleos (ncores * 0.6).
     */
    public void testParManyTaskTwoMillion() {
        final int ncores = getNCores();
        final double minimalExpectedSpeedup = (double)ncores * 0.6;
        final double speedup = parTestHelper(2_000_000, true, ncores);
        final String errMsg = String.format("Se esperaba que la implmentación de muchas tareas en paralelo pudiera ejecutarse " +
                "%fx veces más rápido, pero solo alcanzo a mejorar la rapidez (speedup) %fx veces", minimalExpectedSpeedup, speedup);
        assertTrue(errMsg, speedup >= minimalExpectedSpeedup);
    }

    /**
     * Prueba 4: Implementación de múltiples tareas con 200 millones de elementos (N = 200,000,000).
     *
     * Evalúa la escalabilidad en régimen de gran volumen de datos (Ley de Gustafson-Barsis).
     * Al amortizarse casi por completo la sobrecarga de gestión de hilos, se exige una
     * alta eficiencia paralela del 80% (ncores * 0.8).
     */
    public void testParManyTaskTwoHundredMillion() {
        final int ncores = getNCores();
        final double speedup = parTestHelper(200_000_000, true, ncores);
        final double minimalExpectedSpeedup = (double)ncores * 0.8;
        final String errMsg = String.format("Se esperaba que la implmentación de muchas tareas en paralelo pudiera ejecutarse " +
                " %fx veces más rápido, pero solo alcanzo a mejorar la rapidez (speedup) %fx veces", minimalExpectedSpeedup, speedup);
        assertTrue(errMsg, speedup >= minimalExpectedSpeedup);
    }
}
