"""Arquitectura en capas: préstamos de la Biblioteca UN."""


# ================== Capa de datos ==================
class RepositorioLibros:
    def __init__(self):
        self.libros = {"L1": "Clean Architecture", "L2": "Refactoring"}
        self.prestados = set()


# ================= Capa de negocio =================
class ServicioPrestamos:
    def __init__(self, repo):
        self.repo = repo

    def prestar(self, codigo):
        if codigo not in self.repo.libros:
            return "Ese libro no existe"
        if codigo in self.repo.prestados:
            return "Ese libro ya está prestado"
        self.repo.prestados.add(codigo)
        return f"Prestado: {self.repo.libros[codigo]}"


# =============== Capa de presentación ===============
class Consola:
    def __init__(self, servicio):
        self.servicio = servicio

    def ejecutar(self, accion, codigo):
        if accion == "prestar":
            print(self.servicio.prestar(codigo))


consola = Consola(ServicioPrestamos(RepositorioLibros()))
consola.ejecutar("prestar", "L1")
consola.ejecutar("prestar", "L1")
consola.ejecutar("prestar", "L9")
