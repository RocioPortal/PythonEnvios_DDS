"""
Archivo integrador generado automaticamente
Directorio: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\servicios
Fecha: 2025-11-04 19:55:50
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\servicios\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: servicio_logistica.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\servicios\servicio_logistica.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: sistema_rastreo_global.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\servicios\sistema_rastreo_global.py
# ================================================================================

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



