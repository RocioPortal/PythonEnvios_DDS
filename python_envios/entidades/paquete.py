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

# CORRECCIÓN 1: Se usa un string "Paquete" para el type hint
# para evitar un 'NameError' de referencia circular (forward reference)
# ya que la clase Paquete aún no está completamente definida en este punto.
class Paquete(Observable["Paquete"]):
    """
    Representa un paquete que debe ser enviado.
    Hereda de Observable para poder notificar a los suscriptores
    (como ClienteNotifier o SistemaRastreoGlobal) sobre cambios de estado.

    Attributes:
        _counter (int): Variable de clase estática para autoincrementar el ID.
    """
    
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
        
        # --- CORRECCIÓN 2 ---
        # El error estaba aquí. Se debe usar '._counter' para coincidir
        # con la variable de clase definida arriba.
        Paquete._counter += 1
        self._id: int = Paquete._counter
        
        self._origen: str = origen
        self._destino: str = destino
        self._peso_kg: float = peso_kg
        self._estado: str = "Registrado"
        self._vehiculo_asignado: Optional['Vehiculo'] = None

    def get_id(self) -> int:
        """Retorna el ID único del paquete."""
        return self._id

    def get_peso_kg(self) -> float:
        """Retorna el peso del paquete."""
        return self._peso_kg

    def get_estado(self) -> str:
        """Retorna el estado actual del envío (ej. "Registrado")."""
        return self._estado
        
    def get_origen(self) -> str:
        """Retorna la dirección de origen."""
        return self._origen

    def get_destino(self) -> str:
        """Retorna la dirección de destino."""
        return self._destino
        
    def get_vehiculo(self) -> Optional['Vehiculo']:
        """Retorna el vehículo asignado a este paquete."""
        return self._vehiculo_asignado

    def set_vehiculo(self, vehiculo: 'Vehiculo') -> None:
        """Asigna un vehículo al paquete."""
        self._vehiculo_asignado = vehiculo

    def set_estado(self, nuevo_estado: str) -> None:
        """
        Actualiza el estado del paquete y notifica a todos los observadores.
        Este es el "gatillo" del patrón Observer.

        Args:
            nuevo_estado (str): El nuevo estado (ej. "En Tránsito").
        """
        if self._estado != nuevo_estado:
            self._estado = nuevo_estado
            print(f"\n---> (Paquete {self._id}): Estado cambiado a '{self._estado}' <---")
            # Notifica a todos los suscriptores (ClienteNotifier, SistemaRastreoGlobal)
            self.notificar_observadores(self)

    def __str__(self) -> str:
        """Retorna una representación en string del paquete."""
        return f"Paquete ID {self._id} ({self._peso_kg}kg) | {self._estado}"

