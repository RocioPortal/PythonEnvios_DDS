"""
Implementación del Patrón Singleton.
Esta clase también actúa como un Observer.
"""
# --- Standard library imports ---
from threading import Lock
from typing import Dict, Any, Optional

# --- Local application imports ---
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
                # Double-checked locking
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._paquetes_activos = {}
                    print("[Singleton] Instancia de SistemaRastreoGlobal creada.")
        return cls._instance

    @classmethod
    def get_instance(cls) -> 'SistemaRastreoGlobal':
        """Obtiene la instancia única del sistema de rastreo."""
        if cls._instance is None:
            cls() # Llama a __new__ si aún no existe
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
            # Se suscribe al paquete para recibir futuras actualizaciones (Observer)
            paquete.agregar_observador(self)
            self._paquetes_activos[paquete.get_id()] = {
                "estado": paquete.get_estado(), 
                "ubicacion_actual": "En Centro de Origen"
            }

