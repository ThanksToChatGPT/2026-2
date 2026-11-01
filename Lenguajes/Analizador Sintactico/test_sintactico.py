"""
test_sintactico.py
Ejecuta las pruebas del analizador sintáctico a partir de 'tests/tests.txt'
y muestra ÚNICAMENTE los tests que fallaron.
Muestra: Input, Esperado y Obtenido con colores en terminal.

Uso:
    py test_sintactico.py
    py test_sintactico.py 13 14
    py test_sintactico.py "campuswire 1" "campuswire 2"
    py test_sintactico.py --cli
    py test_sintactico.py --file ruta/a/tests.txt
"""

import os
import sys
import io
import re
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
ARCHIVO_TESTS_DEFECTO = os.path.join(DIRECTORIO_ACTUAL, "tests", "tests.txt")
if not os.path.exists(ARCHIVO_TESTS_DEFECTO):
    _alt = os.path.join(DIRECTORIO_ACTUAL, "tests.txt")
    if os.path.exists(_alt):
        ARCHIVO_TESTS_DEFECTO = _alt

if DIRECTORIO_ACTUAL not in sys.path:
    sys.path.insert(0, DIRECTORIO_ACTUAL)

from analizador_lexico import tokenizador
from analizador_sintactico import AnalizadorSintactico, parsear_gramatica
from conjuntos_de_prediccion import calcular_primeros, conjuntos_de_prediccion
from main import GRAMATICA_TEXTO, MAPA_SIMBOLOS

# Inicializar motor sintáctico en memoria
_gramatica = parsear_gramatica(GRAMATICA_TEXTO)
_simbolo_inicial = next(iter(_gramatica)) if _gramatica else "chunk"
_primeros = calcular_primeros(_gramatica)
_predicciones = conjuntos_de_prediccion(
    _gramatica,
    simbolo_inicial=_simbolo_inicial,
    fin_cadena="final_de_archivo",
    primeros=_primeros
)


def cargar_pruebas(ruta_archivo: str) -> list[dict]:
    """
    Carga pruebas desde un archivo de texto unificado.
    Soporta bloques con encabezados de ID (ej. '=== 01 ===' o '# Test 01')
    y secciones 'Entrada:' y 'Salida:'.
    """
    if not os.path.exists(ruta_archivo):
        return []

    with open(ruta_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    pruebas = []
    lineas = contenido.splitlines()

    id_actual = None
    modo = None  # None, 'entrada', 'salida'
    lineas_entrada = []
    lineas_salida = []
    contador_auto = 1

    def guardar_prueba_actual():
        nonlocal id_actual, modo, lineas_entrada, lineas_salida, contador_auto
        if lineas_entrada or lineas_salida:
            nombre = id_actual if id_actual else f"{contador_auto:02d}"
            entrada_str = "\n".join(lineas_entrada).rstrip("\r\n")
            salida_str = "\n".join(lineas_salida).strip()
            if entrada_str.strip() or salida_str:
                pruebas.append({
                    "id": nombre,
                    "entrada": entrada_str,
                    "esperado": salida_str
                })
                contador_auto += 1
        id_actual = None
        modo = None
        lineas_entrada = []
        lineas_salida = []

    for linea in lineas:
        linea_strip = linea.strip()

        # Separador de test tipo: === 01 === o --- test_name ---
        m_sep = re.match(r"^[=\-]{3,}\s*(?:Test\s*:?\s*)?(.*?)\s*[=\-]{3,}$", linea_strip, re.IGNORECASE)
        if m_sep:
            guardar_prueba_actual()
            nombre_capturado = m_sep.group(1).strip()
            if nombre_capturado:
                id_actual = nombre_capturado
            continue

        # Encabezado Entrada:
        if re.match(r"^Entrada\s*:", linea_strip, re.IGNORECASE):
            if modo == "salida":
                guardar_prueba_actual()
            modo = "entrada"
            resto = linea_strip.split(":", 1)[1].strip()
            if resto:
                lineas_entrada.append(resto)
            continue

        # Encabezado Salida:
        if re.match(r"^Salida\s*:", linea_strip, re.IGNORECASE):
            modo = "salida"
            resto = linea_strip.split(":", 1)[1].strip()
            if resto:
                lineas_salida.append(resto)
            continue

        if modo == "entrada":
            lineas_entrada.append(linea)
        elif modo == "salida":
            lineas_salida.append(linea)

    guardar_prueba_actual()
    return pruebas


def ejecutar_analizador_memoria(codigo: str) -> str:
    analizador = AnalizadorSintactico(
        predicciones=_predicciones,
        primeros=_primeros,
        simbolo_inicial=_simbolo_inicial,
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


def ejecutar_pruebas(filtro_ids=None, modo_cli=False, ruta_tests=None):
    ruta_archivo = ruta_tests or ARCHIVO_TESTS_DEFECTO

    if not os.path.exists(ruta_archivo):
        print(f"{COLOR_FAIL}Error: No existe el archivo de tests: {ruta_archivo}{RESET}")
        return

    pruebas = cargar_pruebas(ruta_archivo)

    if filtro_ids:
        pruebas = [
            p for p in pruebas
            if any(p["id"] == fid or p["id"].startswith(fid) for fid in filtro_ids)
        ]

    if not pruebas:
        print(f"{COLOR_FAIL}No se encontraron pruebas para ejecutar.{RESET}")
        return

    total = len(pruebas)
    fallidos = 0

    for prueba in pruebas:
        test_id = prueba["id"]
        input_codigo = prueba["entrada"]
        esperado = prueba["esperado"]

        if modo_cli:
            obtenido = ejecutar_analizador_cli(input_codigo)
        else:
            obtenido = ejecutar_analizador_memoria(input_codigo)

        # Solo reportar si salio mal
        if obtenido != esperado:
            fallidos += 1
            print(f"{COLOR_TEST}=== Test: {test_id} ==={RESET}")
            print(f"{COLOR_INPUT_HDR}Input:{RESET}")
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

    ruta_custom = None
    if "--file" in args:
        idx = args.index("--file")
        if idx + 1 < len(args):
            ruta_custom = args[idx + 1]
            args = args[:idx] + args[idx + 2:]
        else:
            args = args[:idx]

    filtros = [a for a in args if not a.startswith("--")]
    ejecutar_pruebas(filtro_ids=filtros if filtros else None, modo_cli=usar_cli, ruta_tests=ruta_custom)