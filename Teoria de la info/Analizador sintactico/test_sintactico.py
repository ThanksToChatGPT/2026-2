"""
Script de pruebas automatizado para el analizador sintáctico.
Ejecuta cada archivo .in a través de stdin y compara con .out.
"""

import glob
import subprocess
import sys


def ejecutar_pruebas():
    archivos = sorted(glob.glob("tests/*.in"))
    pasadas = 0
    falladas = 0

    print(f"Ejecutando {len(archivos)} pruebas...\n")

    for f_in in archivos:
        base = f_in[:-3]
        f_out = base + ".out"

        with open(f_in, "r", encoding="utf-8") as f:
            entrada = f.read()

        with open(f_out, "r", encoding="utf-8") as f:
            esperado = f.read().strip()

        proc = subprocess.run(
            [sys.executable, "main.py"],
            input=entrada,
            text=True,
            capture_output=True,
            encoding="utf-8"
        )

        salida = proc.stdout.strip()

        if salida == esperado:
            print(f"[\u2714 PASS] {base}")
            pasadas += 1
        else:
            print(f"[\u2718 FAIL] {base}")
            print(f"   Esperado: {esperado}")
            print(f"   Obtenido: {salida}")
            if proc.stderr:
                print(f"   Stderr:   {proc.stderr.strip()}")
            falladas += 1

    print(f"\nResumen: {pasadas} pasadas, {falladas} falladas.")
    return falladas == 0


if __name__ == "__main__":
    exito = ejecutar_pruebas()
    sys.exit(0 if exito else 1)

