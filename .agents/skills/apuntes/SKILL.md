---
name: apuntes
description: >-
  Toma de apuntes estructurados, concisos y de alta densidad en Markdown para las carpetas
  y asignaturas dentro de 2026-2 a partir de documentos (especialmente PDFs, lecturas,
  presentaciones y libros). Sintetiza ideas puntuales con palabras clave en negrita, enlaces
  de navegación y tablas comparativas, sin redactar párrafos completos, sin relleno y manteniendo
  la máxima utilidad práctica para el estudiante.
---

# Skill: Apuntes (Apuntes Académicos 2026-2)

Esta skill está optimizada exclusivamente para las materias dentro de `2026-2` (Criptografía, Paralela y Distribuida, Teoría de la Información, Ingesoft 2, Computación Visual, Optimización, Lenguajes, SisInfo, etc.).

Su propósito es procesar documentos fuente (PDFs, programas, diapositivas, lecturas) y generar **apuntes en Markdown de máxima escaneabilidad visual, sin relleno, directos a lo útil**.

---

## 🎯 Principios Centrales

1. **Cero Relleno / Cero Párrafos Innecesarios**:
   - Prohibido incluir textos institucionales, justificaciones metodológicas largas, listas bibliográficas extensas o introducciones vacías a menos que se pidan expresamente.
   - **NO añadir Tablas de Contenidos (TOC)** redundantes que solo consumen espacio vertical.
   - Usa exclusivamente **frases telegráficas**, **viñetas directas**, **tablas compactas** y **esquemas de relación (`->`)**.
2. **Lectura Directa de Documentos y PDFs (Cero Scripts de Extracción)**:
   - **Prohibido** usar scripts de Python, terminal o volcados a texto (`pypdf`, `pdftotext`, dumps planos) para procesar PDFs o lecturas.
   - Usa **directamente `view_file`** sobre el archivo `.pdf`. El modelo procesa de forma nativa y multimodal todo el contenido (texto, diagramas, fórmulas y maquetación) en una sola llamada.
3. **Utilidad Inmediata**:
   - Mantén foco en lo que el estudiante realmente necesita: **calificaciones/reglas de nota**, **fechas de entrega/parciales**, **fórmulas/algoritmos clave** y **enlaces rápidos**.
4. **Inserción de Imágenes para Máxima Claridad**:
   - Si un concepto, gráfica (ej. región factible, función objetivo), diagrama de red, árbol o esquema complejo se explica de forma más clara, rápida y directa con una imagen que con texto:
     - Guarda la imagen de soporte en una subcarpeta local de recursos (ej. `./img/` junto al apunte).
     - Usa `view_file` para verificar que la imagen sea legible y representativa.
     - Incrústala en el Markdown con enlace relativo: `![Descripción concisa](./img/grafico.png)`.
     - Añade únicamente una viñeta explicativa debajo con la conclusión o interpretación clave.
5. **Resaltado Visual Inmediato**:
   - Palabras clave, fechas, porcentajes y términos técnicos en **negrita** o código en línea (`` `término` ``).
   - Emojis sutiles y directos (`📌`, `📅`, `📊`, `⚠️`, `🔗`, `📝`, `🖼️`).

---

## 📂 Dos Estructuras de Archivo

### 1. Hub de Materia (`Curso.md`)
El archivo `Curso.md` en la raíz de cada materia es la **hoja de ruta operativa y el índice del curso**, no un volcado de syllabus.

Debe contener **únicamente**:
- **Encabezado mínimo**: Materia, profesor, horario/salón y enlace al programa fuente si existe.
- **📊 Evaluación / Notas**: Porcentajes de cada corte y reglas críticas de evaluación.
- **📅 Calendario de Fechas Clave**: Tabla compacta con parciales, quices, talleres, entregas de proyecto y festivos.
- **🔗 Apuntes & Notas de Clase**: Lista estructurada de enlaces hacia los apuntes del semestre a medida que se vayan creando:
  ```markdown
  ## 🔗 Apuntes del Curso
  - [Semana 01 - Tema](./Apuntes/Semana01_Tema.md): Concepto A, Concepto B.
  ```

> ⛔ **Prohibido en `Curso.md`**:
> - Tablas de contenidos (`## 📑 Tabla de Contenidos`).
> - Bloques narrativos sobre metodología pedagógica.
> - Listas kilométricas de bibliografía complementaria.
> - Descripciones temáticas extensas que pertenezcan a los apuntes individuales.

---

### 2. Apuntes Temáticos Específicos (`Tema.md`)
Úsalo al procesar clases, lecturas o diapositivas específicas:
- **Metadatos & Enlace de retorno**: `[← Volver a Curso.md](./Curso.md)`.
- **Conceptos y Fórmulas**: Definiciones directas, teoremas, pasos algorítmicos.
- **Tablas Comparativas / Resumen**: Diferencias y ventajas clave.
- **Recursos Gráficos**: Diagramas e imágenes de apoyo (`./img/`) cuando simplifiquen la comprensión visual del problema.
- **Puntos Críticos de Examen / Preguntas Típicas**.

---

## 🔍 Checklist de Calidad
Antes de guardar:
- [ ] ¿Se leyó el PDF directamente con `view_file` sin recurrir a scripts o dumps de texto?
- [ ] ¿Hay tablas de contenidos (TOC) innecesarias? -> *Eliminarlas.*
- [ ] En `Curso.md`, ¿hay contenido superfluo (metodología, bibliografía, etc.)? -> *Dejar únicamente notas, fechas y enlaces de apuntes.*
- [ ] ¿Están claras todas las fechas y porcentajes de evaluación? -> *Resaltar en negrita.*
- [ ] ¿Si hay un gráfico, región o diagrama esencial, se incluyó como imagen (`./img/`) con su explicación puntual?
- [ ] ¿Quedó habilitada la sección `🔗 Apuntes del Curso` para futuros links? -> *Asegurar lista expandible.*
