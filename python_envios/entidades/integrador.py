"""
Archivo integrador generado automaticamente
Directorio: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\entidades
Fecha: 2025-11-04 19:55:50
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\entidades\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: cliente.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\entidades\cliente.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/5: paquete.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\entidades\paquete.py
# ================================================================================

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



# ================================================================================
# ARCHIVO 4/5: servicio_rutas.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\entidades\servicio_rutas.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: vehiculo.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\entidades\vehiculo.py
# ================================================================================

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


