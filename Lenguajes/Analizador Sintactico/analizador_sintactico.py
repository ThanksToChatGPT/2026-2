"""
Módulo: analizador_sintactico.py
Analizador Sintáctico en base a un conjunto de predicciones LL(1).
"""

from conjuntos_de_prediccion import descomponer_produccion


def parsear_gramatica(gramatica_str):
    """Convierte una especificación de gramática en texto a un diccionario de producciones."""
    gramatica = {}
    actual_nt = None

    for linea in gramatica_str.splitlines():
        linea = linea.strip()
        if not linea or linea.startswith(("#", "//", "```")):
            continue

        sep = "::=" if "::=" in linea else ("->" if "->" in linea else None)
        if sep:
            partes = linea.split(sep, 1)
            actual_nt = partes[0].strip()
            gramatica.setdefault(actual_nt, [])
            for alt in partes[1].split("|"):
                alt = alt.strip()
                if alt:
                    gramatica[actual_nt].append(alt)
        elif linea.startswith("|") and actual_nt:
            for alt in linea[1:].split("|"):
                alt = alt.strip()
                if alt:
                    gramatica[actual_nt].append(alt)

    return gramatica


class AnalizadorSintactico:
    """Analizador sintáctico que procesa tokens según el conjunto de predicciones LL(1)."""

    def __init__(
        self,
        predicciones,
        primeros,
        simbolo_inicial=None,
        fin_cadena="final_de_archivo",
        mapa_simbolos=None,
    ):
        self.predicciones = predicciones
        self.primeros = primeros
        self.no_terminales = set(predicciones.keys())
        self.simbolo_inicial = simbolo_inicial or next(iter(predicciones))
        self.fin_cadena = fin_cadena
        self.mapa_simbolos = mapa_simbolos or {}

    def display(self, simbolo):
        """Devuelve la representación legible del símbolo para el usuario."""
        return self.mapa_simbolos.get(simbolo, simbolo)

    def _calcular_esperados(self, cadena):
        """Calcula los terminales válidos esperados dada la cadena de símbolos actual."""
        esperados = set()
        for s in cadena:
            if s not in self.no_terminales:
                esperados.add(s)
                break
            primeros_s = self.primeros.get(s, set())
            esperados.update(primeros_s - {"epsilon"})
            if "epsilon" not in primeros_s:
                break
        else:
            if self.fin_cadena:
                esperados.add(self.fin_cadena)
        return esperados

    def _formatear_error(self, token, cadena):
        """Genera el mensaje de error sintáctico con los tokens esperados."""
        esperados = [self.display(s) for s in sorted(self._calcular_esperados(cadena))]
        lista_esp = ", ".join(f'"{e}"' for e in esperados)
        encontrado = self.display(token.tipo) if token.tipo == self.fin_cadena else token.lexema
        return f'<{token.fila}:{token.columna}> Error sintactico: se encontro: "{encontrado}"; se esperaba: {lista_esp}.'

    def analizar(self, tokens):
        """Ejecuta el análisis sintáctico sobre la lista de tokens."""
        cadena = [self.simbolo_inicial]
        idx = 0

        while cadena:
            simbolo_actual = cadena[0]
            token = tokens[idx]
            tipo = token.tipo

            if simbolo_actual in self.no_terminales:
                if tipo in self.predicciones[simbolo_actual]:
                    produccion = self.predicciones[simbolo_actual][tipo]
                    if produccion == "epsilon":
                        esperados_resto = self._calcular_esperados(cadena[1:]) or {self.fin_cadena}
                        if tipo not in esperados_resto:
                            mensaje = self._formatear_error(token, cadena)
                            print(mensaje)
                            return mensaje
                    cadena.pop(0)
                    cadena = descomponer_produccion(produccion) + cadena
                else:
                    mensaje = self._formatear_error(token, cadena)
                    print(mensaje)
                    return mensaje
            else:
                # Terminal: emparejar
                if simbolo_actual == tipo:
                    cadena.pop(0)
                    idx += 1
                else:
                    mensaje = self._formatear_error(token, cadena)
                    print(mensaje)
                    return mensaje

        mensaje = "El analisis sintactico ha finalizado exitosamente."
        print(mensaje)
        return mensaje
