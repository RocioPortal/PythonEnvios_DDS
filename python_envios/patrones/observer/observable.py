"""
Implementación de la clase base Observable (Subject) del Patrón Observer.
Utiliza Generics de Python (TypeVar) para ser tipo-seguro.
"""

# --- Standard library imports ---
from abc import ABC
from typing import Generic, TypeVar, List

# --- Local application imports ---
from .observer import Observer

# --- Type variables ---
T = TypeVar('T') # Tipo genérico para el dato del evento

class Observable(Generic[T], ABC):
    """
    Clase base abstracta para objetos que pueden ser observados (Subject).
    Mantiene una lista de observadores y les notifica de eventos.

    Attributes:
        _observadores (List[Observer[T]]): Lista de observadores suscritos.
    """
    def __init__(self):
        """Inicializa la lista de observadores."""
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Agrega un observador a la lista si no está ya presente.

        Args:
            observador (Observer[T]): El observador a agregar.
        """
        if observador not in self._observadores:
            self._observadores.append(observador)
            print(f"DEBUG (Observable): {observador.__class__.__name__} suscrito a {self.__class__.__name__}")

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Quita un observador de la lista.

        Args:
            observador (Observer[T]): El observador a quitar.
        """
        try:
            self._observadores.remove(observador)
        except ValueError:
            print(f"Advertencia: Intento de eliminar observador no suscrito: {observador}")


    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores suscritos sobre un nuevo evento.

        Args:
            evento (T): El dato o evento a notificar.
        """
        for observador in self._observadores:
            try:
                observador.actualizar(evento)
            except Exception as e:
                print(f"Error al notificar al observador {observador.__class__.__name__}: {e}")

