"""
test_sintactico.py
Ejecuta las pruebas del analizador sintáctico y muestra ÚNICAMENTE los tests que fallaron.
Muestra: Input, Esperado y Obtenido con colores en terminal.

Uso:
    py test_sintactico.py
    py test_sintactico.py 13 14
    py test_sintactico.py --cli
"""

import os
import sys
import io
import subprocess

# Habilitar soporte de colores ANSI en terminales de Windows
os.system("")

# Códigos de color ANSI
COLOR_TEST = "\033[1;36m"      # Cyan brillante
COLOR_INPUT_HDR = "\033[1;33m" # Amarillo brillante
COLOR_EXP_HDR = "\033[1;32m"   # Verde brillante
COLOR_EXP = "\033[92m"         # Verde
COLOR_ACT_HDR = "\033[1;31m"   # Rojo brillante
COLOR_ACT = "\033[91m"         # Rojo
COLOR_OK = "\033[1;92m"        # Verde brillante
COLOR_FAIL = "\033[1;91m"      # Rojo brillante
RESET = "\033[0m"

DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
CARPETA_TESTS = os.path.join(DIRECTORIO_ACTUAL, "tests")

if DIRECTORIO_ACTUAL not in sys.path:
    sys.path.insert(0, DIRECTORIO_ACTUAL)

from analizador_lexico import tokenizador
from analizador_sintactico import AnalizadorSintactico, parsear_gramatica
from conjuntos_de_prediccion import calcular_primeros, conjuntos_de_prediccion
from main import GRAMATICA_TEXTO, MAPA_SIMBOLOS

# Inicializar motor sintáctico en memoria
_gramatica = parsear_gramatica(GRAMATICA_TEXTO)
_primeros = calcular_primeros(_gramatica)
_predicciones = conjuntos_de_prediccion(
    _gramatica,
    simbolo_inicial="CHUNK",
    fin_cadena="final_de_archivo",
    primeros=_primeros
)


def ejecutar_analizador_memoria(codigo: str) -> str:
    analizador = AnalizadorSintactico(
        predicciones=_predicciones,
        primeros=_primeros,
        simbolo_inicial="CHUNK",
        fin_cadena="final_de_archivo",
        mapa_simbolos=MAPA_SIMBOLOS
    )
    tokens = tokenizador(codigo)
    buffer = io.StringIO()
    stdout_original = sys.stdout
    try:
        sys.stdout = buffer
        analizador.analizar(tokens)
    finally:
        sys.stdout = stdout_original
    return buffer.getvalue().strip()


def ejecutar_analizador_cli(codigo: str) -> str:
    script_main = os.path.join(DIRECTORIO_ACTUAL, "main.py")
    proc = subprocess.run(
        [sys.executable, script_main],
        input=codigo,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    return proc.stdout.strip()


def ejecutar_pruebas(filtro_ids=None, modo_cli=False):
    if not os.path.exists(CARPETA_TESTS):
        print(f"{COLOR_FAIL}Error: No existe la carpeta {CARPETA_TESTS}{RESET}")
        return

    archivos_in = sorted([f for f in os.listdir(CARPETA_TESTS) if f.endswith(".in")])
    if filtro_ids:
        archivos_in = [
            f for f in archivos_in
            if any(f.startswith(fid) or f == f"{fid}.in" for fid in filtro_ids)
        ]

    if not archivos_in:
        print(f"{COLOR_FAIL}No se encontraron pruebas.{RESET}")
        return

    total = len(archivos_in)
    fallidos = 0

    for nombre_in in archivos_in:
        test_id = nombre_in[:-3]
        ruta_in = os.path.join(CARPETA_TESTS, nombre_in)
        ruta_out = os.path.join(CARPETA_TESTS, f"{test_id}.out")

        with open(ruta_in, "r", encoding="utf-8") as f:
            input_codigo = f.read()

        esperado = ""
        if os.path.exists(ruta_out):
            with open(ruta_out, "r", encoding="utf-8") as f:
                esperado = f.read().strip()

        if modo_cli:
            obtenido = ejecutar_analizador_cli(input_codigo)
        else:
            obtenido = ejecutar_analizador_memoria(input_codigo)

        # Solo reportar si salio mal
        if obtenido != esperado:
            fallidos += 1
            print(f"{COLOR_TEST}=== Test: {test_id} ==={RESET}")
            print(f"{COLOR_INPUT_HDR}Input:{RESET}")
            # Mostrar input con indentación limpia
            for linea in input_codigo.rstrip("\n").split("\n"):
                print(f"  {linea}")
            print(f"{COLOR_EXP_HDR}Esperado:{RESET}")
            print(f"  {COLOR_EXP}{esperado}{RESET}")
            print(f"{COLOR_ACT_HDR}Obtenido:{RESET}")
            print(f"  {COLOR_ACT}{obtenido}{RESET}")
            print()

    if fallidos == 0:
        print(f"{COLOR_OK}Todos los tests pasaron exitosamente ({total}/{total}).{RESET}")
    else:
        print(f"{COLOR_FAIL}Fallaron {fallidos} de {total} tests.{RESET}")


if __name__ == "__main__":
    args = sys.argv[1:]
    usar_cli = "--cli" in args
    filtros = [a for a in args if not a.startswith("--")]
    ejecutar_pruebas(filtro_ids=filtros if filtros else None, modo_cli=usar_cli)
