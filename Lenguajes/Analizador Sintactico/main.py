"""
Módulo principal: main.py
Punto de entrada para el analizador sintáctico del lenguaje Lua.
Configura la gramática de Lua, el tokenizador y el mapa de símbolos,
y utiliza el motor LL(1) para realizar el análisis sintáctico.
"""

import sys
from analizador_lexico import tokenizador
from analizador_sintactico import AnalizadorSintactico, parsear_gramatica
from conjuntos_de_prediccion import calcular_primeros, conjuntos_de_prediccion

# Mapa de representación de símbolos para mensajes de error de Lua
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

GRAMATICA_TEXTO = """
CHUNK -> BLOCK final_de_archivo

BLOCK -> STAT_LIST RETSTAT_OPCIONAL

STAT_LIST -> STAT STAT_LIST
           | epsilon

STAT -> tkn_semicolon
      | while EXP do BLOCK end
      | repeat BLOCK until EXP
      | if EXP then BLOCK IF_TAIL
      | for NAME FOR_TAIL
      | function FUNCNAME FUNCBODY
      | local LOCAL_TAIL
      | global GLOBAL_TAIL
      | break
      | goto NAME
      | LABEL
      | NAME STAT_IDENT_TAIL

IF_TAIL -> elseif EXP then BLOCK IF_TAIL
         | else BLOCK end
         | end

FOR_TAIL -> tkn_assign EXP tkn_comma EXP FOR_STEP_OPCIONAL do BLOCK end
          | NAMELIST_TAIL in EXPLIST do BLOCK end

FOR_STEP_OPCIONAL -> tkn_comma EXP
                   | epsilon

LOCAL_TAIL -> function NAME FUNCBODY
            | NAME ATTNAMELIST_TAIL LOCAL_ASIGNACION_OPCIONAL

GLOBAL_TAIL -> function NAME FUNCBODY
             | NAME ATTNAMELIST_TAIL GLOBAL_ASIGNACION_OPCIONAL

LOCAL_ASIGNACION_OPCIONAL -> tkn_assign ASIGN_EXPLIST
                           | epsilon

GLOBAL_ASIGNACION_OPCIONAL -> tkn_assign ASIGN_EXPLIST
                            | epsilon

STAT_IDENT_TAIL -> tkn_period NAME STAT_IDENT_TAIL
                 | tkn_opening_bra EXP tkn_closing_bra STAT_IDENT_TAIL
                 | tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par CALL_TAIL
                 | tkn_colon NAME tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par CALL_TAIL
                 | tkn_comma VARLIST_ASSIGN
                 | tkn_assign ASIGN_EXPLIST

ATTNAMELIST_TAIL -> ATTRIB_OPCIONAL ATTNAMELIST_TAIL_RESTO

ATTNAMELIST_TAIL_RESTO -> tkn_comma NAME ATTNAMELIST_TAIL
                        | epsilon

ATTRIB -> tkn_less NAME tkn_greater

ATTRIB_OPCIONAL -> ATTRIB
                 | epsilon

RETSTAT -> return EXPLIST_OPCIONAL SEMICOLON_OPCIONAL

RETSTAT_OPCIONAL -> RETSTAT
                  | epsilon

SEMICOLON_OPCIONAL -> tkn_semicolon
                    | epsilon

LABEL -> tkn_goto NAME tkn_goto

FUNCNAME -> NAME FUNCNAME_TAIL

FUNCNAME_TAIL -> tkn_period NAME FUNCNAME_TAIL
               | tkn_colon NAME
               | epsilon

VARLIST_ASSIGN -> VAR VARLIST_ASSIGN_TAIL

VARLIST_ASSIGN_TAIL -> tkn_comma VARLIST_ASSIGN
                     | tkn_assign ASIGN_EXPLIST

VAR -> NAME VAR_SUFFIX

VAR_SUFFIX -> tkn_period NAME VAR_SUFFIX
            | tkn_opening_bra EXP tkn_closing_bra VAR_SUFFIX
            | epsilon

NAMELIST_TAIL -> tkn_comma NAME NAMELIST_TAIL
               | epsilon

ASIGN_EXP -> EXP
           | FUNCTIONDEF
           | tkn_varargs

ASIGN_EXPLIST -> ASIGN_EXP ASIGN_EXPLIST_TAIL

ASIGN_EXPLIST_TAIL -> tkn_comma ASIGN_EXP ASIGN_EXPLIST_TAIL
                    | epsilon

EXPLIST -> EXP EXPLIST_TAIL

EXPLIST_TAIL -> tkn_comma EXP EXPLIST_TAIL
              | epsilon

EXPLIST_OPCIONAL -> EXPLIST
                  | epsilon

EXP -> UNOP EXP
     | TERM EXP_TAIL

EXP_TAIL -> BINOP EXP
          | epsilon

TERM -> nil
      | false
      | true
      | valor_numerico
      | cadena_de_caracteres
      | TABLECONSTRUCTOR
      | PREFIXEXP

PREFIXEXP -> NAME PREFIX_SUFFIX
           | tkn_opening_par EXP tkn_closing_par PREFIX_SUFFIX

PREFIX_SUFFIX -> tkn_period NAME PREFIX_SUFFIX
               | tkn_opening_bra EXP tkn_closing_bra PREFIX_SUFFIX
               | tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par PREFIX_SUFFIX
               | tkn_colon NAME tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par PREFIX_SUFFIX
               | epsilon

CALL_TAIL -> tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par CALL_TAIL
           | tkn_colon NAME tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par CALL_TAIL
           | tkn_period NAME STAT_IDENT_TAIL
           | tkn_opening_bra EXP tkn_closing_bra STAT_IDENT_TAIL
           | epsilon

FUNCTIONDEF -> function FUNCBODY

FUNCBODY -> tkn_opening_par PARLIST_OPCIONAL tkn_closing_par BLOCK_FUNC end

BLOCK_FUNC -> STAT_LIST RETSTAT_OPCIONAL

PARLIST_OPCIONAL -> PARLIST
                  | epsilon

PARLIST -> VARARGPARAM
         | NAME PARLIST_TAIL

PARLIST_TAIL -> tkn_comma PARLIST_RESTO
              | epsilon

PARLIST_RESTO -> VARARGPARAM
               | NAME PARLIST_TAIL

VARARGPARAM -> tkn_varargs VARARG_NAME_OPCIONAL

VARARG_NAME_OPCIONAL -> NAME
                      | epsilon

TABLECONSTRUCTOR -> tkn_opening_key FIELDLIST_OPCIONAL tkn_closing_key

FIELDLIST -> FIELD FIELDLIST_TAIL

FIELDLIST_OPCIONAL -> FIELDLIST
                    | epsilon

FIELDLIST_TAIL -> FIELDSEP FIELDLIST_RESTO
                | epsilon

FIELDLIST_RESTO -> FIELD FIELDLIST_TAIL
                 | epsilon

FIELD -> tkn_opening_bra EXP tkn_closing_bra tkn_assign ASIGN_EXP
       | NAME FIELD_IDENT_TAIL
       | UNOP EXP
       | nil EXP_TAIL
       | false EXP_TAIL
       | true EXP_TAIL
       | valor_numerico EXP_TAIL
       | cadena_de_caracteres EXP_TAIL
       | tkn_varargs EXP_TAIL
       | FUNCTIONDEF EXP_TAIL
       | TABLECONSTRUCTOR EXP_TAIL
       | tkn_opening_par EXP tkn_closing_par PREFIX_SUFFIX EXP_TAIL

FIELD_IDENT_TAIL -> tkn_assign ASIGN_EXP
                  | PREFIX_SUFFIX EXP_TAIL

FIELDSEP -> tkn_comma
          | tkn_semicolon

BINOP -> tkn_plus
       | tkn_minus
       | tkn_times
       | tkn_div
       | tkn_floor_div
       | tkn_power
       | tkn_mod
       | tkn_bit_and
       | tkn_bitex_or
       | tkn_bit_or
       | tkn_right_shift
       | tkn_left_shift
       | tkn_concat
       | tkn_less
       | tkn_leq
       | tkn_greater
       | tkn_geq
       | tkn_equal
       | tkn_neq
       | and
       | or

UNOP -> tkn_minus
      | not
      | tkn_length

NAME -> id
      | error
      | pcall
      | print
      | warn
      | xpcall
"""


def leer_entrada():
    """Lee el código fuente desde stdin (en terminal interactiva, finaliza con Enter en línea vacía)."""
    if not sys.stdin.isatty():
        return sys.stdin.read()

    lineas = []
    while True:
        try:
            linea = sys.stdin.readline()
        except (EOFError, KeyboardInterrupt):
            break
        if not linea or linea in ("\n", "\r\n"):
            break
        lineas.append(linea)
    return "".join(lineas)


def main():
    codigo = leer_entrada()
    tokens = tokenizador(codigo)
    gramatica = parsear_gramatica(GRAMATICA_TEXTO)
    primeros = calcular_primeros(gramatica)
    predicciones = conjuntos_de_prediccion(
        gramatica,
        simbolo_inicial="CHUNK",
        fin_cadena="final_de_archivo",
        primeros=primeros,
    )
    analizador = AnalizadorSintactico(
        predicciones=predicciones,
        primeros=primeros,
        simbolo_inicial="CHUNK",
        fin_cadena="final_de_archivo",
        mapa_simbolos=MAPA_SIMBOLOS,
    )
    analizador.analizar(tokens)


if __name__ == "__main__":
    main()
