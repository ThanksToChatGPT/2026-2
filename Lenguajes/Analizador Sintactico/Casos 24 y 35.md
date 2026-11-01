# Casos 24 y 35

El juez no acepta nada pegado después de una expresión entre paréntesis, como `.campo`, `[i]`, `:metodo()` o una llamada. Si tu parser lo acepta, fallan los casos 24 y 35; la solución es quitar esos sufijos de la gramática justo después del `)`.

## El problema

En el Lua real, `(a).b` es válido, y si armas la gramática desde el manual lo aceptas. El juez espera un error en ese punto.

| Entrada | Qué espera el juez |
| --- | --- |
| `x = (a).b` | error |
| `x = (t)[1]` | error |
| `x = (f)(1)` | error |
| `x = (a) + 1` | válido |
| `x = f(a).b` | válido |

La regla: después del `)` que cierra un paréntesis de agrupación solo puede venir `^`, un operador binario o el final de la expresión. Los paréntesis de una llamada, como `f(a)`, son otra cosa y sí admiten sufijos.

## Cómo saber si te pasa

Probar `x = (a).b`. Si tu parser lo acepta, o si en algún error la lista de "se esperaba" después de un `)` incluye `.`, `[`, `:`, `(` o `{`, es este problema.

Con la gramática correcta, la salida que espera el juez para `x = (a).b` empieza así:

```
<1:8> Error sintactico: se encontro: "."; se esperaba: "and", ...
```

Es decir, error en la línea 1, columna 8, justo en el `.`, y la lista de "se esperaba" ya no trae sufijos.

## Cómo arreglarlo

1. Busca en tu gramática todas las reglas con una expresión entre paréntesis de agrupación.
2. Quita los sufijos que van justo después del `)`. Deja `^` y los operadores binarios.
3. No toques las reglas de nombres ni de llamadas: ahí los sufijos sí van.
4. Vuelve a generar la tabla y repite las pruebas de arriba.

Lo más común es olvidar una copia: si la expresión aparece en más de un lugar (a nosotros nos pasó con los campos de las tablas), hay que cambiarla en todos.

No tenemos el contenido exacto de los tests 24 y 35, pero fallaban antes de este cambio y pasaron después, sin tocar nada más.
