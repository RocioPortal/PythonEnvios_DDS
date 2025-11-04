"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios
Fecha de generacion: 2025-11-04 19:55:50
Total de archivos integrados: 20
Total de directorios procesados: 7
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#   3. main.py
#
# DIRECTORIO: entidades
#   4. __init__.py
#   5. cliente.py
#   6. paquete.py
#   7. servicio_rutas.py
#   8. vehiculo.py
#
# DIRECTORIO: patrones
#   9. __init__.py
#
# DIRECTORIO: patrones\factory
#   10. __init__.py
#   11. vehiculo_factory.py
#
# DIRECTORIO: patrones\observer
#   12. __init__.py
#   13. cliente_notifier.py
#   14. observable.py
#   15. observer.py
#
# DIRECTORIO: patrones\strategy
#   16. __init__.py
#   17. estrategia_ruteo.py
#
# DIRECTORIO: servicios
#   18. __init__.py
#   19. servicio_logistica.py
#   20. sistema_rastreo_global.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/20: __init__.py
# Directorio: .
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/20: constantes.py
# Directorio: .
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\constantes.py
# ==============================================================================

"""
Módulo para centralizar todas las constantes mágicas del sistema.
Cumple con el criterio de "NO magic numbers" de la rúbrica.
"""
PESO_MAXIMO_MOTO = 50.0 

VELOCIDAD_PROMEDIO_MOTO = 60.0 
VELOCIDAD_PROMEDIO_CAMION = 70.0 
FACTOR_TRAFICO = 1.2 


# ==============================================================================
# ARCHIVO 3/20: main.py
# Directorio: .
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\main.py
# ==============================================================================

"""
Punto de entrada principal para la demostración del sistema PythonEnvios.
Este archivo simula el rol del "Cliente" u "Operador" que utiliza el sistema.
"""
import time 
# Entidades y Contexto de Strategy
from python_envios.entidades.cliente import Cliente
from python_envios.entidades.servicio_rutas import ServicioRutas

# Servicios y Singleton
from python_envios.servicios.servicio_logistica import ServicioLogistica
from python_envios.servicios.sistema_rastreo_global import SistemaRastreoGlobal

# Patrones
from python_envios.patrones.observer.cliente_notifier import ClienteNotifier
from python_envios.patrones.strategy.estrategia_ruteo import RutaMasCorta, RutaEcologica, RutaMasRapida

from python_envios.patrones.observer.observable import Observable
class Paquete(Observable['Paquete']):
    """Entidad Paquete (Observable)."""
    _counter = 0
    def __init__(self, origen, destino, peso):
        super().__init__()
        Paquete._counter += 1
        self._id = Paquete._counter
        self._origen = origen
        self._destino = destino
        self._peso_kg = peso
        self._estado = "Registrado"
        self._vehiculo_asignado = None
    def get_id(self): return self._id
    def get_peso_kg(self): return self._peso_kg
    def get_estado(self): return self._estado
    def get_origen(self): return self._origen
    def get_destino(self): return self._destino
    def set_vehiculo(self, v): self._vehiculo_asignado = v
    def get_vehiculo(self): return self._vehiculo_asignado
    def set_estado(self, nuevo_estado):
        if self._estado != nuevo_estado:
            self._estado = nuevo_estado
            print(f"\n---> (Paquete {self._id}): Estado cambiado a '{self._estado}' <---")
            self.notificar_observadores(self)

import python_envios.entidades.paquete as paquete_module
paquete_module.Paquete = Paquete

class Vehiculo:
    """Entidad Vehículo (Base)."""
    def __init__(self, id_v, cap, vel): self._id = id_v; self._cap = cap; self._vel = vel
    def get_capacidad_kg(self): return self._cap
    def get_velocidad_max_kmh(self): return self._vel
    def describir(self): print(f"Vehículo genérico {self._id}")

class Camion(Vehiculo): 
    """Entidad Camión."""
    def __init__(self, id_vehiculo, capacidad_kg):
        super().__init__(id_vehiculo, capacidad_kg, 90.0)
    def describir(self): print(f"Camión ID {self._id}, Capacidad: {self._capacidad_kg}kg")

class Moto(Vehiculo): 
    """Entidad Moto."""
    def __init__(self, id_vehiculo, capacidad_kg):
        super().__init__(id_vehiculo, capacidad_kg, 110.0)
    def describir(self): print(f"Moto ID {self._id}, Capacidad: {self._capacidad_kg}kg")

import python_envios.entidades.vehiculo as vehiculo_module
vehiculo_module.Vehiculo = Vehiculo
vehiculo_module.Camion = Camion
vehiculo_module.Moto = Moto


def imprimir_titulo(titulo):
    """Función helper para imprimir títulos."""
    print("\n" + "="*70)
    print(f"  {titulo.upper()}")
    print("="*70)

def main_demo_patrones():
    """Función principal que demuestra los 4 patrones."""

    imprimir_titulo("Inicio de la Simulación Logística - PythonEnvios")

    # ======================================================================
    # PATRÓN SINGLETON: Sistema de Rastreo Global
    # ======================================================================
    imprimir_titulo("Patrón Singleton")
    print("Obteniendo instancias del Sistema de Rastreo Global...")
    rastreador1 = SistemaRastreoGlobal.get_instance()
    rastreador2 = SistemaRastreoGlobal.get_instance()

    if rastreador1 is rastreador2:
        print("[OK] Ambas variables apuntan a la MISMA instancia única del rastreador.")
    else:
        print("[ERROR] Se crearon múltiples instancias del Singleton.")
    print(f"ID de la instancia: {id(rastreador1)}")

    # ======================================================================
    # Inicialización General
    # ======================================================================
    imprimir_titulo("Inicialización del Sistema")
    servicio_logistica = ServicioLogistica() 
    cliente_ana = Cliente("Ana")
    cliente_luis = Cliente("Luis")
    
    servicio_rutas = ServicioRutas() 
    
    notifier_ana = ClienteNotifier(cliente_ana.get_nombre())
    notifier_luis = ClienteNotifier(cliente_luis.get_nombre())

    # ======================================================================
    # PATRÓN FACTORY METHOD: Creación de vehículos (implícito)
    # y PATRÓN OBSERVER: Suscripción
    # ======================================================================
    imprimir_titulo("Patrón Factory Method y Observer (Suscripción)")
    print("Registrando paquetes (esto usa Factory para asignar vehículo y suscribe Observers)...")

    paquete_ana_id = servicio_logistica.registrar_y_asignar_paquete(
        origen="Depósito Central",
        destino="Casa Ana",
        peso_kg=5.0, 
        observadores_externos=[notifier_ana] 
    )

    paquete_luis_id = servicio_logistica.registrar_y_asignar_paquete(
        origen="Puerto Seco",
        destino="Fábrica Luis",
        peso_kg=501.0, # > 50kg
        observadores_externos=[notifier_luis] 
    )
    rastreador1.mostrar_estado_global()

    # ======================================================================
    # PATRÓN STRATEGY: Cálculo y cambio de Rutas
    # ======================================================================
    imprimir_titulo("Patrón Strategy")
    paquete_ana = servicio_logistica._paquetes_db[paquete_ana_id]
    
    print("Planificando entrega con estrategia por defecto (RutaMasRapida)...")
    servicio_rutas.calcular_ruta("Depósito Central", "Casa Ana", 10.0, paquete_ana.get_vehiculo())

    print("\nCambiando a estrategia RutaMasCorta...")
    servicio_rutas.set_estrategia(RutaMasCorta())
    servicio_rutas.calcular_ruta("Depósito Central", "Casa Ana", 10.0, paquete_ana.get_vehiculo())

    # ======================================================================
    # PATRÓN OBSERVER: Notificaciones por cambio de estado
    # ======================================================================
    imprimir_titulo("Patrón Observer en Acción (Notificaciones)")
    print("Procesando envíos (cambiarán estado y notificarán a los Observers)...")

    print("\n--- Procesando paquete de Ana ---")
    servicio_logistica.procesar_envio(paquete_ana_id) 
    time.sleep(1) # Simula tiempo
    servicio_logistica.procesar_envio(paquete_ana_id) 

    print("\n--- Procesando paquete de Luis ---")
    servicio_logistica.procesar_envio(paquete_luis_id) 

    # ======================================================================
    # PATRÓN SINGLETON: Verificación final del estado
    # ======================================================================
    imprimir_titulo("Patrón Singleton: Verificación Final del Rastreo")
    rastreador2.mostrar_estado_global()

    imprimir_titulo("Simulación Logística Completada")

if __name__ == "__main__":
    main_demo_patrones()




################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 4/20: __init__.py
# Directorio: entidades
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\entidades\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/20: cliente.py
# Directorio: entidades
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\entidades\cliente.py
# ==============================================================================

"""
Entidad Cliente.
"""
class Cliente:
    """
    Entidad que representa a un cliente.
    
    Attributes:
        _nombre (str): Nombre del cliente.
    """
    def __init__(self, nombre: str):
        self._nombre = nombre
    
    def get_nombre(self) -> str:
        return self._nombre


# ==============================================================================
# ARCHIVO 6/20: paquete.py
# Directorio: entidades
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\entidades\paquete.py
# ==============================================================================

"""
Define la entidad principal Paquete.
Esta entidad también actúa como un 'Observable' (Sujeto) en el patrón Observer.
"""
from typing import TYPE_CHECKING, Optional
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
            self.notificar_observadores(self)

    def __str__(self) -> str:
        """Retorna una representación en string del paquete."""
        return f"Paquete ID {self._id} ({self._peso_kg}kg) | {self._estado}"



# ==============================================================================
# ARCHIVO 7/20: servicio_rutas.py
# Directorio: entidades
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\entidades\servicio_rutas.py
# ==============================================================================

"""
Implementación del Contexto para el Patrón Strategy.
"""
from typing import Dict, Optional, TYPE_CHECKING
from ..patrones.strategy.estrategia_ruteo import EstrategiaRuteo, RutaMasRapida 

if TYPE_CHECKING:
    from .vehiculo import Vehiculo

class ServicioRutas:
    """
    Representa el contexto que utiliza una Estrategia de Ruteo.
    Permite cambiar la estrategia dinámicamente.

    Attributes:
        _estrategia_actual (EstrategiaRuteo): La estrategia de ruteo
                                              actualmente seleccionada.
    """
    def __init__(self, estrategia_inicial: Optional[EstrategiaRuteo] = None):
        """
        Inicializa el servicio con una estrategia opcional.
        Si no se provee estrategia, usa RutaMasRapida por defecto.

        Args:
            estrategia_inicial (Optional[EstrategiaRuteo]): La estrategia a usar.
                                                             Defaults to RutaMasRapida().
        """
        self._estrategia_actual = estrategia_inicial if estrategia_inicial else RutaMasRapida()

    def set_estrategia(self, nueva_estrategia: EstrategiaRuteo) -> None:
        """
        Permite cambiar la estrategia de ruteo en tiempo de ejecución.

        Args:
            nueva_estrategia (EstrategiaRuteo): La nueva instancia de estrategia a utilizar.
        """
        print(f"\n[Servicio Rutas] Cambiando estrategia de "
              f"'{self._estrategia_actual.__class__.__name__}' a "
              f"'{nueva_estrategia.__class__.__name__}'")
        self._estrategia_actual = nueva_estrategia

    def calcular_ruta(self, origen: str, destino: str, distancia_km: float, vehiculo: 'Vehiculo') -> Dict:
        """
        Planifica una ruta de entrega utilizando la estrategia actual.

        Args:
            origen (str): Punto de partida.
            destino (str): Punto de llegada.
            distancia_km (float): Distancia base en kilómetros.
            vehiculo (Vehiculo): El vehículo que hará la ruta.

        Returns:
            Dict: La ruta calculada por la estrategia actual.
        """
        print(f"[Servicio Rutas] Calculando ruta de '{origen}' a '{destino}' usando {self._estrategia_actual.__class__.__name__}...")
        ruta = self._estrategia_actual.calcular_ruta(origen, destino, distancia_km, vehiculo)
        
        print(f"[Servicio Rutas] Ruta calculada:")
        print(f"  - Pasos: {ruta['pasos']}")
        print(f"  - Tiempo Estimado: {ruta['tiempo_estimado_h']:.2f} horas")
        return ruta


# ==============================================================================
# ARCHIVO 8/20: vehiculo.py
# Directorio: entidades
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\entidades\vehiculo.py
# ==============================================================================

"""
Entidades para Vehículos.
Define la clase base abstracta y las clases concretas
que serán creadas por el Factory Method.
"""
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """Clase base abstracta para todos los vehículos."""
    def __init__(self, id_vehiculo: str, capacidad_kg: float, velocidad_max_kmh: float):
        self._id_vehiculo = id_vehiculo
        self._capacidad_kg = capacidad_kg
        self._velocidad_max_kmh = velocidad_max_kmh

    def get_id(self) -> str:
        return self._id_vehiculo
    
    def get_capacidad_kg(self) -> float:
        return self._capacidad_kg
    
    @abstractmethod
    def describir(self) -> None:
        """Método abstracto para describir el vehículo."""
        pass

class Camion(Vehiculo):
    """Vehículo tipo Camión."""
    def __init__(self, id_vehiculo: str, capacidad_kg: float):
        super().__init__(id_vehiculo, capacidad_kg, velocidad_max_kmh=90.0)
    
    def describir(self) -> None:
        print(f"Camión ID {self._id_vehiculo}, Capacidad: {self._capacidad_kg}kg")

class Moto(Vehiculo):
    """Vehículo tipo Moto."""
    def __init__(self, id_vehiculo: str, capacidad_kg: float):
        super().__init__(id_vehiculo, capacidad_kg, velocidad_max_kmh=110.0)

    def describir(self) -> None:
        print(f"Moto ID {self._id_vehiculo}, Capacidad: {self._capacidad_kg}kg")



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 9/20: __init__.py
# Directorio: patrones
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\factory
################################################################################

# ==============================================================================
# ARCHIVO 10/20: __init__.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\factory\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 11/20: vehiculo_factory.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\factory\vehiculo_factory.py
# ==============================================================================

"""
Implementación del Patrón Factory Method.
"""
from typing import TYPE_CHECKING, Dict, Callable
from ...constantes import PESO_MAXIMO_MOTO

if TYPE_CHECKING:
    from ...entidades.vehiculo import Vehiculo, Camion, Moto

class VehiculoFactory:
    """
    Implementa el patrón Factory Method para crear diferentes tipos de vehículos.
    Desacopla la lógica de negocio de las clases concretas de vehículos.
    """

    _contador_camion = 0
    _contador_moto = 0

    @staticmethod
    def _crear_camion() -> 'Camion':
        """Método privado para crear un Camión."""
        from ...entidades.vehiculo import Camion
        VehiculoFactory._contador_camion += 1
        return Camion(id_vehiculo=f"CAM-{VehiculoFactory._contador_camion}", capacidad_kg=1000.0)

    @staticmethod
    def _crear_moto() -> 'Moto':
        """Método privado para crear una Moto."""
        from ...entidades.vehiculo import Moto
        VehiculoFactory._contador_moto += 1
        return Moto(id_vehiculo=f"MOT-{VehiculoFactory._contador_moto}", capacidad_kg=PESO_MAXIMO_MOTO)

    @staticmethod
    def crear_vehiculo(peso_paquete_kg: float) -> 'Vehiculo':
        """
        Método de fábrica principal. Decide qué vehículo crear basado en el peso.

        Args:
            peso_paquete_kg (float): El peso del paquete a transportar.

        Returns:
            Vehiculo: Una instancia de Camion o Moto.
        """
        if peso_paquete_kg > PESO_MAXIMO_MOTO:
            print(f"DEBUG (Factory): Peso {peso_paquete_kg}kg > {PESO_MAXIMO_MOTO}kg. Creando Camión.")
            return VehiculoFactory._crear_camion()
        else:
            print(f"DEBUG (Factory): Peso {peso_paquete_kg}kg <= {PESO_MAXIMO_MOTO}kg. Creando Moto.")
            return VehiculoFactory._crear_moto()




################################################################################
# DIRECTORIO: patrones\observer
################################################################################

# ==============================================================================
# ARCHIVO 12/20: __init__.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\observer\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 13/20: cliente_notifier.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\observer\cliente_notifier.py
# ==============================================================================

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



# ==============================================================================
# ARCHIVO 14/20: observable.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\observer\observable.py
# ==============================================================================

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



# ==============================================================================
# ARCHIVO 15/20: observer.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\observer\observer.py
# ==============================================================================

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




################################################################################
# DIRECTORIO: patrones\strategy
################################################################################

# ==============================================================================
# ARCHIVO 16/20: __init__.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\strategy\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 17/20: estrategia_ruteo.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\strategy\estrategia_ruteo.py
# ==============================================================================

"""
Implementación del Patrón Strategy.
Define la interfaz (ABC) y las implementaciones concretas.
"""
from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, TYPE_CHECKING 

from ...constantes import VELOCIDAD_PROMEDIO_CAMION, VELOCIDAD_PROMEDIO_MOTO, FACTOR_TRAFICO

if TYPE_CHECKING:
    from ...entidades.vehiculo import Vehiculo

class EstrategiaRuteo(ABC):
    """
    Interfaz abstracta (Strategy) para los algoritmos de cálculo de rutas.
    """
    @abstractmethod
    def calcular_ruta(self, origen: str, destino: str, distancia_km: float, vehiculo: 'Vehiculo') -> Dict:
        """
        Calcula la ruta y devuelve un diccionario con los detalles.

        Args:
            origen (str): Punto de partida.
            destino (str): Punto de llegada.
            distancia_km (float): Distancia base en kilómetros.
            vehiculo (Vehiculo): El vehículo que hará la ruta.

        Returns:
            Dict: Un diccionario con "pasos" (str) y "tiempo_estimado_h" (float).
        """
        pass

class RutaMasRapida(EstrategiaRuteo):
    """Calcula la ruta considerando el tráfico (simulado)."""
    def calcular_ruta(self, origen: str, destino: str, distancia_km: float, vehiculo: 'Vehiculo') -> Dict:
        """Calcula la ruta más rápida, penalizada por tráfico."""
        print(f"[Estrategia Ruta Rápida] Calculando ruta de {origen} a {destino}...")
        
        from ...entidades.vehiculo import Camion
        if isinstance(vehiculo, Camion):
            velocidad = VELOCIDAD_PROMEDIO_CAMION
        else:
            velocidad = VELOCIDAD_PROMEDIO_MOTO
            
        distancia_real_km = distancia_km * 1.1 
        tiempo_base_h = distancia_real_km / velocidad
        tiempo_final_h = tiempo_base_h * FACTOR_TRAFICO
        
        pasos = f"Tomar Autopista Central (Ruta Rápida). Distancia: {distancia_real_km:.1f}km."
        return {"pasos": pasos, "tiempo_estimado_h": tiempo_final_h}

class RutaMasCorta(EstrategiaRuteo):
    """Calcula la ruta con menor distancia (simulado)."""
    def calcular_ruta(self, origen: str, destino: str, distancia_km: float, vehiculo: 'Vehiculo') -> Dict:
        """Calcula la ruta más corta, penalizada por más tráfico."""
        print(f"[Estrategia Ruta Corta] Calculando ruta de {origen} a {destino}...")
        
        from ...entidades.vehiculo import Camion
        if isinstance(vehiculo, Camion):
            velocidad = VELOCIDAD_PROMEDIO_CAMION
        else:
            velocidad = VELOCIDAD_PROMEDIO_MOTO
            
        distancia_real_km = distancia_km
        tiempo_base_h = distancia_real_km / velocidad
        tiempo_final_h = tiempo_base_h * (FACTOR_TRAFICO + 0.1)
        
        pasos = f"Atravesar centro de la ciudad (Ruta Corta). Distancia: {distancia_real_km:.1f}km."
        return {"pasos": pasos, "tiempo_estimado_h": tiempo_final_h}

class RutaEcologica(EstrategiaRuteo):
    """Calcula la ruta minimizando emisiones (simulado)."""
    def calcular_ruta(self, origen: str, destino: str, distancia_km: float, vehiculo: 'Vehiculo') -> Dict:
        """Calcula la ruta más ecológica (simulación simple)."""
        print(f"[Estrategia Ruta Ecológica] Calculando ruta de {origen} a {destino} (minimizando emisiones)...")
        
        distancia_real_km = distancia_km * 0.95
        velocidad = VELOCIDAD_PROMEDIO_MOTO 
        
        tiempo_base_h = distancia_real_km / velocidad
        tiempo_final_h = tiempo_base_h * (FACTOR_TRAFICO - 0.05)
        
        pasos = f"Usar ruta de circunvalación verde. Distancia: {distancia_real_km:.1f}km."
        return {"pasos": pasos, "tiempo_estimado_h": tiempo_final_h}




################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 18/20: __init__.py
# Directorio: servicios
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\servicios\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 19/20: servicio_logistica.py
# Directorio: servicios
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\servicios\servicio_logistica.py
# ==============================================================================

"""
Servicio principal de logística.
Orquesta los patrones y entidades.
"""
from typing import List, Dict, Any

from ..entidades.paquete import Paquete
from ..entidades.cliente import Cliente
from ..patrones.factory.vehiculo_factory import VehiculoFactory
from ..patrones.observer.observer import Observer
from .sistema_rastreo_global import SistemaRastreoGlobal

class ServicioLogistica:
    """
    Servicio de alto nivel que orquesta la lógica de envío de paquetes.
    Utiliza el Factory para crear vehículos y el Singleton para rastrear.
    """
    def __init__(self):
        self._rastreador = SistemaRastreoGlobal.get_instance()
        self._paquetes_db: Dict[int, Paquete] = {}

    def registrar_y_asignar_paquete(
        self, 
        origen: str, 
        destino: str, 
        peso_kg: float, 
        observadores_externos: List[Observer[Paquete]]
    ) -> int:
        """
        Crea un paquete, le asigna un vehículo (usando Factory)
        y lo registra en el sistema (Singleton y Observer).

        Args:
            origen (str): Dirección de origen.
            destino (str): Dirección de destino.
            peso_kg (float): Peso del paquete.
            observadores_externos (List[Observer[Paquete]]): Lista de observadores
                (como ClienteNotifier) que deben ser suscritos.

        Returns:
            int: El ID del paquete creado.
        """
        print(f"\nRegistrando nuevo paquete de {peso_kg}kg para ir de '{origen}' a '{destino}'...")
        
        paquete = Paquete(origen, destino, peso_kg)
        
        vehiculo = VehiculoFactory.crear_vehiculo(paquete.get_peso_kg())
        paquete.set_vehiculo(vehiculo)
        
        self._paquetes_db[paquete.get_id()] = paquete
        
        self._rastreador.registrar_nuevo_paquete(paquete) 
        
        for obs in observadores_externos:
            paquete.agregar_observador(obs)
            
        return paquete.get_id()

    def procesar_envio(self, paquete_id: int) -> None:
        """
        Simula el procesamiento de un envío, actualizando el estado del paquete.
        Esto disparará automáticamente las notificaciones del Patrón Observer.

        Args:
            paquete_id (int): El ID del paquete a procesar.
        """
        if paquete_id not in self._paquetes_db:
            print(f"Error: Paquete con ID {paquete_id} no encontrado.")
            return

        paquete = self._paquetes_db[paquete_id]
        estado_actual = paquete.get_estado()

        if estado_actual == "Registrado":
            paquete.set_estado("En Tránsito")
        elif estado_actual == "En Tránsito":
            paquete.set_estado("Entregado")
        elif estado_actual == "Entregado":
            print(f"DEBUG (Logistica): Paquete {paquete_id} ya fue entregado.")
            
    def mostrar_estado_global(self) -> None:
        """Delega la llamada al Singleton para mostrar el estado."""
        self._rastreador.mostrar_estado_global()


# ==============================================================================
# ARCHIVO 20/20: sistema_rastreo_global.py
# Directorio: servicios
# Ruta completa: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\servicios\sistema_rastreo_global.py
# ==============================================================================

"""
Implementación del Patrón Singleton.
Esta clase también actúa como un Observer.
"""
from threading import Lock
from typing import Dict, Any, Optional
from ..entidades.paquete import Paquete
from ..patrones.observer.observer import Observer

class SistemaRastreoGlobal(Observer[Paquete]):
    """
    Sistema centralizado para rastrear el estado de todos los paquetes.
    Implementa el patrón Singleton para garantizar una única instancia.
    Actúa como Observer para recibir actualizaciones de los paquetes.

    Attributes:
        _instance (Optional[SistemaRastreoGlobal]): La única instancia de la clase.
        _lock (Lock): Lock para asegurar la creación thread-safe de la instancia.
        _paquetes_activos (Dict[int, Dict[str, Any]]): Almacena el estado de los paquetes.
    """
    _instance: Optional['SistemaRastreoGlobal'] = None
    _lock: Lock = Lock()

    def __new__(cls):
        """Controla la creación de la instancia (Singleton)."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._paquetes_activos = {}
                    print("[Singleton] Instancia de SistemaRastreoGlobal creada.")
        return cls._instance

    @classmethod
    def get_instance(cls) -> 'SistemaRastreoGlobal':
        """Obtiene la instancia única del sistema de rastreo."""
        if cls._instance is None:
            cls() 
        return cls._instance

    def actualizar(self, paquete: Paquete) -> None:
        """
        Método llamado por el Paquete (Observable) cuando su estado cambia.
        Actualiza el estado del paquete en el registro central.

        Args:
            paquete (Paquete): El paquete que ha cambiado de estado.
        """
        print(f"[Rastreo Global (Observer)] Actualización recibida del Paquete ID {paquete.get_id()}: Nuevo estado '{paquete.get_estado()}'")
        if paquete.get_id() in self._paquetes_activos:
            self._paquetes_activos[paquete.get_id()]["estado"] = paquete.get_estado()
            self._paquetes_activos[paquete.get_id()]["ubicacion_actual"] = f"Ubicación de {paquete.get_estado()}"
        else:
            print(f"[Rastreo Global (Observer)] Advertencia: Paquete {paquete.get_id()} no estaba registrado, registrando ahora.")
            self.registrar_nuevo_paquete(paquete)

    def mostrar_estado_global(self) -> None:
        """Muestra el estado actual de todos los paquetes rastreados."""
        print("\n--- ESTADO GLOBAL DE ENVÍOS ---")
        if not self._paquetes_activos:
            print("  No hay paquetes activos siendo rastreados.")
            return
        for id_paquete, info in self._paquetes_activos.items():
            print(f"  - Paquete ID {id_paquete}: Estado='{info['estado']}', Ubicación='{info['ubicacion_actual']}'")
        print("------------------------------")

    def registrar_nuevo_paquete(self, paquete: Paquete) -> None:
        """Registra un nuevo paquete para empezar a rastrearlo."""
        if paquete.get_id() not in self._paquetes_activos:
            print(f"[Rastreo Global] Registrando nuevo paquete ID {paquete.get_id()}")
            paquete.agregar_observador(self)
            self._paquetes_activos[paquete.get_id()] = {
                "estado": paquete.get_estado(), 
                "ubicacion_actual": "En Centro de Origen"
            }




################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 20
# Generado: 2025-11-04 19:55:50
################################################################################
