"""
Módulo: conjuntos_de_prediccion.py
Calcula los conjuntos PRIMEROS, SIGUIENTES y las predicciones
para cualquier GIC.
"""


def descomponer_produccion(produccion):
    """Divide una producción en sus símbolos individuales, omitiendo epsilon."""
    return [s for s in produccion.strip().split() if s != "epsilon"]


def primeros_de_secuencia(secuencia, primeros, no_terminales):
    """Calcula el conjunto PRIMEROS de una secuencia de símbolos."""
    if not secuencia:
        return {"epsilon"}

    resultado = set()
    for simbolo in secuencia:
        if simbolo not in no_terminales:
            resultado.add(simbolo)
            return resultado

        primeros_simbolo = primeros.get(simbolo, set())
        resultado.update(primeros_simbolo - {"epsilon"})
        if "epsilon" not in primeros_simbolo:
            return resultado

    resultado.add("epsilon")
    return resultado


def calcular_primeros(gramatica):
    """Calcula los conjuntos PRIMEROS para cada no terminal de la gramática."""
    no_terminales = set(gramatica.keys())
    primeros = {nt: set() for nt in no_terminales}

    cambio = True
    while cambio:
        cambio = False
        for nt, producciones in gramatica.items():
            for prod in producciones:
                simbolos = descomponer_produccion(prod)
                f = primeros_de_secuencia(simbolos, primeros, no_terminales)
                if not f.issubset(primeros[nt]):
                    primeros[nt].update(f)
                    cambio = True

    return primeros


def calcular_siguientes(gramatica, primeros, simbolo_inicial=None, fin_cadena="$"):
    """Calcula los conjuntos SIGUIENTES para cada no terminal de la gramática."""
    no_terminales = set(gramatica.keys())
    if simbolo_inicial is None:
        simbolo_inicial = next(iter(gramatica))

    siguientes = {nt: set() for nt in no_terminales}
    siguientes[simbolo_inicial].add(fin_cadena)

    cambio = True
    while cambio:
        cambio = False
        for nt, producciones in gramatica.items():
            for prod in producciones:
                simbolos = descomponer_produccion(prod)
                for i, simbolo in enumerate(simbolos):
                    if simbolo in no_terminales:
                        resto = simbolos[i + 1:]
                        f_resto = primeros_de_secuencia(resto, primeros, no_terminales)

                        term_resto = f_resto - {"epsilon"}
                        if not term_resto.issubset(siguientes[simbolo]):
                            siguientes[simbolo].update(term_resto)
                            cambio = True

                        if "epsilon" in f_resto:
                            if not siguientes[nt].issubset(siguientes[simbolo]):
                                siguientes[simbolo].update(siguientes[nt])
                                cambio = True

    return siguientes


def conjuntos_de_prediccion(gramatica, simbolo_inicial=None, fin_cadena="$", primeros=None):
    """
    Construye las predicciones LL(1) en formato:
        {no_terminal: {terminal: produccion}}
    """
    if simbolo_inicial is None:
        simbolo_inicial = next(iter(gramatica))

    if primeros is None:
        primeros = calcular_primeros(gramatica)

    siguientes = calcular_siguientes(gramatica, primeros, simbolo_inicial, fin_cadena)
    no_terminales = set(gramatica.keys())
    predicciones = {nt: {} for nt in gramatica}

    for nt, producciones in gramatica.items():
        for prod in producciones:
            simbolos = descomponer_produccion(prod)
            f = primeros_de_secuencia(simbolos, primeros, no_terminales)

            cp = f - {"epsilon"}
            if "epsilon" in f:
                cp = cp | siguientes[nt]

            for terminal in sorted(cp):
                predicciones[nt][terminal] = prod

    return predicciones
