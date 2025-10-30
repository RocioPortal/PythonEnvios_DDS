"""
Define la entidad principal Paquete.
Esta entidad también actúa como un 'Observable' (Sujeto) en el patrón Observer.
"""

# --- Standard library imports ---
from typing import TYPE_CHECKING, Optional

# --- Local application imports ---
from ..patrones.observer.observable import Observable

if TYPE_CHECKING:
    from .vehiculo import Vehiculo

class Paquete(Observable['Paquete']):
    """
    Representa un paquete que debe ser enviado.
    Hereda de Observable para poder notificar a los suscriptores
    (como ClienteNotifier o SistemaRastreoGlobal) sobre cambios de estado.
    """
    
    # Variable de clase para autoincrementar el ID de forma única
    _counter: int = 0

    def __init__(self, origen: str, destino: str, peso_kg: float):
        """
        Inicializa un nuevo paquete.

        Args:
            origen (str): Dirección de origen.
            destino (str): Dirección de destino.
            peso_kg (float): Peso del paquete en kilogramos.
        """
        super().__init__() # Llama al __init__ de Observable
        
        # --- CORRECCIÓN AQUÍ ---
        # Usamos _counter, no _id_counter
        Paquete._counter += 1
        self._id: int = Paquete._counter
        
        self._origen: str = origen
        self._destino: str = destino
        self._peso_kg: float = peso_kg
        self._estado: str = "Registrado"
        self._vehiculo_asignado: Optional['Vehiculo'] = None

    def get_id(self) -> int:
        return self._id

    def get_peso_kg(self) -> float:
        return self._peso_kg

    def get_estado(self) -> str:
        return self._estado
        
    def get_origen(self) -> str:
        return self._origen

    def get_destino(self) -> str:
        return self._destino
        
    def get_vehiculo(self) -> Optional['Vehiculo']:
        return self._vehiculo_asignado

    def set_vehiculo(self, vehiculo: 'Vehiculo') -> None:
        """Asigna un vehículo al paquete."""
        self._vehiculo_asignado = vehiculo

    def set_estado(self, nuevo_estado: str) -> None:
        """
        Actualiza el estado del paquete y notifica a todos los observadores.
        Este es el "gatillo" del patrón Observer.
        """
        if self._estado != nuevo_estado:
            self._estado = nuevo_estado
            print(f"\n---> (Paquete {self._id}): Estado cambiado a '{self._estado}' <---")
            # Notifica a todos los suscriptores (ClienteNotifier, SistemaRastreoGlobal)
            self.notificar_observadores(self)

    def __str__(self) -> str:
        return f"Paquete ID {self._id} ({self._peso_kg}kg) | {self._estado}"

