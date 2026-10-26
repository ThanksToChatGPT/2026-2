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

        if "->" in linea:
            partes = linea.split("->", 1)
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
    """Analizador sintáctico que procesa tokens según el conjunto de predicciones."""

    def __init__(
        self,
        predicciones,
        primeros=None,
        simbolo_inicial=None,
        fin_cadena="$",
        mapa_simbolos=None,
    ):
        self.predicciones = predicciones
        self.no_terminales = set(predicciones.keys())
        self.simbolo_inicial = simbolo_inicial if simbolo_inicial is not None else next(iter(predicciones))
        self.fin_cadena = fin_cadena
        self.mapa_simbolos = mapa_simbolos or {}
        self.primeros = primeros
    

    def display(self, simbolo):
        """Devuelve la representación legible del símbolo según el mapa configurado."""
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
        return esperados

    def _formatear_error(self, token, cadena):
        """Genera el mensaje de error sintáctico."""
        esperados = [self.display(s) for s in sorted(self._calcular_esperados(cadena))]
        lista_esp = ", ".join(f'"{e}"' for e in esperados)
        tipo = getattr(token, "tipo", str(token))
        lexema = getattr(token, "lexema", str(token))
        fila = getattr(token, "fila", 1)
        columna = getattr(token, "columna", 1)

        encontrado = self.display(tipo) if tipo == self.fin_cadena else lexema
        return f'<{fila}:{columna}> Error sintactico: se encontro: "{encontrado}"; se esperaba: {lista_esp}.'

    def analizar(self, tokens):
        """Ejecuta el análisis sintáctico sobre una secuencia de tokens."""
        cadena = [self.simbolo_inicial]
        idx = 0

        while cadena:
            simbolo_actual = cadena[0]
            token = tokens[idx]
            tipo = getattr(token, "tipo", str(token))

            if simbolo_actual in self.no_terminales:
                if tipo in self.predicciones[simbolo_actual]:
                    cadena.pop(0)
                    produccion = self.predicciones[simbolo_actual][tipo]
                    simbolos_nuevos = descomponer_produccion(produccion)
                    cadena = simbolos_nuevos + cadena
                else:
                    mensaje = self._formatear_error(token, cadena)
                    print(mensaje, end="")
                    return mensaje
            else:
                # Terminal: emparejar
                if simbolo_actual == tipo:
                    cadena.pop(0)
                    idx += 1
                else:
                    mensaje = self._formatear_error(token, cadena)
                    print(mensaje, end="")
                    return mensaje

        mensaje = "El analisis sintactico ha finalizado exitosamente."
        print(mensaje)
        return mensaje
