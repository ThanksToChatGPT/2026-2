# Práctica 2: Analizador Sintáctico de Lua

Implementación de un analizador sintáctico predictivo descendente recursivo (LL(1)) para el lenguaje de programación **Lua**, cumpliendo con todas las especificaciones y el alcance del taller.

---

## 📁 Estructura del Proyecto

```text
Analizador sintactico/
├── analizador_lexico.py       # Analizador léxico (tokenizador, posiciones de fila/columna)
├── analizador_sintactico.py   # Analizador sintáctico LL(1) con manejo de errores
├── main.py                    # Punto de entrada principal (lee de stdin, salida a stdout)
├── test_sintactico.py         # Script de ejecución y verificación de pruebas
├── gramatica.bnf              # Definición formal de la gramática LL(1)
└── tests/                     # Suite de pruebas (.in y .out)
```

---

## 🚀 Ejecución

### Ejecución directa desde consola (con entrada estándar)
```bash
python main.py < tests/01.in
```
o
```bash
python analizador_sintactico.py < tests/01.in
```

### Ejecutar todas las pruebas
```bash
python test_sintactico.py
```
---

## 📋 Salida y Especificación de Errores

### 1. Código Sintácticamente Correcto
Si el programa analizado no contiene errores sintácticos, se imprime en una sola línea:
```text
El analisis sintactico ha finalizado exitosamente.
```

### 2. Detección de Errores Sintácticos
En caso de detectar un error sintáctico, el análisis se aborta en el primer error y se imprime el mensaje en el formato exacto:
```text
<<fila>:<columna>> Error sintactico: se encontro: "<lexema>"; se esperaba: "<token1>", "<token2>", ...
```

Donde:
- `<fila>` y `<columna>` indican la posición exacta donde se detectó el error.
- `<lexema>` es el lexema encontrado (o `"final de archivo"` si es fin de archivo).
- La lista de símbolos/tokens esperados aparece **ordenada lexicográficamente** según el identificador de tipo interno del token.
- Las funciones del sistema (`print`, `warn`, `pcall`, `xpcall`, `error`) son tratadas sintácticamente como identificadores (`Name`).
- Operaciones a nivel de bits se manejan de forma estrictamente binaria (`~` solo binario).

---

## 🛠️ Detalles Gramaticales LL(1)

1. **Eliminación de Recursión Izquierda y Factorización:**
   - La distinción entre sentencias de asignación (`varlist = explist`) y llamadas de función (`functioncall`) se factoriza tras el consumo inicial de `Name`.
   - Tras leer `Name` a nivel de sentencia, se anticipa determinísticamente si sigue asignación (`=`, `,`), acceso indexado (`[`, `.`), o invocación de función (`(`, `:`).
2. **Expresiones Aritmético-Lógicas:**
   - Expresiones formuladas como `atom { binop atom }`, verificando en cada punto de corte que el siguiente token pertenezca al conjunto de operadores binarios o al conjunto `FOLLOW` del contexto sintáctico (delimitadores de argumentos, sentencias de control, etc.).
3. **Declaraciones Locales y Globales:**
   - Manejo unificado de `local` y `global`, soportando definición de funciones (`local/global function Name ...`) y declaración de variables con inicialización opcional (`local/global Name {',' Name} ['=' explist]`).

