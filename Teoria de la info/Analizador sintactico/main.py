"""
Programa principal para el analizador sintáctico de Lua.
Lee el código fuente desde la entrada estándar (consola) y
reporta si el análisis sintáctico fue exitoso o el primer error sintáctico.
"""

import sys
from analizador_lexico import tokenizador
from analizador_sintactico import AnalizadorSintactico, ErrorSintactico


def main():
    codigo = sys.stdin.read()
    tokens = tokenizador(codigo)
    parser = AnalizadorSintactico(tokens)
    try:
        parser.analizar()
        print("El analisis sintactico ha finalizado exitosamente.")
    except ErrorSintactico as e:
        print(e)
        sys.exit(0)


if __name__ == "__main__":
    main()

