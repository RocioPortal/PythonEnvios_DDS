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
