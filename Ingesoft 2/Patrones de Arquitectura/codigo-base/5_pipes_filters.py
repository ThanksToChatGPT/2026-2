"""Tuberías y filtros: reporte de libros atrasados."""

PRESTAMOS = [
    {"estudiante": "ana", "titulo": "Clean Architecture", "dias": 3},
    {"estudiante": "marta", "titulo": "Design Patterns", "dias": 17},
    {"estudiante": "luis", "titulo": "Refactoring", "dias": 20},
]


# ===== FILTROS: cada uno recibe una lista y devuelve otra =====
def solo_atrasados(prestamos):              # más de 14 días
    return [p for p in prestamos if p["dias"] > 14]


def calcular_multa(prestamos):              # $500 por día de atraso
    return [{**p, "multa": (p["dias"] - 14) * 500} for p in prestamos]


def formatear(prestamos):
    return [f"{p['estudiante']}: {p['titulo']} -> ${p['multa']}"
            for p in prestamos]


# ===== TUBERÍA: pasa los datos por los filtros, en orden =====
def tuberia(datos, filtros):
    for filtro in filtros:
        datos = filtro(datos)
    return datos


for linea in tuberia(PRESTAMOS, [solo_atrasados, calcular_multa, formatear]):
    print(linea)
