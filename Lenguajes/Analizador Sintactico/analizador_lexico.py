"""
Módulo: analizador_lexico.py
Analizador léxico para el lenguaje de programación Lua.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Token:
    tipo: str
    lexema: str
    fila: int
    columna: int

    def __getitem__(self, item):
        return getattr(self, item)


RESERVADAS = {
    "and", "break", "do", "else", "elseif", "end", "false", "for", "function",
    "global", "goto", "if", "in", "local", "nil", "not", "or", "repeat",
    "return", "then", "true", "until", "while",
    "error", "pcall", "print", "warn", "xpcall"
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


class AnalizadorLexico:
    """Analizador léxico que convierte código fuente Lua en una secuencia de tokens."""

    def __init__(self, codigo: str):
        self.codigo = codigo.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
        self.longitud = len(self.codigo)
        self.pos = 0
        self.fila = 1
        self.columna = 1

    def tokenizar(self) -> list[Token]:
        tokens = []
        while self.pos < self.longitud:
            c = self.codigo[self.pos]

            if c == "\n":
                self.pos += 1
                self.fila += 1
                self.columna = 1
            elif c.isspace():
                self.pos += 1
                self.columna += 1
            elif self.codigo.startswith("--[[", self.pos):
                self._saltar_comentario_bloque()
            elif self.codigo.startswith("--", self.pos):
                self._saltar_comentario_linea()
            else:
                tokens.append(self._extraer_token())

        fila_eof = len(self.codigo.splitlines()) + 1 if self.codigo else 1
        tokens.append(Token("final_de_archivo", "final de archivo", fila_eof, 1))
        return tokens

    def _saltar_comentario_bloque(self):
        self.pos += 4
        self.columna += 4
        while self.pos < self.longitud and not self.codigo.startswith("]]", self.pos):
            if self.codigo[self.pos] == "\n":
                self.fila += 1
                self.columna = 1
            else:
                self.columna += 1
            self.pos += 1
        if self.codigo.startswith("]]", self.pos):
            self.pos += 2
            self.columna += 2

    def _saltar_comentario_linea(self):
        self.pos += 2
        while self.pos < self.longitud and self.codigo[self.pos] != "\n":
            self.pos += 1

    def _extraer_token(self) -> Token:
        fila, col = self.fila, self.columna
        c = self.codigo[self.pos]

        # Identificadores y palabras reservadas
        if ("a" <= c <= "z") or ("A" <= c <= "Z") or c == "_":
            inicio = self.pos
            while self.pos < self.longitud and (
                ("a" <= self.codigo[self.pos] <= "z")
                or ("A" <= self.codigo[self.pos] <= "Z")
                or ("0" <= self.codigo[self.pos] <= "9")
                or self.codigo[self.pos] == "_"
            ):
                self.pos += 1
            lexema = self.codigo[inicio:self.pos]
            self.columna += len(lexema)
            tipo = lexema if lexema in RESERVADAS else "id"
            return Token(tipo, lexema, fila, col)

        # Números
        if c.isdigit():
            inicio = self.pos
            while self.pos < self.longitud and self.codigo[self.pos].isdigit():
                self.pos += 1
            if self.pos < self.longitud and self.codigo[self.pos] == ".":
                if self.pos + 1 < self.longitud and self.codigo[self.pos + 1].isdigit():
                    self.pos += 1
                    while self.pos < self.longitud and self.codigo[self.pos].isdigit():
                        self.pos += 1
            lexema = self.codigo[inicio:self.pos]
            self.columna += len(lexema)
            return Token("valor_numerico", lexema, fila, col)

        # Cadenas de caracteres
        if c in ('"', "'"):
            comilla = c
            inicio = self.pos
            self.pos += 1
            lexema = ""
            while self.pos < self.longitud and self.codigo[self.pos] != comilla:
                if self.codigo[self.pos] == "\\" and self.pos + 1 < self.longitud:
                    lexema += self.codigo[self.pos:self.pos + 2]
                    self.pos += 2
                else:
                    lexema += self.codigo[self.pos]
                    self.pos += 1
            self.pos += 1
            self.columna += (self.pos - inicio)
            return Token("cadena_de_caracteres", lexema, fila, col)

        # Símbolo de 3 caracteres (...)
        if self.codigo.startswith("...", self.pos):
            self.pos += 3
            self.columna += 3
            return Token("tkn_varargs", "...", fila, col)

        # Símbolos de 2 caracteres
        op2 = self.codigo[self.pos:self.pos + 2]
        if op2 in SIMBOLOS2:
            self.pos += 2
            self.columna += 2
            return Token(SIMBOLOS2[op2], op2, fila, col)

        # Símbolos de 1 carácter
        if c in SIMBOLOS1:
            self.pos += 1
            self.columna += 1
            return Token(SIMBOLOS1[c], c, fila, col)


def tokenizador(codigo: str) -> list[Token]:
    """Función de conveniencia para tokenizar código fuente Lua."""
    return AnalizadorLexico(codigo).tokenizar()
