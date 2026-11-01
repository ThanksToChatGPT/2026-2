"""
Módulo principal: main.py
Punto de entrada para el analizador sintáctico de Lua 5.5.
"""

import os
import sys
from analizador_lexico import tokenizador
from analizador_sintactico import AnalizadorSintactico, parsear_gramatica
from conjuntos_de_prediccion import calcular_primeros, conjuntos_de_prediccion

# Mapa de símbolos para la presentación amigable de errores al usuario
MAPA_SIMBOLOS = {
    "id": "id",
    "final_de_archivo": "final de archivo",
    "tkn_semicolon": ";",
    "tkn_colon": ":",
    "tkn_comma": ",",
    "tkn_period": ".",
    "tkn_assign": "=",
    "tkn_opening_par": "(",
    "tkn_closing_par": ")",
    "tkn_opening_bra": "[",
    "tkn_closing_bra": "]",
    "tkn_opening_key": "{",
    "tkn_closing_key": "}",
    "tkn_plus": "+",
    "tkn_minus": "-",
    "tkn_times": "*",
    "tkn_div": "/",
    "tkn_floor_div": "//",
    "tkn_power": "^",
    "tkn_mod": "%",
    "tkn_equal": "==",
    "tkn_neq": "~=",
    "tkn_less": "<",
    "tkn_leq": "<=",
    "tkn_greater": ">",
    "tkn_geq": ">=",
    "tkn_bit_and": "&",
    "tkn_bit_or": "|",
    "tkn_bitex_or": "~",
    "tkn_left_shift": "<<",
    "tkn_right_shift": ">>",
    "tkn_concat": "..",
    "tkn_varargs": "...",
    "tkn_goto": "::",
    "tkn_length": "#",
}

RUTA_GRAMATICA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gramatica.txt")


def cargar_gramatica(ruta=RUTA_GRAMATICA):
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()


GRAMATICA_TEXTO = cargar_gramatica()


def main():
    codigo = sys.stdin.read()
    tokens = tokenizador(codigo)
    gramatica = parsear_gramatica(GRAMATICA_TEXTO)
    simbolo_inicial = next(iter(gramatica))
    primeros = calcular_primeros(gramatica)
    predicciones = conjuntos_de_prediccion(
        gramatica,
        simbolo_inicial=simbolo_inicial,
        fin_cadena="final_de_archivo",
        primeros=primeros,
    )
    analizador = AnalizadorSintactico(
        predicciones=predicciones,
        primeros=primeros,
        simbolo_inicial=simbolo_inicial,
        fin_cadena="final_de_archivo",
        mapa_simbolos=MAPA_SIMBOLOS,
    )
    analizador.analizar(tokens)


if __name__ == "__main__":
    main()
