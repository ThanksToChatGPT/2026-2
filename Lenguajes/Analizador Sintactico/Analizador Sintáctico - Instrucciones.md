Práctica 2  
Analizador Sintáctico \- Lenguaje Lua


Dado un programa en el lenguaje de programación Lua, su tarea consiste en realizar el **análisis sintáctico**. Para realizar la implementación se podrán utilizar únicamente los siguientes lenguajes de programación: **Python 3.9, C/C++** y **Java**.

# Entrada

La **entrada** consiste en el código fuente de un programa en **Lua**, el cual puede estar correcto sintácticamente o no. Su programa debe recibir por la **entrada estándar (consola)** el código fuente de un programa escrito en el lenguaje de programación **Lua**. La entrada dada **no contiene errores léxicos**. 

Para evaluar el analizador sintáctico de forma automática, su programa debe realizar el análisis sintáctico de la entrada dada y generar la salida adecuada de acuerdo con las especificaciones dadas. A continuación se muestra la manera correcta de generar las salidas correspondientes.

# Salida

Las salidas se deben generar por la **salida estándar (consola)**. Nos vamos a enfocar en los errores sintácticos generados. Note que en este punto no interesa si el programa tiene errores semánticos porque, por el momento, nos enfocaremos solamente en el análisis sintáctico.

En caso de que el programa esté bien formado de acuerdo a las reglas de la gramática del lenguaje Lua, se debe mostrar el mensaje: 

**El analisis sintactico ha finalizado exitosamente.**

Note que no se permiten tildes. 

En caso contrario, es decir, si se encontró algún error sintáctico, se debe abortar el análisis y reportar únicamente el primer error sintáctico detectado.

# Consideraciones gramaticales

Se deben considerar todas las construcciones sintácticas definidas en el [manual de referencia](https://www.lua.org/manual/5.5/) así como el [alcance definido](https://docs.google.com/document/d/1MuZYY6Oi02NocGbGnO1qeO8VmrbSyGNjGJci5FEIUBo/edit?tab=t.0) para las prácticas. 

A continuación se detallan algunos puntos importantes:

1. Vamos a suponer que en el archivo de entrada se le intenta asignar una cadena a una variable la siguiente secuencia de operaciones   
   por ejemplo: 		x \= "n"\+a-true\*(vari\[3\] % 70) 

   Dado que en el lenguaje Lua todos los tipos de variables son correctos; podemos decir que el ejemplo mostrado anteriormente refiere a un error dado que no se pueden operar esos tipos de datos entre sí (y aún desconociendo los tipos de variables **a** y el contenido del arreglo **vari**). Por ende, el ejemplo hace referencia a un error **semántico** dado que no se presentan errores de sintaxis al ser capaces de operar todos los tipos de datos si fueran almacenados en variables. Por ende, en estos casos en particular, podemos permitir en expresiones aritméticas y relacionales, todos los tipos de datos presentes en el lenguaje dado que pueden ser definidos como variables. De esta manera, le corresponderá al analizador semántico verificar si las operaciones presentes en la expresión se pueden realizar con los tipos de datos ahí presentes.  
     
   El analizador sintáctico tan solo se encarga de validar que el programa ingresado satisfaga las **reglas gramaticales** del lenguaje.  
     
2. Tenga en cuenta que en Lua es posible acceder a un índice de una tabla por medio de una operación aritmética mientras satisfaga el hecho de que el resultado sea un número entero (responsabilidad del analizador semántico), por lo que expresiones mostradas anteriormente son **válidas** sintácticamente para referir al índice de un arreglo. 

3. Aunque en Lua están presentes las funciones de salida y manejo de control ya implementadas (print, xpcall, pcall, error y warn); el compilador nos permite reutilizar sus respectivos nombres explícitos para la definición de variables, por ende, sintácticamente son tratados como **identificadores**.

4. En las operaciones a nivel de bits, solo se debe contemplar la operación entre dos términos, es decir, operaciones bitwise **binarias** únicamente.

5. Aunque en la mayoría de lenguajes de programación se considera el fin de línea para manejar reglas sintácticas (ej. Python), o en su defecto, la definición de un token que representa el fin de sentencias (ej “;” en C++ y Java). En nuestro caso, Lua es un lenguaje que no es sensible a saltos de línea ni terminación explícita de sentencias. Por ende, los siguientes códigos tendrían el mismo resultado en nuestro analizador sintáctico; y también son correctos semánticamente.  
   

| local a \= 4;  global b \= 5; | local a \= 4; global b=5;  |
| :---- | :---- |

# Errores sintácticos

En el caso de cualquier error sintáctico, se debe informar al programador usando el siguiente formato:

**\<*linea*:*col*\> Error sintactico: se encontro: \<*lexema del token encontrado\>*; se esperaba: \<*lista de simbolos/tokens esperados separados por comas\>*.**

Donde:

* ***linea*** y ***col*** son los números de línea y columna donde se detectó el error.  
* **\<*lexema del token encontrado\>*:** corresponde al lexema encontrado que no se esperaba encerrado entre comillas dobles (**OJO:** el lexema, no el token).  
* **\<*lista de simbolos/tokens esperados separados por comas\>*:** corresponde a lista de tokens esperados separados por comas y encerrados entre comillas dobles. Por ejemplo: "if", "else", "/", "-", "+", "^", "\*", …  
* El mensaje no debe contener tildes.

Nótese que debe manejar un lenguaje que sea fácilmente comprensible para el programador de lenguaje Lua. Los símbolos "**)**", "**,**"**,** "**:**" pueden haber tenido otros nombres internamente, por ejemplo: **tkn\_closing\_par**, **tkn\_comma**, **tkn\_colon**. No obstante, estos detalles no deberían ser conocidos por el programador de Lua. Es por ello que en la lista de símbolos/tokens:

* Para las palabras reservadas se muestra el **lexema** correspondiente, pues sabemos que el tipo de token y el lexema son iguales en ese caso. (Por ejemplo: **"print"**)  
* Para los identificadores se muestra **"id"**.  
* Para los tokens de tipo **tkn\_num** se muestra **"valor\_numerico"**.  
* Para los tokens de tipo **tkn\_str** se muestra **"cadena\_de\_caracteres"**.  
* Para los operadores y símbolos se muestra el operador o símbolo correspondiente (Por ejemplo, **"+"**, en reemplazo a **tkn\_plus**).  
* Si se esperaba el final del archivo, se muestra **"final de archivo"**.

**IMPORTANTE:** En casos como el anterior, cuando se debe imprimir una lista de varios símbolos/tokens esperados, éstos deben estar entre comillas dobles, separados por un espacio en blanco, **y el orden en que debe aparecer la lista está determinado por el orden lexicográfico ascendente de los mismos**, es decir, simplemente se debe ordenar el arreglo de strings. 

En caso que se encuentre el fin de archivo (el token “**EOF**”) de manera inesperada, el analizador debe mostrar el siguiente error:	

**\<*linea*:*col*\> Error sintactico: se encontro: “final de archivo”; se esperaba: \<*lista de simbolos/tokens esperados separados por comas\>*.**

# Ejemplos

Así debería reportarse un programa sin errores sintácticos:

| Entrada | Salida |
| :---- | :---- |
| \-- Definición de la función function saludar(texto)     print(texto) end  \-- Llamada a la función saludar("¡Hola, mundo\!")  | El analisis sintactico ha finalizado exitosamente. |

Y así los programas con errores sintácticos:

| Entrada | Salida |
| :---- | :---- |
| local 1; | \<1:7\> Error sintactico: se encontro: "1"; se esperaba: "error", "function", "id", "pcall", "print", "warn", "xpcall". |

| Entrada | Salida |
| :---- | :---- |
| print(45"this") | \<1:9\> Error sintactico: se encontro: "this"; se esperaba: "and", "or", "&", "\|", "\~", ")", ",", "..", "/", "==", "//", "\>=", "\>", "\<\<", "\<=", "\<", "-", "%", "\~=", "+", "^", "\>\>", "\*". |

Nótese que el token “)” podría estar en las siguientes líneas o posiciones (después del número 45), siempre y cuando sea el siguiente token leído. 

Veamos más ejemplos.

| Entrada | Salida |
| :---- | :---- |
| local entrada  if entrada \== nil then     print("Valor indefinido") else     print("Valor definido") end  | El analisis sintactico ha finalizado exitosamente. |

| Entrada | Salida |
| :---- | :---- |
| local i \= 0;  while (i \< 5) do     p \== \[i\];3     i \= i \+ 1; end | \<4:7\> Error sintactico: se encontro: "=="; se esperaba: "=", ":", ",", "\[", "(", ".". |

# **Nota:** Tenga en cuenta que tal y como se mencionó anteriormente, la salida del analizador sintáctico debe imprimirse en **una sola línea**, no confundirse con el cambio de formato y alteración de los ejemplos presentes en este enunciado.

# Recomendaciones

Es posible implementar el analizador sintáctico calculando los conjuntos de predicción e implementando el analizador “a mano”. Sin embargo, esto puede significar tener que escribir muchas líneas de código repetitivas, lo cual puede ser susceptible de errores.

Se recomienda lo siguiente:

1. **Nivel 1**. Hacer un programa que halle los conjuntos de predicción (siguientes y primeros) dada una gramática **LL(1)**. Esto evitará que pierda tiempo haciendo cosas muy repetitivas.  
     
2. **Nivel 2**. Hacer un programa que **genere automáticamente** el analizador dada la gramática, usando el paso anterior: esto le ahorrará también mucho trabajo tedioso, reemplazándolo por trabajo interesante. En este caso, deberá enviar todos los archivos de su proyecto (incluida la gramática) junto con la entrega del programa resultante. No olvide consultar la documentación de UNCode respecto al envío de múltiples archivos.