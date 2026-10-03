import sys

# Conjunto oficial de palabras reservadas de Lua + la función 'print' requerida en la práctica
RESERVED_WORDS = {
    "and", "break", "do", "else", "elseif", "end", "false",
    "for", "function", "goto", "if", "in", "local", "nil",
    "not", "or", "repeat", "return", "then", "true", "until",
    "while", "print"
}

# Operadores y símbolos especiales de 3 caracteres
SYMBOLS_3 = {
    "...": "tkn_varargs"
}

# Operadores y símbolos especiales de 2 caracteres
SYMBOLS_2 = {
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
SYMBOLS_1 = {
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


def is_latin_alpha(c: str) -> bool:
    """Verifica si el carácter es una letra del alfabeto latino estándar."""
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z')


def is_ident_start(c: str) -> bool:
    """Un identificador puede iniciar con letra latina o guión bajo."""
    return is_latin_alpha(c) or c == '_'


def is_ident_part(c: str) -> bool:
    """Un identificador puede continuar con letras latinas, dígitos o guión bajo."""
    return is_latin_alpha(c) or ('0' <= c <= '9') or c == '_'


def report_lexical_error(line: int, col: int) -> None:
    """Emite el mensaje de error léxico especificado y aborta la ejecución."""
    print(f">>> Error lexico (linea: {line}, posicion: {col})")
    sys.exit(0)


def tokenize(source: str) -> None:
    i = 0
    n = len(source)
    line = 1
    col = 1

    while i < n:
        c = source[i]

        # 1. Manejo de saltos de línea y espacios en blanco
        if c == '\r':
            if i + 1 < n and source[i + 1] == '\n':
                i += 2
            else:
                i += 1
            line += 1
            col = 1
            continue

        if c == '\n':
            i += 1
            line += 1
            col = 1
            continue

        if c in (' ', '\t'):
            i += 1
            col += 1
            continue

        # 2. Comentarios (-- o --[[ ... ]])
        if c == '-' and i + 1 < n and source[i + 1] == '-':
            if source[i:i + 4] == '--[[':
                start_comment_line = line
                start_comment_col = col
                i += 4
                col += 4
                closed = False
                while i < n:
                    if source[i:i + 2] == ']]':
                        i += 2
                        col += 2
                        closed = True
                        break
                    elif source[i] == '\r':
                        if i + 1 < n and source[i + 1] == '\n':
                            i += 2
                        else:
                            i += 1
                        line += 1
                        col = 1
                    elif source[i] == '\n':
                        i += 1
                        line += 1
                        col = 1
                    else:
                        i += 1
                        col += 1
                if not closed:
                    report_lexical_error(start_comment_line, start_comment_col)
                continue
            else:
                # Comentario de una línea: ignorar hasta el salto de línea o fin de archivo
                i += 2
                col += 2
                while i < n and source[i] not in ('\r', '\n'):
                    i += 1
                    col += 1
                continue

        # 3. Cadenas de caracteres ("..." o '...')
        if c in ('"', "'"):
            delim = c
            start_line = line
            start_col = col
            i += 1
            col += 1
            content_chars = []
            closed = False

            while i < n:
                curr = source[i]
                if curr == '\\':
                    if i + 1 >= n:
                        report_lexical_error(start_line, start_col)
                    next_c = source[i + 1]
                    if next_c == '\r':
                        if i + 2 < n and source[i + 2] == '\n':
                            content_chars.append(source[i:i + 3])
                            i += 3
                        else:
                            content_chars.append(source[i:i + 2])
                            i += 2
                        line += 1
                        col = 1
                    elif next_c == '\n':
                        content_chars.append(source[i:i + 2])
                        i += 2
                        line += 1
                        col = 1
                    else:
                        content_chars.append(source[i:i + 2])
                        i += 2
                        col += 2
                elif curr in ('\r', '\n'):
                    # Cadena no cerrada antes de finalizar la línea
                    report_lexical_error(start_line, start_col)
                elif curr == delim:
                    i += 1
                    col += 1
                    closed = True
                    break
                else:
                    content_chars.append(curr)
                    i += 1
                    col += 1

            if not closed:
                report_lexical_error(start_line, start_col)

            lexeme = "".join(content_chars)
            print(f"<tkn_str,{lexeme},{start_line},{start_col}>")
            continue

        # 4. Literales numéricos (enteros y decimales)
        if '0' <= c <= '9':
            start_line = line
            start_col = col
            start_idx = i
            while i < n and ('0' <= source[i] <= '9'):
                i += 1
                col += 1
            # Reconoce punto decimal solo si le sigue al menos un dígito (Maximal Munch)
            if i < n and source[i] == '.':
                if i + 1 < n and ('0' <= source[i + 1] <= '9'):
                    i += 1
                    col += 1
                    while i < n and ('0' <= source[i] <= '9'):
                        i += 1
                        col += 1
            lexeme = source[start_idx:i]
            print(f"<tkn_num,{lexeme},{start_line},{start_col}>")
            continue

        # 5. Identificadores y palabras reservadas
        if is_ident_start(c):
            start_line = line
            start_col = col
            start_idx = i
            while i < n and is_ident_part(source[i]):
                i += 1
                col += 1
            lexeme = source[start_idx:i]
            if lexeme in RESERVED_WORDS:
                print(f"<{lexeme},{start_line},{start_col}>")
            else:
                print(f"<id,{lexeme},{start_line},{start_col}>")
            continue

        # 6. Operadores y símbolos especiales (Maximal Munch: 3, luego 2, luego 1 carácter)
        if i + 3 <= n and source[i:i + 3] in SYMBOLS_3:
            tok = SYMBOLS_3[source[i:i + 3]]
            print(f"<{tok},{line},{col}>")
            i += 3
            col += 3
            continue

        if i + 2 <= n and source[i:i + 2] in SYMBOLS_2:
            tok = SYMBOLS_2[source[i:i + 2]]
            print(f"<{tok},{line},{col}>")
            i += 2
            col += 2
            continue

        if c in SYMBOLS_1:
            tok = SYMBOLS_1[c]
            print(f"<{tok},{line},{col}>")
            i += 1
            col += 1
            continue

        # 7. Carácter no perteneciente al alfabeto de Lua -> Error léxico inmediato
        report_lexical_error(line, col)


def main() -> None:
    source = sys.stdin.read()
    tokenize(source)


if __name__ == "__main__":
    main()
