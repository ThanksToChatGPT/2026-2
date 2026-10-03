# Guia de Navegacion, Enlaces e Indexacion

Esta guia define los estandares de conexion entre archivos dentro del entorno `2026-2` para garantizar navegacion fluida y recuperacion rapida de informacion sin saturar la ventana de contexto.

---

## 1. Indice Filtrable por Terminos Clave en `Curso.md`

El archivo `Curso.md` en la raiz de cada materia centraliza el indice operativo del curso. Para que cualquier concepto o termino sea localizable de inmediato mediante busqueda rapida (`Ctrl+F`) o comandos de busqueda textual sin tener que abrir cada archivo individual ni saturar el contexto del modelo, los enlaces deben seguir estrictamente este patron:

```markdown
## Apuntes del Curso

- [01. Introduccion a IO y PL](./Apuntes/01_Introduccion_IO_y_PL.md):  `investigacion de operaciones`, `programacion lineal`, `funcion objetivo`, `region factible`, `restricciones`, `variables de decision`.
- [02. Metodo Grafico](./Apuntes/02_Metodo_Grafico.md): `vertices extremos`, `lineas de nivel`, `solucion no acotada`, `infactibilidad`, `soluciones multiples`.
- [04. Paralelismo a Nivel de Tarea](./Apuntes/04_Paralelismo_a_Nivel_de_Tarea.md): `work`, `span`, `speedup`, `costo`, `slackness`, `ley de amdahl`, `ley de gustafson-barsis`, `deadlock`, `data race`.
```

### Reglas de indexacion:
- Cada apunte ocupa una unica viñeta en la seccion `## Apuntes del Curso`.
- La etiqueta `Terminos clave:` debe listar de forma exhaustiva los conceptos, teoremas, algoritmos y formulas principales tratados en la ficha, formateados en codigo en linea (`` `termino` ``).

---

## 2. Enlaces de Retorno en Fichas Tematicas (`Tema.md`)

Todo apunte ubicado dentro de la subcarpeta `Apuntes/` debe iniciar exactamente con la ruta de retorno al hub:

```markdown
[← Volver a Curso.md](../Curso.md)
```

Inmediatamente debajo se define la cabecera tecnica:
```markdown
# Titulo del Tema

> **Materia**: Nombre de la Materia | **Fuente**: [Documento.pdf](../Documentos/Documento.pdf)  
> **Terminos Core**: `TerminoA`, `TerminoB`, `TerminoC`
```

---

## 3. Enlaces Relativos a Documentos Fuente e Imagenes

1. **Documentos Fuente (PDFs / Lecturas)**:
   - Los documentos originales suelen residir en la carpeta `Documentos/` de la materia o en la raiz.
   - Enlace relativo desde un apunte en `Apuntes/`:
     ```markdown
     > **Fuente**: [Clase_03_Simplex.pdf](../Documentos/Clase_03_Simplex.pdf)
     ```
   - Si el archivo esta en la raiz de la materia:
     ```markdown
     > **Fuente**: [Programa_Curso.pdf](../Programa_Curso.pdf)
     ```

2. **Recursos Visuales Locales (`./img/`)**:
   - Las imagenes de apoyo se ubican en una carpeta `img/` dentro de `Apuntes/`:
     ```markdown
     ![Region factible acotada](./img/region_factible_ejemplo1.png)
     ```
   - Siempre acompañar la imagen de una viñeta concisa con la regla o interpretacion fundamental.

---

## 4. Prohibicion de Tablas de Contenidos Internas

- Las fichas tecnicas tematicas estan diseñadas como cheat sheets de lectura vertical rapida y alta densidad.
- **No incluir tablas de contenidos internas ni anclas (`#seccion`)** dentro de los archivos de apuntes; la organizacion debe ser directa mediante subtitulos tematicos limpios (`## Subtitulo`).
