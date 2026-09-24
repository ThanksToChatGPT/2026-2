# Guía de Enlaces y Navegación para Apuntes en Markdown

El objetivo es que los apuntes dentro de `2026-2` no queden aislados, sino que formen una red de fácil navegación con un solo clic.

---

## 1. Tabla de Contenidos (TOC) Interna con Anclas

Para que el usuario pueda saltar directamente a una sección:
- Los encabezados Markdown generan anclas automáticas en minúsculas, reemplazando espacios por guiones y eliminando caracteres especiales.
- Ejemplo:
  ```markdown
  ## 1. Conceptos Fundamentales
  ...
  ## 2. Algoritmo RSA y Complejidad
  ```
  En la TOC:
  ```markdown
  - [1. Conceptos Fundamentales](#1-conceptos-fundamentales)
  - [2. Algoritmo RSA y Complejidad](#2-algoritmo-rsa-y-complejidad)
  ```

---

## 2. Enlaces Cruzados con `Curso.md`

Cada materia tiene un archivo central `Curso.md`.

### Al crear un apunte nuevo:
1. En la cabecera del nuevo apunte:
   ```markdown
   🔗 [← Volver al Índice de la Materia](./Curso.md)
   ```
2. En `Curso.md`:
   Añade el enlace al nuevo archivo en la sección correspondiente:
   ```markdown
   ### Apuntes y Temas
   - [📌 Fork-Join y RecursiveAction](./ForkJoin.md) - Modelos de concurrencia y tareas paralelas.
   ```

---

## 3. Enlaces Relativos a Documentos Fuente (PDFs)

Si el apunte proviene de un archivo en la misma carpeta o subcarpeta:
```markdown
> 📄 **Documento fuente**: [Que_es_la_recursividad_2026.pdf](./Que_es_la_recursividad_2026.pdf)
```
Si el documento está en una subcarpeta:
```markdown
> 📄 **Documento fuente**: [Lectura1.pdf](./Lecturas/Lectura1.pdf)
```
Esto permite al usuario abrir el archivo original directamente desde su editor de Markdown.
