import sys


RESERVADAS = {
    # "Lexical Conventions"
    "and",
    "break",
    "do",
    "else",
    "elseif",
    "end",
    "false",
    "for",
    "function",
    "global",
    "goto",
    "if",
    "in",
    "local",
    "nil",
    "not",
    "or",
    "repeat",
    "return",
    "then",
    "true",
    "until",
    "while",
    # Funciones
    "error",
    "pcall",
    "print",
    "warn",
    "xpcall",
}

SIMBOLOS3 = {
    "...": "tkn_varargs"
}

# Operadores y símbolos especiales de 2 caracteres
SIMBOLOS2 = {
    ">>": "tkn_right_shift",
    "<<": "tkn_left_shift",
    "..": "tkn_concat",
    "::": "tkn_goto",
    "//": "tkn_floor_div",
    "==": "tkn_equal",
    "~=": "tkn_neq",
    "<=": "tkn_leq",
    ">=": "tkn_geq",
}

# Operadores y símbolos especiales de 1 carácter
SIMBOLOS1 = {
    "&": "tkn_bit_and",
    "|": "tkn_bit_or",
    "~": "tkn_bitex_or",
    ";": "tkn_semicolon",
    ":": "tkn_colon",
    ",": "tkn_comma",
    ".": "tkn_period",
    "{": "tkn_opening_key",
    "}": "tkn_closing_key",
    "[": "tkn_opening_bra",
    "]": "tkn_closing_bra",
    "(": "tkn_opening_par",
    ")": "tkn_closing_par",
    "#": "tkn_length",
    "+": "tkn_plus",
    "-": "tkn_minus",
    "*": "tkn_times",
    "/": "tkn_div",
    "^": "tkn_power",
    "%": "tkn_mod",
    ">": "tkn_greater",
    "<": "tkn_less",
    "=": "tkn_assign",
}


def es_ident_inicio(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or c == '_'

def es_ident_parte(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9') or c == '_'


def siguiente_lexema(string, i):
    nombre_token = None
    lexema = ""
    j = i
    # Buscar un identificador o palabra reservada (restringido a ASCII)
    if es_ident_inicio(string[i]):
        while j < len(string) and es_ident_parte(string[j]):
            lexema += string[j]
            j += 1
        if lexema in RESERVADAS:
            nombre_token = "reservada"
        else:
            nombre_token = "id" 

    elif string[i].isdigit():
        while j < len(string) and string[j].isdigit():
            lexema += string[j]
            j += 1
        # Solo absorbe el punto decimal si le sigue al menos un dígito (evita colisión con '..')
        if j < len(string) and string[j] == '.':
            if j + 1 < len(string) and string[j + 1].isdigit():
                lexema += string[j]
                j += 1
                while j < len(string) and string[j].isdigit():
                    lexema += string[j]
                    j += 1
        nombre_token = "tkn_num"


    elif string[i] == '"' or string[i] == "'":
        tipo_comilla = string[i]
        j += 1
        cerrada = False
        while j < len(string):
            if string[j] == '\\':
                if j + 1 < len(string):
                    # Preservar el escape (ej: \", \', \\) y saltar ambos caracteres
                    lexema += string[j:j+2]
                    j += 2
                else:
                    break
            elif string[j] == '\n':
                # En Lua una cadena con comillas no puede contener saltos de línea sin escapar
                break
            elif string[j] == tipo_comilla:
                j += 1  # Consumir comilla de cierre
                cerrada = True
                break
            else:
                lexema += string[j]
                j += 1
        if cerrada:
            nombre_token = "tkn_str"


    elif  string[i:i+3] in SIMBOLOS3:
        j = i + 3
        lexema = string[i:i+3]
        nombre_token = SIMBOLOS3[lexema]

    elif string[i:i+2] in SIMBOLOS2:
        j = i + 2
        lexema = string[i:i+2]
        nombre_token = SIMBOLOS2[lexema]
    elif string[i] in SIMBOLOS1:
        j = i + 1
        lexema = string[i]
        nombre_token = SIMBOLOS1[lexema]

    return nombre_token, lexema, j

def tokenizador(input):
    i = 0
    fila, columna = 1, 1
    while True:
        
        if i >= len(input):
            break
        if input[i] == '\n':
            i += 1
            fila += 1
            columna = 1
        elif input[i].isspace():
            i += 1
            columna += 1
        # Comentarios multilínea: --[[ ... ]]
        elif input[i:i+4] == '--[[':
            inicio_fila, inicio_columna = fila, columna
            i += 4
            columna += 4
            while i < len(input) and input[i:i+2] != ']]':
                if input[i] == '\n':
                    fila += 1
                    columna = 1
                    i += 1
                else:
                    columna += 1
                    i += 1
            if i < len(input) and input[i:i+2] == ']]':
                i += 2
                columna += 2
            else:
                print(f">>> Error lexico (linea: {inicio_fila}, posicion: {inicio_columna})")
                break
        # Comentarios de una sola línea: -- ...
        elif input[i:i+2] == '--':
            i += 2
            while i < len(input) and input[i] != '\n': #En la siguiente se consume el \n
                i += 1
        else:
            nombre_token, lexema, nuevo_i = siguiente_lexema(input, i)
            # Si no se reconoció ningún token -> Error léxico 
            if nombre_token is None:
                print(f">>> Error lexico (linea: {fila}, posicion: {columna})")
                break

            if nombre_token == "reservada":
                # sin nombre_token
                print(f"<{lexema},{fila},{columna}>")
            elif nombre_token in ("id", "tkn_num", "tkn_str"):
                # <tipo,lexema,fila,columna>
                print(f"<{nombre_token},{lexema},{fila},{columna}>")
            else:
                # Símbolos y operadores: <tkn_nombre_token,fila,columna> (sin lexema)
                print(f"<{nombre_token},{fila},{columna}>")

            # Avanzar a la siguiente posición
            columna += (nuevo_i - i)
            i = nuevo_i


codigo_fuente = sys.stdin.read().replace('\r\n', '\n').replace('\r', '\n')
tokenizador(codigo_fuente)