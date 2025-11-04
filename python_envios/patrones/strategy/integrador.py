"""
Archivo integrador generado automaticamente
Directorio: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\strategy
Fecha: 2025-11-04 19:55:50
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\strategy\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: estrategia_ruteo.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\strategy\estrategia_ruteo.py
# ================================================================================

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



