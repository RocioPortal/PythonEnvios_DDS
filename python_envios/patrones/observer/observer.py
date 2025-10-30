"""
Implementación de la interfaz Observer (ABC) del Patrón Observer.
Utiliza Generics de Python (TypeVar) para ser tipo-seguro.
"""

# --- Standard library imports ---
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

# --- Type variables ---
T = TypeVar('T') # Tipo genérico para el dato del evento

class Observer(Generic[T], ABC):
    """
    Interfaz abstracta para los Observadores.
    Define el método 'actualizar' que será llamado por el Observable.
    """
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método llamado por el Observable cuando ocurre un evento.

        Args:
            evento (T): El dato o evento notificado por el Observable.
        """
        pass

