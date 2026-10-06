---
name: apuntes
description: >-
  Procesa documentos academicos (PDFs, diapositivas, lecturas) y notas borrador del
  estudiante para generar y mantener apuntes en Markdown con formato de ficha tecnica
  y cheat sheet de alta densidad. Sintetiza conceptos esenciales, formulas, tablas
  comparativas y recursos visuales sin prosa ni relleno, manteniendo un indice navegable
  y filtrable por terminos clave en el archivo Curso.md en la raiz de cada materia.
---

# Skill: Apuntes Academicos (Fichas Tecnicas y Cheat Sheets)

Esta skill optimiza la toma, estructuracion y mantenimiento de apuntes para las materias dentro de `2026-2`.

Su proposito es transformar documentos fuente (PDFs, diapositivas, lecturas) y apuntes preliminares del estudiante en **fichas tecnicas de alta densidad informativa, estilo cheat sheet, sin relleno y optimizadas para consulta rapida** sin saturar la ventana de contexto.

---

## Principios Fundamentales

1. **Formato Ficha Tecnica / Cheat Sheet**:
   - Orientado a memoria de trabajo: el estudiante ya vio la clase y entiende el contexto. Solo necesita las palabras clave, definiciones formales, formulas y advertencias que disparen el recuerdo inmediato.
   - Prohibidos bloques de texto narrativo, introducciones academicas, justificaciones metodologicas y conclusiones vacias.
   - Usar frases telegraficas, viñetas directas, terminos tecnicos en **negrita**, fragmentos de codigo en linea (`` `termino` ``) y formulas matematicas en KaTeX (`$ ... $`).
   - **Prohibido agregar Tablas de Contenidos (TOC)** en los apuntes temáticos; consumen espacio vertical sin aportar valor en archivos condensados.

2. **Lectura Directa Multimodal**:
   - Usar **directamente `view_file`** sobre el archivo fuente (`.pdf`, `.png`, etc.).
   - Prohibido crear scripts en Python o volcados a texto plano (`pdftotext`, `pypdf`); el modelo analiza de forma nativa la maquetacion, formulas y graficos del documento original.

3. **Integracion Homogenea de Apuntes**:
   - Si el estudiante dejo notas o borradores previos en el archivo, la IA debe leerlos primero e integrarlos con el contenido del PDF en una estructura unica y cohesionada.
   - No crear secciones redundantes ni duplicar ideas; complementar y pulir respetando el foco y las prioridades de la clase.

4. **Estrategia Hibrida para Recursos Visuales**:
   - **Mermaid**: Utilizar bloques de codigo `mermaid` para diagramas de arquitectura, arboles de decision, maquinas de estado y flujos logicos (100% nativo, ligero y editable).
   - **Imagenes locales (`./img/`)**: Cuando un grafico numerico, region factible o esquema complejo del PDF sea indispensable y no pueda modelarse en Mermaid:
     - Guardar la imagen de soporte en `./img/` relativo al apunte.
     - Vincular con sintaxis Markdown: `![Descripcion puntual](./img/grafico.png)`.
     - Agregar debajo una unica viñeta telegrafica con la conclusion o regla practica que se deriva de la figura.

---

## Convencion de Estructura y Archivos

Cada materia mantiene una organizacion uniforme:

```text
<Nombre_Materia>/
├── Curso.md                  # Hub de la materia: politicas, notas e indice filtrable
├── Apuntes/                  # Fichas tecnicas tematicas
│   ├── Tema_01.md
│   └── img/                  # Imagenes o diagramas de apoyo
└── Documentos/               # PDFs, diapositivas y lecturas fuente
```

### 1. Hub de Materia (`Curso.md`)
Ubicado siempre en la **raiz de la materia**. Funciona como mapa operativo e indice tematico:
- **Cabecera minima**: Materia, docente, y enlace a los documentos fuente.
- **Evaluacion**: Porcentajes de corte, criterios de calificacion y fechas de parciales.
- **Indice de Apuntes con Etiquetas de Busqueda**:
  Lista de enlaces a cada apunte acompañada deun listado exhaustivo de **Terminos clave** en codigo en linea. Esto permite buscar con `Ctrl+F` o busqueda textual cualquier concepto sin tener que recordar en que clase se vio ni abrir cada archivo:
  ```markdown
  ## Apuntes del Curso
  - [04. Paralelismo a Nivel de Tarea](./Apuntes/04_Paralelismo_a_Nivel_de_Tarea.md): `work`, `span`, `speedup`, `costo`, `slackness`, `ley de amdahl`, `ley de gustafson-barsis`, `deadlock`, `data race`.
  ```

### 2. Ficha Tecnica Tematica (`Apuntes/Tema.md`)
Ubicado dentro de la subcarpeta `Apuntes/`:
- **Navegacion superior**: Enlace de retorno normalizado `[← Volver a Curso.md](../Curso.md)` y enlace al documento fuente.
- **Terminos Core**: Lista en linea de los terminos y formulas principales tratados en la ficha.
- **Definiciones y Reglas Operativas**: Puntos directos y telegraficos.
- **Tablas Comparativas / Sintesis**: Cuadros matriciales para contrastar variantes, algoritmos o propiedades.
- **Recursos Visuales**: Diagramas Mermaid o referencias de `./img/`.
- **Casos Trampa / Puntos de Parcial**: Advertencias criticas, preguntas tipicas de evaluacion y errores frecuentes.

---

## Procedimiento Paso a Paso para la IA

Cuando el usuario solicite tomar o complementar apuntes:

1. **Inspeccionar Insumos**:
   - Abrir el archivo destino si ya contiene notas previas del estudiante.
   - Leer el documento fuente (PDF/diapositivas) mediante `view_file`.
2. **Generar la Ficha Tecnica**:
   - Aplicar el formato condensado cheat sheet integrando el borrador del usuario con los puntos criticos del documento.
   - Omitir TOC y omitir prosa explicativa.
   - Modelar diagramas en Mermaid o guardar capturas en `./img/` segun corresponda.
   - Asegurar el enlace `[← Volver a Curso.md](../Curso.md)`.
3. **Actualizar el Indice en `Curso.md`**:
   - Agregar o actualizar la entrada del apunte en la seccion `## Apuntes del Curso` con su ruta relativa y el bloque con todas las palabras clave relevantes.

---

## Referencias y Plantillas

- [Plantilla y Ejemplo de Ficha Tecnica](./references/academic-examples.md): Estructura detallada de un apunte de alta densidad estilo cheat sheet.
- [Guia de Navegacion e Indexacion](./references/navigation-and-links.md): Reglas para el indexado por terminos clave y consistencia de rutas relativas.

---

## Checklist de Calidad

Antes de finalizar:
- [ ] ¿Se leyo el documento fuente directamente con `view_file` sin usar scripts?
- [ ] ¿Se omitio cualquier Tabla de Contenidos (TOC) y se elimino toda prosa innecesaria?
- [ ] ¿Las definiciones y formulas estan en estilo telegrafico y con terminos en negrita/KaTeX?
- [ ] ¿El apunte incluye el enlace de retorno `[← Volver a Curso.md](../Curso.md)`?
- [ ] ¿Se actualizo `Curso.md` en la raiz agregando la lista completa de terminos clave para busqueda instantanea?
