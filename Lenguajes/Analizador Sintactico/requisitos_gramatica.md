Actúa como un experto en teoría de lenguajes de programación, compiladores y diseño de gramáticas libres de contexto para analizadores sintácticos LL(1).

Tu tarea es diseñar y entregar la gramática libre de contexto completa, formal, sin ambigüedades y adaptada estrictamente para análisis sintáctico LL(1) (sin recursión por la izquierda y factorizada por la izquierda) para el lenguaje de programación Lua 5.5, cumpliendo rigurosamente con los requisitos del manual de referencia, el analizador léxico provisto y las decisiones de diseño validadas en la batería de pruebas.

---

### 1. FORMATO OBLIGATORIO DE LA GRAMÁTICA

La gramática debe escribirse estrictamente siguiendo este formato estándar de producciones:

```text
CHUNK ::= BLOCK

BLOCK ::= STAT_LIST

STAT_LIST ::= STAT STAT_LIST
           | epsilon

```

Reglas de formato:

1. El símbolo de producción debe ser exactamente `::=`.
2. Las alternativas de una producción deben alinearse con `|`.
3. La cadena vacía debe escribirse únicamente como la palabra en minúsculas: `epsilon`.
4. Todos los símbolos no terminales deben escribirse en MAYÚSCULAS y separados con guiones bajos si es necesario (ej. `STAT`, `EXP`, `VAR_TAIL`, `PRIMARY_EXP`, etc.).
5. Los símbolos terminales deben usar exactamente los nombres de tokens del analizador léxico detallados a continuación.
6. La gramática debe comenzar obligatoriamente con el axioma `CHUNK ::= BLOCK`.

---

### 2. TERMINALES Y TOKENS DEL ANALIZADOR LÉXICO

El analizador sintáctico recibe los tokens emitidos por el analizador léxico. Los nombres de terminales en las producciones deben coincidir exactamente con esta convención:

* **Literales:**
* `valor_numerico` (números enteros y flotantes)
* `cadena_de_caracteres` (literales de texto)
* `nil`
* `true`
* `false`


* **Identificadores y funciones nativas reutilizables:**
* En Lua, los identificadores pueden ser nombres de usuario o nombres de funciones estándar de salida y control (`print`, `xpcall`, `pcall`, `error`, `warn`), las cuales el analizador léxico devuelve con su propio nombre reservado pero sintácticamente pueden utilizarse como variables o identificadores.
* Se debe definir un no terminal auxiliar para abarcar estos identificadores en cualquier posición donde se espere un nombre:
```text
ID_NAME ::= id
          | print
          | warn
          | pcall
          | xpcall
          | error

```




* **Operadores y caracteres de puntuación (prefijo `tkn_*`):**
* Asignación y delimitadores:
* `tkn_assign` (`=`)
* `tkn_semicolon` (`;`)
* `tkn_colon` (`:`)
* `tkn_comma` (`,`)
* `tkn_period` (`.`)
* `tkn_goto` (`::`)
* `tkn_opening_par` (`(`)
* `tkn_closing_par` (`)`)
* `tkn_opening_bra` (`[`)
* `tkn_closing_bra` (`]`)
* `tkn_opening_key` (`{`)
* `tkn_closing_key` (`}`)
* `tkn_varargs` (`...`)


* Aritméticos:
* `tkn_plus` (`+`)
* `tkn_minus` (`-`)
* `tkn_times` (`*`)
* `tkn_div` (`/`)
* `tkn_floor_div` (`//`)
* `tkn_mod` (`%`)
* `tkn_power` (`^`)


* Relacionales y comparación:
* `tkn_equal` (`==`)
* `tkn_neq` (`~=`)
* `tkn_less` (`<`)
* `tkn_greater` (`>`)
* `tkn_leq` (`<=`)
* `tkn_geq` (`>=`)


* Concatenación:
* `tkn_concat` (`..`)


* Operaciones a nivel de bits (solo binarias y unario `~`):
* `tkn_bit_and` (`&`)
* `tkn_bit_or` (`|`)
* `tkn_bitex_or` (`~`)
* `tkn_left_shift` (`<<`)
* `tkn_right_shift` (`>>`)


* Longitud:
* `tkn_length` (`#`)




* **Palabras reservadas (terminales en minúsculas):**
* `and`, `break`, `do`, `else`, `elseif`, `end`, `for`, `function`, `global`, `goto`, `if`, `in`, `local`, `not`, `or`, `repeat`, `return`, `then`, `until`, `while`.



---

### 3. REGLAS, REQUISITOS Y RESTRICCIONES CRÍTICAS DE DISEÑO

La fuente de verdad principal es el Manual de Referencia de Lua 5.5, pero la gramática debe incorporar las siguientes decisiones arquitectónicas obligatorias deducidas de la suite de pruebas del evaluador sintáctico:

1. **Exclusividad del token `do` (Test 4):**
* Se omite completamente la estructura `stat ::= do block end`.
* El token `do` queda reservado **única y exclusivamente** para las estructuras de control de ciclos (`while ... do ... end` y `for ... do ... end`).
* El token `do` **NO** inicia una sentencia independiente. Por esta razón, `do` **NO** debe pertenecer a `First(STAT)` ni a los tokens esperados de inicio de sentencia.
* En una función vacía o al inicio de sentencia (Test 04), los tokens esperados son exactamente:
`"break", "end", "error", "for", "function", "global", "goto", "id", "if", "local", "pcall", "print", "repeat", "return", "::", ";", "warn", "while", "xpcall"`.


2. **Restricción de `function` en ciclos `for` (Test 13):**
* En las expresiones numéricas de la cabecera del ciclo `for` (`for ID_NAME = exp , exp [, exp] do`), se omite la posibilidad de definir funciones anónimas (`function funcbody`).
* La gramática debe tener una regla especializada de expresión para los ciclos `for` (`EXP_FOR` o similar) donde el First de la expresión numérica tras el `=` contenga literales, identificadores, llamadas, paréntesis y operadores unarios, pero **NO** contenga el terminal `function`.
* Tras el `=` de un `for`, los tokens esperados ante un error de inicio de expresión (Test 13) deben ser:
`"cadena_de_caracteres", "error", "false", "id", "nil", "not", "pcall", "print", "#", "-", "{", "(", "true", "valor_numerico", "warn", "xpcall"`.
* En expresiones de asignación general o retorno (`x = )`), la expresión regular sí admite `function` (Campuswire 2).


3. **Unificación de declaraciones `local` y `global` (Test 23):**
* Las declaraciones iniciadas con `local` y `global` comparten exactamente la misma estructura sintáctica y el mismo conjunto de continuación sintáctica al unificarse.
* No se incluyen declaraciones implícitas como `global *` ni atributos `<const>` en declaraciones colectivas.
* Después de `local` o `global`, solo se permite:
1. Una función local/global: `function ID_NAME funcbody`
2. Una lista de nombres de variables con inicialización opcional: `attnamelist ['=' explist]`


* Por tanto, tras `local` o `global` (Test 23 y Ejemplo 2), ante un token inválido (como un número), los tokens esperados son exactamente:
`"error", "function", "id", "pcall", "print", "warn", "xpcall"`.


4. **Factorización LL(1) de Sentencias: Variables vs Llamadas a Función (Test 18):**
* En Lua, tanto la asignación (`varlist = explist`) como la llamada a función (`functioncall`) inician con una expresión primaria (`ID_NAME` o parentizada).
* Para evitar conflictos de prefijo común y recursión izquierda, la gramática debe factorizar la sentencia que inicia con una expresión primaria (`PRIMARY_STAT` o similar) de tal modo que se consuman los accesos a campos (`.ID_NAME`), índices (`[exp]`), llamadas (`(...)`, `tableconstructor`, `cadena_de_caracteres`) y métodos (`:ID_NAME(...)`), bifurcándose luego limpiamente en:
* Asignación: lista restante de variables `[, varlist] = explist`.
* Sentencia de llamada a función ya consumida.


* Nótese que tras evaluar una variable simple al inicio de sentencia (Test 18: `p == [i]`), los tokens esperados de continuación de sentencia deben ser:
`"=", ":", ",", "[", "(", "."`.


5. **Lista de Parámetros en Funciones (Campuswire 4):**
* En la cabecera de parámetros de una función `( [parlist] )`, si hay una coma tras un parámetro (`function f(a,)`), no es opcional: obligatoriamente debe continuar un identificador (`ID_NAME`) o los puntos suspensivos (`tkn_varargs` / `...`).


6. **Sentencias de Control de Flujo:**
* `if EXP then BLOCK ELSEIF_LIST ELSE_OPT end`
* `while EXP do BLOCK end`
* `repeat BLOCK until EXP`
* `for ID_NAME FOR_TAIL` (distinguiendo `FOR_NUMERIC` con `EXP_FOR` de `FOR_GENERIC` con `in EXP_LIST`)
* `goto ID_NAME`
* `LABEL ::= tkn_goto ID_NAME tkn_goto`
* `break`
* `return [EXPLIST] [tkn_semicolon]` (debe ser válido al final de un bloque o en sentencias)
* Sentencia vacía: `tkn_semicolon` (`;`)


7. **Jerarquía Estricta de Precedencia y Asociatividad de Expresiones (LL(1)):**
La expresión general debe descomponerse en niveles para garantizar ausencia de recursión izquierda:
1. `or`
2. `and`
3. Relacionales: `<`, `>`, `<=`, `>=`, `~=`, `==`
4. Bitwise OR: `|`
5. Bitwise XOR binario: `~`
6. Bitwise AND: `&`
7. Shifts: `<<`, `>>`
8. Concatenación: `..` (asociativo a derecha)
9. Aditivos: `+`, `-`
10. Multiplicativos: `*`, `/`, `//`, `%`
11. Unarios prefijos: `not`, `tkn_length` (`#`), `tkn_minus` (`-`), `tkn_bitex_or` (`~`)
12. Potencia: `^` (asociativo a derecha)
13. Expresiones atómicas / primarias (literales, tablas `{ [fieldlist] }`, closures `function funcbody`, variables y llamadas).

.


---

### 4. ENTREGABLE ESPERADO

Genera de manera exhaustiva, estructurada y completa la gramática libre de contexto, sin omitir ninguna producción, comenzando directamente con el bloque de producciones en formato de texto plano según las especificaciones anteriores.