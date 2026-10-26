"""
Módulo: analizador_sintactico.py
Analizador sintáctico predictivo LL(1) para el lenguaje de programación Lua.
"""

from typing import Optional
from analizador_lexico import Token, tokenizador, RESERVADAS, SIMBOLOS1, SIMBOLOS2, SIMBOLOS3


# Mapeo de tipo de token a representación amigable para el usuario
TIPO_A_LEXEMA = {
    # Tipos especiales
    "id": "id",
    "valor_numerico": "valor_numerico",
    "cadena_de_caracteres": "cadena_de_caracteres",
    "final_de_archivo": "final de archivo",

    # Símbolos de 3 caracteres
    "tkn_varargs": "...",

    # Símbolos de 2 caracteres
    "tkn_right_shift": ">>",
    "tkn_left_shift": "<<",
    "tkn_concat": "..",
    "tkn_goto": "::",
    "tkn_floor_div": "//",
    "tkn_equal": "==",
    "tkn_neq": "~=",
    "tkn_leq": "<=",
    "tkn_geq": ">=",

    # Símbolos de 1 carácter
    "tkn_bit_and": "&",
    "tkn_bit_or": "|",
    "tkn_bitex_or": "~",
    "tkn_semicolon": ";",
    "tkn_colon": ":",
    "tkn_comma": ",",
    "tkn_period": ".",
    "tkn_opening_key": "{",
    "tkn_closing_key": "}",
    "tkn_opening_bra": "[",
    "tkn_closing_bra": "]",
    "tkn_opening_par": "(",
    "tkn_closing_par": ")",
    "tkn_length": "#",
    "tkn_plus": "+",
    "tkn_minus": "-",
    "tkn_times": "*",
    "tkn_div": "/",
    "tkn_power": "^",
    "tkn_mod": "%",
    "tkn_greater": ">",
    "tkn_less": "<",
    "tkn_assign": "=",
}

for kw in RESERVADAS:
    TIPO_A_LEXEMA[kw] = kw


# Conjuntos de tokens
NAMES = {"id", "error", "pcall", "print", "warn", "xpcall"}

UNOP = {"not", "tkn_length", "tkn_minus"}

LITERALS = {"valor_numerico", "cadena_de_caracteres", "nil", "true", "false"}

FIRST_EXP = NAMES | UNOP | LITERALS | {"tkn_opening_key", "tkn_opening_par"}

BINOPS = {
    "and", "or", "tkn_bit_and", "tkn_bit_or", "tkn_bitex_or",
    "tkn_concat", "tkn_div", "tkn_equal", "tkn_floor_div", "tkn_geq",
    "tkn_greater", "tkn_left_shift", "tkn_leq", "tkn_less", "tkn_minus",
    "tkn_mod", "tkn_neq", "tkn_plus", "tkn_power", "tkn_right_shift", "tkn_times"
}

STAT_STARTERS = {
    "break", "for", "function", "global", "goto", "if", "local",
    "repeat", "tkn_goto", "tkn_semicolon", "while"
} | NAMES


class ErrorSintactico(Exception):
    def __init__(self, token: Token, esperados: set[str]):
        self.token = token
        self.esperados = esperados
        super().__init__(self.formatear())

    def formatear(self) -> str:
        lexema_encontrado = self.token.lexema
        sorted_tipos = sorted(self.esperados)
        esperados_str = ", ".join(f'"{TIPO_A_LEXEMA.get(t, t)}"' for t in sorted_tipos)
        return (
            f"<{self.token.fila}:{self.token.columna}> Error sintactico: "
            f'se encontro: "{lexema_encontrado}"; se esperaba: {esperados_str}.'
        )


class AnalizadorSintactico:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    @property
    def token_actual(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]

    def peek(self, n: int = 1) -> Token:
        target = self.pos + n
        if target < len(self.tokens):
            return self.tokens[target]
        return self.tokens[-1]

    def consumir(self, tipo_esperado: str) -> Token:
        tok = self.token_actual
        if tok.tipo == tipo_esperado:
            self.pos += 1
            return tok
        raise ErrorSintactico(tok, {tipo_esperado})

    def consumir_nombre(self) -> Token:
        tok = self.token_actual
        if tok.tipo in NAMES:
            self.pos += 1
            return tok
        raise ErrorSintactico(tok, set(NAMES))

    def analizar(self):
        """Punto de entrada para analizar un programa completo (chunk)."""
        self.parse_block(stop_tokens={"final_de_archivo"})
        self.consumir("final_de_archivo")

    def parse_block(self, stop_tokens: set[str]):
        """Parsea una secuencia de sentencias y opcional retstat."""
        while True:
            tok = self.token_actual
            if tok.tipo in stop_tokens:
                break
            if tok.tipo == "return":
                self.parse_retstat(stop_tokens)
                break
            if tok.tipo in STAT_STARTERS:
                self.parse_stat()
            else:
                esperados = STAT_STARTERS | {"return"} | stop_tokens
                raise ErrorSintactico(tok, esperados)

    def parse_stat(self):
        tok = self.token_actual

        if tok.tipo == "tkn_semicolon":
            self.consumir("tkn_semicolon")
        elif tok.tipo == "break":
            self.consumir("break")
        elif tok.tipo == "goto":
            self.consumir("goto")
            self.consumir_nombre()
        elif tok.tipo == "tkn_goto":  # :: label ::
            self.consumir("tkn_goto")
            self.consumir_nombre()
            self.consumir("tkn_goto")
        elif tok.tipo == "while":
            self.consumir("while")
            self.parse_exp(follow={"do"})
            self.consumir("do")
            self.parse_block(stop_tokens={"end"})
            self.consumir("end")
        elif tok.tipo == "repeat":
            self.consumir("repeat")
            self.parse_block(stop_tokens={"until"})
            self.consumir("until")
            self.parse_exp(follow=STAT_STARTERS | {"return", "end", "until", "elseif", "else", "final_de_archivo"})
        elif tok.tipo == "if":
            self.consumir("if")
            self.parse_exp(follow={"then"})
            self.consumir("then")
            self.parse_block(stop_tokens={"elseif", "else", "end"})
            while self.token_actual.tipo == "elseif":
                self.consumir("elseif")
                self.parse_exp(follow={"then"})
                self.consumir("then")
                self.parse_block(stop_tokens={"elseif", "else", "end"})
            if self.token_actual.tipo == "else":
                self.consumir("else")
                self.parse_block(stop_tokens={"end"})
            self.consumir("end")
        elif tok.tipo == "for":
            self.consumir("for")
            self.consumir_nombre()
            tok_next = self.token_actual
            if tok_next.tipo == "tkn_assign":
                # for Name = exp, exp [, exp] do block end
                self.consumir("tkn_assign")
                self.parse_exp(follow={"tkn_comma"})
                self.consumir("tkn_comma")
                self.parse_exp(follow={"tkn_comma", "do"})
                if self.token_actual.tipo == "tkn_comma":
                    self.consumir("tkn_comma")
                    self.parse_exp(follow={"do"})
                self.consumir("do")
                self.parse_block(stop_tokens={"end"})
                self.consumir("end")
            elif tok_next.tipo in {"tkn_comma", "in"}:
                # for namelist in explist do block end
                while self.token_actual.tipo == "tkn_comma":
                    self.consumir("tkn_comma")
                    self.consumir_nombre()
                self.consumir("in")
                self.parse_explist(follow={"do"})
                self.consumir("do")
                self.parse_block(stop_tokens={"end"})
                self.consumir("end")
            else:
                raise ErrorSintactico(tok_next, {"in", "tkn_assign", "tkn_comma"})
        elif tok.tipo == "function":
            self.consumir("function")
            self.consumir_nombre()
            # funcname
            while self.token_actual.tipo == "tkn_period":
                self.consumir("tkn_period")
                self.consumir_nombre()
            if self.token_actual.tipo == "tkn_colon":
                self.consumir("tkn_colon")
                self.consumir_nombre()
            elif self.token_actual.tipo != "tkn_opening_par":
                raise ErrorSintactico(self.token_actual, {"tkn_colon", "tkn_opening_par", "tkn_period"})
            self.parse_funcbody()
        elif tok.tipo in {"local", "global"}:
            kw = tok.tipo
            self.consumir(kw)
            if self.token_actual.tipo == "function":
                self.consumir("function")
                self.consumir_nombre()
                self.parse_funcbody()
            elif self.token_actual.tipo in NAMES:
                self.consumir_nombre()
                while self.token_actual.tipo == "tkn_comma":
                    self.consumir("tkn_comma")
                    self.consumir_nombre()
                if self.token_actual.tipo == "tkn_assign":
                    self.consumir("tkn_assign")
                    self.parse_explist(follow=STAT_STARTERS | {"return", "end", "until", "elseif", "else", "final_de_archivo", "tkn_semicolon"})
            else:
                raise ErrorSintactico(self.token_actual, {"function"} | NAMES)
        elif tok.tipo in NAMES:
            self.parse_call_or_assign_stat()
        else:
            raise ErrorSintactico(tok, STAT_STARTERS)

    def parse_funcbody(self):
        self.consumir("tkn_opening_par")
        tok = self.token_actual
        if tok.tipo == "tkn_closing_par":
            self.consumir("tkn_closing_par")
        elif tok.tipo == "tkn_varargs":
            self.consumir("tkn_varargs")
            self.consumir("tkn_closing_par")
        elif tok.tipo in NAMES:
            self.consumir_nombre()
            while self.token_actual.tipo == "tkn_comma":
                self.consumir("tkn_comma")
                if self.token_actual.tipo == "tkn_varargs":
                    self.consumir("tkn_varargs")
                    break
                else:
                    self.consumir_nombre()
            self.consumir("tkn_closing_par")
        else:
            raise ErrorSintactico(tok, {"tkn_closing_par", "tkn_varargs"} | NAMES)
        self.parse_block(stop_tokens={"end"})
        self.consumir("end")

    def parse_call_or_assign_stat(self):
        """Parsea una sentencia que comienza con Name: varlist '=' explist o functioncall."""
        self.consumir_nombre()
        self._parse_call_or_assign_after_name()

    def _parse_call_or_assign_after_name(self):
        tok = self.token_actual
        opciones_esperadas = {
            "tkn_assign", "tkn_colon", "tkn_comma",
            "tkn_opening_bra", "tkn_opening_par", "tkn_period"
        }

        if tok.tipo == "tkn_assign":
            self.consumir("tkn_assign")
            self.parse_explist(follow=STAT_STARTERS | {"return", "end", "until", "elseif", "else", "final_de_archivo", "tkn_semicolon"})
        elif tok.tipo == "tkn_comma":
            self.consumir("tkn_comma")
            self._parse_remaining_varlist()
            self.consumir("tkn_assign")
            self.parse_explist(follow=STAT_STARTERS | {"return", "end", "until", "elseif", "else", "final_de_archivo", "tkn_semicolon"})
        elif tok.tipo == "tkn_opening_bra":
            self.consumir("tkn_opening_bra")
            self.parse_exp(follow={"tkn_closing_bra"})
            self.consumir("tkn_closing_bra")
            self._parse_call_or_assign_after_name()
        elif tok.tipo == "tkn_period":
            self.consumir("tkn_period")
            self.consumir_nombre()
            self._parse_call_or_assign_after_name()
        elif tok.tipo == "tkn_opening_par":
            self.consumir("tkn_opening_par")
            if self.token_actual.tipo in FIRST_EXP or self.token_actual.tipo == "function":
                self.parse_explist(follow={"tkn_closing_par"})
            self.consumir("tkn_closing_par")
            self._parse_optional_call_or_index_chain()
        elif tok.tipo == "tkn_colon":
            self.consumir("tkn_colon")
            self.consumir_nombre()
            self.consumir("tkn_opening_par")
            if self.token_actual.tipo in FIRST_EXP or self.token_actual.tipo == "function":
                self.parse_explist(follow={"tkn_closing_par"})
            self.consumir("tkn_closing_par")
            self._parse_optional_call_or_index_chain()
        else:
            raise ErrorSintactico(tok, opciones_esperadas)

    def _parse_remaining_varlist(self):
        """Parsea var { ',' var } hasta el '='."""
        while True:
            self.consumir_nombre()
            while self.token_actual.tipo in {"tkn_opening_bra", "tkn_period"}:
                if self.token_actual.tipo == "tkn_opening_bra":
                    self.consumir("tkn_opening_bra")
                    self.parse_exp(follow={"tkn_closing_bra"})
                    self.consumir("tkn_closing_bra")
                else:
                    self.consumir("tkn_period")
                    self.consumir_nombre()
            if self.token_actual.tipo == "tkn_comma":
                self.consumir("tkn_comma")
            else:
                break

    def _parse_optional_call_or_index_chain(self):
        """Parsea posibles encadenamientos después de una llamada: f()() o f().x = 1 o f()[1]."""
        while self.token_actual.tipo in {"tkn_opening_par", "tkn_colon", "tkn_opening_bra", "tkn_period"}:
            tok = self.token_actual
            if tok.tipo == "tkn_opening_par":
                self.consumir("tkn_opening_par")
                if self.token_actual.tipo in FIRST_EXP or self.token_actual.tipo == "function":
                    self.parse_explist(follow={"tkn_closing_par"})
                self.consumir("tkn_closing_par")
            elif tok.tipo == "tkn_colon":
                self.consumir("tkn_colon")
                self.consumir_nombre()
                self.consumir("tkn_opening_par")
                if self.token_actual.tipo in FIRST_EXP or self.token_actual.tipo == "function":
                    self.parse_explist(follow={"tkn_closing_par"})
                self.consumir("tkn_closing_par")
            elif tok.tipo == "tkn_opening_bra":
                self.consumir("tkn_opening_bra")
                self.parse_exp(follow={"tkn_closing_bra"})
                self.consumir("tkn_closing_bra")
                if self.token_actual.tipo == "tkn_assign":
                    self.consumir("tkn_assign")
                    self.parse_explist(follow=STAT_STARTERS | {"return", "end", "until", "elseif", "else", "final_de_archivo", "tkn_semicolon"})
                    return
            elif tok.tipo == "tkn_period":
                self.consumir("tkn_period")
                self.consumir_nombre()
                if self.token_actual.tipo == "tkn_assign":
                    self.consumir("tkn_assign")
                    self.parse_explist(follow=STAT_STARTERS | {"return", "end", "until", "elseif", "else", "final_de_archivo", "tkn_semicolon"})
                    return

    def parse_retstat(self, stop_tokens: set[str]):
        self.consumir("return")
        tok = self.token_actual
        if tok.tipo in FIRST_EXP or tok.tipo == "function":
            self.parse_explist(follow=stop_tokens | {"tkn_semicolon"})
        if self.token_actual.tipo == "tkn_semicolon":
            self.consumir("tkn_semicolon")
        if self.token_actual.tipo not in stop_tokens:
            raise ErrorSintactico(self.token_actual, stop_tokens)

    def parse_explist(self, follow: set[str]):
        """Parsea explist ::= (exp | functiondef) { ',' (exp | functiondef) }."""
        self._parse_exp_or_func(follow=follow | {"tkn_comma"})
        while self.token_actual.tipo == "tkn_comma":
            self.consumir("tkn_comma")
            self._parse_exp_or_func(follow=follow | {"tkn_comma"})

    def _parse_exp_or_func(self, follow: set[str]):
        if self.token_actual.tipo == "function":
            self.consumir("function")
            self.parse_funcbody()
        else:
            self.parse_exp(follow=follow)

    def parse_exp(self, follow: set[str]):
        """Parsea exp ::= atom { binop atom }."""
        self.parse_atom()
        while self.token_actual.tipo in BINOPS:
            self.consumir(self.token_actual.tipo)
            self.parse_atom()
        if self.token_actual.tipo not in follow:
            raise ErrorSintactico(self.token_actual, BINOPS | follow)

    def parse_atom(self):
        tok = self.token_actual
        if tok.tipo in UNOP:
            self.consumir(tok.tipo)
            self.parse_atom()
        elif tok.tipo in LITERALS:
            self.consumir(tok.tipo)
        elif tok.tipo == "tkn_opening_key":
            self.parse_tableconstructor()
        elif tok.tipo == "tkn_opening_par":
            self.consumir("tkn_opening_par")
            self.parse_exp(follow={"tkn_closing_par"})
            self.consumir("tkn_closing_par")
            self.parse_prefix_suffixes()
        elif tok.tipo in NAMES:
            self.consumir_nombre()
            self.parse_prefix_suffixes()
        else:
            raise ErrorSintactico(tok, set(FIRST_EXP))

    def parse_prefix_suffixes(self):
        """Parsea sufijos en expresiones: [exp], .Name, (args), :Name(args)."""
        while self.token_actual.tipo in {"tkn_opening_bra", "tkn_period", "tkn_opening_par", "tkn_colon"}:
            tok = self.token_actual
            if tok.tipo == "tkn_opening_bra":
                self.consumir("tkn_opening_bra")
                self.parse_exp(follow={"tkn_closing_bra"})
                self.consumir("tkn_closing_bra")
            elif tok.tipo == "tkn_period":
                self.consumir("tkn_period")
                self.consumir_nombre()
            elif tok.tipo == "tkn_opening_par":
                self.consumir("tkn_opening_par")
                if self.token_actual.tipo in FIRST_EXP or self.token_actual.tipo == "function":
                    self.parse_explist(follow={"tkn_closing_par"})
                self.consumir("tkn_closing_par")
            elif tok.tipo == "tkn_colon":
                self.consumir("tkn_colon")
                self.consumir_nombre()
                self.consumir("tkn_opening_par")
                if self.token_actual.tipo in FIRST_EXP or self.token_actual.tipo == "function":
                    self.parse_explist(follow={"tkn_closing_par"})
                self.consumir("tkn_closing_par")

    def parse_tableconstructor(self):
        self.consumir("tkn_opening_key")
        fieldsep = {"tkn_comma", "tkn_semicolon"}
        follow_field = fieldsep | {"tkn_closing_key"}

        if self.token_actual.tipo != "tkn_closing_key":
            self.parse_field(follow=follow_field)
            while self.token_actual.tipo in fieldsep:
                self.consumir(self.token_actual.tipo)
                if self.token_actual.tipo == "tkn_closing_key":
                    break
                self.parse_field(follow=follow_field)

        self.consumir("tkn_closing_key")

    def parse_field(self, follow: set[str]):
        tok = self.token_actual
        if tok.tipo == "tkn_opening_bra":
            self.consumir("tkn_opening_bra")
            self.parse_exp(follow={"tkn_closing_bra"})
            self.consumir("tkn_closing_bra")
            self.consumir("tkn_assign")
            self._parse_exp_or_func(follow=follow)
        elif tok.tipo in NAMES and self.peek().tipo == "tkn_assign":
            self.consumir_nombre()
            self.consumir("tkn_assign")
            self._parse_exp_or_func(follow=follow)
        elif tok.tipo == "function":
            self.consumir("function")
            self.parse_funcbody()
        else:
            self.parse_exp(follow=follow)


def main():
    import sys
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

