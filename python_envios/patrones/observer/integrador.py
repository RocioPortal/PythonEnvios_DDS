"""
Archivo integrador generado automaticamente
Directorio: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\observer
Fecha: 2025-11-04 19:55:50
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\observer\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: cliente_notifier.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\observer\cliente_notifier.py
# ================================================================================

"""
Implementación de un Observer concreto.
"""
from .observer import Observer
from ...entidades.paquete import Paquete 

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



# ================================================================================
# ARCHIVO 3/4: observable.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\observer\observable.py
# ================================================================================

"""
Implementación de la clase base Observable (Subject) del Patrón Observer.
Utiliza Generics de Python (TypeVar) para ser tipo-seguro.
"""
from abc import ABC
from typing import Generic, TypeVar, List
from .observer import Observer

T = TypeVar('T') 

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



# ================================================================================
# ARCHIVO 4/4: observer.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\observer\observer.py
# ================================================================================

"""
Implementación de la interfaz Observer (ABC) del Patrón Observer.
Utiliza Generics de Python (TypeVar) para ser tipo-seguro.
"""
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T') 

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



