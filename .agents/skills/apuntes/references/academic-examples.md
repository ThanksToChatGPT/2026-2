# Ejemplo de Apunte Académico de Alta Densidad

A continuación se muestra un ejemplo real de cómo debe estructurarse un apunte dentro de una carpeta de `2026-2` (ej. `Paralela y distribuida`).

---

```markdown
# 📌 Framework Fork-Join y Concurrencia de Tareas

> **Materia**: Paralela y Distribuida | **Fuente**: [Capitulo2_Concurrencia.pdf](./Capitulo2_Concurrencia.pdf)  
> **Conceptos Core**: `ForkJoinPool` `RecursiveTask` `RecursiveAction` `Work-Stealing`  
> 🔗 [← Volver a Curso.md](./Curso.md)

---

## 📑 Tabla de Contenidos
- [1. Arquitectura del Modelo Fork-Join](#1-arquitectura-del-modelo-fork-join)
- [2. RecursiveAction vs. RecursiveTask](#2-recursiveaction-vs-recursivetask)
- [3. Algoritmo Work-Stealing](#3-algoritmo-work-stealing)
- [4. Preguntas Típicas de Sustentación](#4-preguntas-típicas-de-sustentación)

---

## 1. Arquitectura del Modelo Fork-Join

### Conceptos Clave & Definiciones
- **Fork**: Operación asíncrona que divide una tarea grande en subtareas independientes (`async`).
- **Join**: Barrera de sincronización que bloquea hasta que una subtarea finaliza y retorna su resultado.
- **Umbral Secuencial (Threshold)**: Tamaño mínimo de problema donde ya no conviene dividir sino ejecutar secuencialmente.

### Puntos y Métricas
- **Sobrecarga de paralelismo**: Crear demasiadas subtareas añade coste en memoria y scheduler.
  * 📊 **Regla empírica**: Cada tarea hoja debe realizar entre 10.000 y 100.000 operaciones básicas para amortizar el coste de fork.
  * ⚠️ **Peligro**: Si el umbral es muy bajo ($<100$), el tiempo de gestión supera al tiempo de cómputo.

---

## 2. RecursiveAction vs. RecursiveTask

| Característica | `RecursiveAction` | `RecursiveTask<V>` |
| :--- | :--- | :--- |
| **Retorno de valor** | `void` (no retorna nada). | Retorna objeto de tipo `V`. |
| **Método abstracto** | `protected void compute()` | `protected V compute()` |
| **Caso de uso típico** | Modificaciones in-place (ej. ordenamiento de arreglo). | Reducciones (ej. suma de elementos, búsqueda). |

---

## 3. Algoritmo Work-Stealing
- **Estructura base**: Cada hilo trabajador (*worker thread*) posee una cola de doble extremo (**Deque**).
- **Mecanismo de robo**:
  * El hilo dueño toma tareas de la **cabeza (LIFO)** -> maximiza localidad temporal y de caché.
  * Un hilo ocioso roba tareas de la **cola (FIFO)** de otro hilo ocupado -> minimiza contención de bloqueos.

---

## 4. Preguntas Típicas de Sustentación
- **¿Por qué `compute()` de la segunda subtarea se debe llamar directamente y no hacer `fork()` a ambas?**:
  * Hacer `subtask1.fork()` y luego `subtask2.compute()` reutiliza el hilo actual para la segunda tarea, ahorrando la sobrecarga de despachar un hilo extra del pool.
```
