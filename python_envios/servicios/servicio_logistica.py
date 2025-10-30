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
