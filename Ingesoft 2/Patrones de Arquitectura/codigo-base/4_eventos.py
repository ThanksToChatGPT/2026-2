"""Arquitectura orientada a eventos: publicar y suscribir."""


# ================= BUS DE EVENTOS =================
class Bus:
    def __init__(self):
        self.suscriptores = {}               # evento -> lista de funciones

    def suscribir(self, evento, funcion):
        self.suscriptores.setdefault(evento, []).append(funcion)

    def publicar(self, evento, datos):
        for funcion in self.suscriptores.get(evento, []):
            funcion(datos)


# =================== PRODUCTOR ===================
class ServicioPrestamos:                     # no sabe quién escucha
    def __init__(self, bus):
        self.bus = bus

    def prestar(self, estudiante, titulo):
        print(f"* {estudiante} se lleva '{titulo}'")
        self.bus.publicar("libro_prestado", (estudiante, titulo))


# ================== CONSUMIDORES ==================
def enviar_correo(datos):
    estudiante, titulo = datos
    print(f"   [correo] {estudiante}, recuerda devolver '{titulo}'")


def registrar_auditoria(datos):
    print(f"   [auditoría] préstamo registrado: {datos}")


bus = Bus()
bus.suscribir("libro_prestado", enviar_correo)
bus.suscribir("libro_prestado", registrar_auditoria)

servicio = ServicioPrestamos(bus)
servicio.prestar("ana", "Clean Architecture")
