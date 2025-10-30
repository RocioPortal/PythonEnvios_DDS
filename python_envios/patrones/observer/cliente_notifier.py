"""
Implementación de un Observer concreto.
"""
# --- Local application imports ---
from .observer import Observer
from ...entidades.paquete import Paquete # Importamos Paquete para type hinting

class ClienteNotifier(Observer[Paquete]):
    """
    Un Observer concreto que notifica al cliente sobre el estado del paquete.
    Observa objetos de tipo Paquete.
    """
    def __init__(self, nombre_cliente: str):
        """
        Inicializa el notificador con el nombre del cliente.

        Args:
            nombre_cliente (str): Nombre del cliente a notificar.
        """
        self._nombre_cliente = nombre_cliente

    def actualizar(self, paquete: Paquete) -> None:
        """
        Recibe la notificación del paquete y muestra un mensaje al cliente.

        Args:
            paquete (Paquete): El paquete que ha cambiado de estado.
        """
        print(f"[Notificación para Cliente '{self._nombre_cliente}'] "
              f"El estado de su paquete ID {paquete.get_id()} ha cambiado a: '{paquete.get_estado()}'")

