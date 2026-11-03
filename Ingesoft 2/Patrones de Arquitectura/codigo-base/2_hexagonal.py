"""Arquitectura hexagonal: el núcleo define puertos; afuera, adaptadores."""
from abc import ABC, abstractmethod


# ==================== NÚCLEO ====================
class Notificador(ABC):                    # PUERTO: lo que el núcleo necesita
    @abstractmethod
    def enviar(self, estudiante, mensaje): ...


class ServicioPrestamos:                   # reglas del negocio
    def __init__(self, notificador: Notificador):
        self.notificador = notificador

    def prestar(self, estudiante, titulo):
        self.notificador.enviar(estudiante, f"Te prestamos '{titulo}'")


# ================= ADAPTADORES =================
class NotificadorConsola(Notificador):     # ADAPTADOR: una forma de cumplirlo
    def enviar(self, estudiante, mensaje):
        print(f"[consola] para {estudiante}: {mensaje}")


# ===== Aquí se escoge qué adaptador usar =====
servicio = ServicioPrestamos(NotificadorConsola())
servicio.prestar("ana", "Clean Architecture")
servicio.prestar("luis", "Refactoring")
