package co.edu.unal.paralela;

import java.util.concurrent.ForkJoinTask;
import java.util.concurrent.RecursiveAction;

/**
 * Clase que contiene los métodos para implementar la suma de los recíprocos
 * de un arreglo usando paralelismo basado en tareas (Framework Fork-Join de Java).
 *
 * El cálculo de recíprocos consiste en sumar (1 / X[i]) para cada elemento del arreglo.
 * Dado que cada iteración es computacionalmente independiente de las demás, este problema
 * es "embarazosamente paralelo" (embarrassingly parallel), lo que permite descomponer el
 * dominio de datos en múltiples subtareas concurrentes.
 */
public final class ReciprocalArraySum {

    /**
     * Constructor privado para prevenir la instanciación de esta clase de utilidades.
     */
    private ReciprocalArraySum() {
    }

    /**
     * Calcula secuencialmente la suma de los recíprocos de los elementos del arreglo.
     * Sirve como implementación de referencia (línea base secuencial T_1) para verificar
     * la exactitud del cálculo paralelo y medir el factor de aceleración (speedup).
     *
     * @param input Arreglo de entrada con números reales (ningún valor debe ser 0)
     * @return La suma de los recíprocos de todos los elementos del arreglo
     */
    protected static double seqArraySum(final double[] input) {
        double sum = 0;

        // Itera secuencialmente sobre cada elemento acumulando su recíproco (1 / input[i])
        for (int i = 0; i < input.length; i++) {
            sum += 1 / input[i];
        }

        return sum;
    }

    /**
     * Calcula el tamaño estándar de cada sección (chunk) dividiendo la cantidad
     * de elementos entre el número de tareas deseadas.
     * Utiliza la función techo entera: ceil(nElements / nChunks) = (nElements + nChunks - 1) / nChunks,
     * garantizando que los elementos se distribuyan equitativamente entre las tareas.
     *
     * @param nChunks El número de secciones (chunks) para crear
     * @param nElements El número de elementos para dividir
     * @return El tamaño por defecto de la sección (chunk)
     */
    private static int getChunkSize(final int nChunks, final int nElements) {
        // Función techo entera para evitar truncamiento hacia abajo
        return (nElements + nChunks - 1) / nChunks;
    }

    /**
     * Calcula el índice del elemento inclusivo donde la sección/trozo (chunk) inicia,
     * dado que hay cierto número de secciones/trozos (chunks).
     * Multiplica el identificador del chunk por el tamaño base del chunk.
     *
     * @param chunk La sección/trozo (chunk) para calcular la posición de inicio (0 a nChunks - 1)
     * @param nChunks Cantidad de secciones/trozos (chunks) creados
     * @param nElements La cantidad de elementos que deben atravesarse
     * @return El índice inclusivo donde esta sección/trozo (chunk) inicia en el conjunto de nElements
     */
    private static int getChunkStartInclusive(final int chunk,
            final int nChunks, final int nElements) {
        final int chunkSize = getChunkSize(nChunks, nElements);
        return chunk * chunkSize;
    }

    /**
     * Calcula el índice del elemento exclusivo que marca el final de la sección/trozo (chunk).
     * Toma el límite teórico (chunk + 1) * chunkSize y lo acota con nElements para
     * asegurar que la última sección no sobrepase la longitud del arreglo.
     *
     * @param chunk La sección para calcular donde termina (0 a nChunks - 1)
     * @param nChunks Cantidad de secciones/trozos (chunks) creados
     * @param nElements La cantidad de elementos que deben atravesarse
     * @return El índice de terminación exclusivo para esta sección/trozo (chunk)
     */
    private static int getChunkEndExclusive(final int chunk, final int nChunks,
            final int nElements) {
        final int chunkSize = getChunkSize(nChunks, nElements);
        final int end = (chunk + 1) * chunkSize;
        // Acota con nElements para evitar IndexOutOfBoundsException en el último fragmento
        if (end > nElements) {
            return nElements;
        } else {
            return end;
        }
    }

    /**
     * Subtarea Fork-Join que hereda de {@link RecursiveAction}.
     * Se encarga de procesar un rango contiguo del arreglo [startIndexInclusive, endIndexExclusive).
     *
     * Se utiliza {@link RecursiveAction} (en lugar de RecursiveTask) porque la tarea no retorna
     * un valor directamente a través de compute(); en su lugar, almacena el resultado acumulado
     * en el campo {@code value}, el cual se consulta posteriormente mediante {@link #getValue()}.
     */
    private static class ReciprocalArraySumTask extends RecursiveAction {
        /**
         * Índice inicial inclusivo para el recorrido y cálculo de esta tarea.
         */
        private final int startIndexInclusive;
        /**
         * Índice final exclusivo para el recorrido y cálculo de esta tarea.
         */
        private final int endIndexExclusive;
        /**
         * Referencia al arreglo original de entrada (compartido en modo de solo lectura).
         */
        private final double[] input;
        /**
         * Almacena el resultado parcial acumulado producido por esta tarea.
         */
        private double value;

        /**
         * Constructor que establece los límites del bloque y el arreglo de datos.
         *
         * @param setStartIndexInclusive Establece el índice inicial inclusivo para la tarea
         * @param setEndIndexExclusive Establece el índice final exclusivo para la tarea
         * @param setInput Valores de entrada sobre los cuales se calcula la suma
         */
        ReciprocalArraySumTask(final int setStartIndexInclusive,
                final int setEndIndexExclusive, final double[] setInput) {
            this.startIndexInclusive = setStartIndexInclusive;
            this.endIndexExclusive = setEndIndexExclusive;
            this.input = setInput;
        }

        /**
         * Adquiere el valor calculado por esta tarea una vez finalizada su ejecución.
         *
         * @return El valor acumulado de los recíprocos en el rango asignado
         */
        public double getValue() {
            return value;
        }

        /**
         * Método principal de cómputo ejecutado por el worker thread de Fork-Join.
         * Realiza la suma secuencial de los recíprocos en el subrango contiguo asignado.
         */
        @Override
        protected void compute() {
            double sum = 0;
            // Itera secuencialmente sobre el bloque contiguo asignado en memoria
            for (int i = startIndexInclusive; i < endIndexExclusive; i++) {
                sum += 1 / input[i];
            }
            // Guarda el resultado intermedio para ser recuperado tras la sincronización
            value = sum;
        }
    }

    /**
     * Calcula la suma de los recíprocos dividiendo el arreglo en dos mitades y ejecutándolas
     * en paralelo mediante dos subtareas Fork-Join.
     *
     * Implementa el patrón clásico de bifurcación y encuentro (Fork-Join / async-finish):
     * 1. Se asume que la longitud del arreglo es divisible por 2.
     * 2. Se divide el arreglo en dos partes: [0, mid) y [mid, length).
     * 3. Se crean dos subtareas: left (primera mitad) y right (segunda mitad).
     * 4. {@code ForkJoinTask.invokeAll(left, right)} bifurca una tarea en el pool común de Java
     *    mientras el hilo invocador ejecuta la otra, esperando al final la sincronización de ambas.
     * 5. Se combinan (reducen) los resultados parciales sumando los valores obtenidos.
     *
     * @param input Arreglo de entrada (su longitud debe ser par / divisible por 2)
     * @return La suma de los recíprocos del arreglo calculada concurrentemente
     */
    protected static double parArraySum(final double[] input) {
        assert input.length % 2 == 0;

        // Calcula el índice medio para la partición simétrica en dos mitades
        final int mid = input.length / 2;

        // Crea las dos subtareas asignando cada mitad del arreglo
        final ReciprocalArraySumTask left =
                new ReciprocalArraySumTask(0, mid, input);
        final ReciprocalArraySumTask right =
                new ReciprocalArraySumTask(mid, input.length, input);

        // Ejecuta concurrentemente ambas tareas en el ForkJoinPool.commonPool()
        ForkJoinTask.invokeAll(left, right);

        // Fase de reducción: suma los resultados parciales calculados por cada tarea
        return left.getValue() + right.getValue();
    }

    /**
     * Generaliza el cálculo paralelo para un número establecido de tareas (numTasks).
     *
     * Cada tarea procesa un bloque contiguo del arreglo (chunk) calculado mediante
     * {@link #getChunkStartInclusive} y {@link #getChunkEndExclusive}.
     *
     * Flujo de ejecución:
     * 1. Se calculan los rangos y se instancian las numTasks subtareas.
     * 2. Todas las tareas se despachan en paralelo usando {@code ForkJoinTask.invokeAll(tasks)}.
     * 3. Se acumulan (reducen) secuencialmente los resultados parciales de cada tarea.
     *
     * @param input Arreglo de entrada
     * @param numTasks El número de tareas para crear (usualmente igual a los núcleos de la CPU)
     * @return La suma total de los recíprocos del arreglo calculada en paralelo
     */
    protected static double parManyTaskArraySum(final double[] input,
            final int numTasks) {
        // Arreglo para almacenar las referencias a cada subtarea creada
        final ReciprocalArraySumTask[] tasks =
                new ReciprocalArraySumTask[numTasks];

        // Particiona el arreglo en numTasks bloques contiguos y asigna cada uno a una tarea
        for (int i = 0; i < numTasks; i++) {
            final int start = getChunkStartInclusive(i, numTasks, input.length);
            final int end = getChunkEndExclusive(i, numTasks, input.length);
            tasks[i] = new ReciprocalArraySumTask(start, end, input);
        }

        // Despacha concurrentemente todas las tareas y espera a que todas concluyan
        ForkJoinTask.invokeAll(tasks);

        // Fase de reducción: acumula los resultados parciales de todas las tareas
        double sum = 0;
        for (int i = 0; i < numTasks; i++) {
            sum += tasks[i].getValue();
        }

        return sum;
    }
}
