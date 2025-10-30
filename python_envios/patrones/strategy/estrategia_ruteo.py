"""
Implementación del Patrón Strategy.
Define la interfaz (ABC) y las implementaciones concretas.
"""
# --- Standard library imports ---
from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, TYPE_CHECKING # <--- CORRECCIÓN AQUÍ: Se agregó 'Dict'

# --- Local application imports ---
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

# --- Implementaciones Concretas (Concrete Strategies) ---

class RutaMasRapida(EstrategiaRuteo):
    """Calcula la ruta considerando el tráfico (simulado)."""
    def calcular_ruta(self, origen: str, destino: str, distancia_km: float, vehiculo: 'Vehiculo') -> Dict:
        """Calcula la ruta más rápida, penalizada por tráfico."""
        print(f"[Estrategia Ruta Rápida] Calculando ruta de {origen} a {destino}...")
        
        # Lógica de velocidad diferente por vehículo
        from ...entidades.vehiculo import Camion
        if isinstance(vehiculo, Camion):
            velocidad = VELOCIDAD_PROMEDIO_CAMION
        else:
            velocidad = VELOCIDAD_PROMEDIO_MOTO
            
        # La ruta "rápida" es más larga pero usa autopista, y tiene tráfico
        distancia_real_km = distancia_km * 1.1 # 10% más larga
        tiempo_base_h = distancia_real_km / velocidad
        tiempo_final_h = tiempo_base_h * FACTOR_TRAFICO # Aplicamos factor de tráfico
        
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
            
        # La ruta "corta" es la distancia base pero tiene más tráfico (simulado)
        distancia_real_km = distancia_km
        tiempo_base_h = distancia_real_km / velocidad
        tiempo_final_h = tiempo_base_h * (FACTOR_TRAFICO + 0.1) # 10% más de tráfico por ser ruta corta (urbana)
        
        pasos = f"Atravesar centro de la ciudad (Ruta Corta). Distancia: {distancia_real_km:.1f}km."
        return {"pasos": pasos, "tiempo_estimado_h": tiempo_final_h}

class RutaEcologica(EstrategiaRuteo):
    """Calcula la ruta minimizando emisiones (simulado)."""
    def calcular_ruta(self, origen: str, destino: str, distancia_km: float, vehiculo: 'Vehiculo') -> Dict:
        """Calcula la ruta más ecológica (simulación simple)."""
        print(f"[Estrategia Ruta Ecológica] Calculando ruta de {origen} a {destino} (minimizando emisiones)...")
        
        # Simulación: ruta eco es un 5% más corta y tiene 5% menos tráfico que la corta
        distancia_real_km = distancia_km * 0.95
        velocidad = VELOCIDAD_PROMEDIO_MOTO # Asume vehículo más ligero
        
        tiempo_base_h = distancia_real_km / velocidad
        tiempo_final_h = tiempo_base_h * (FACTOR_TRAFICO - 0.05)
        
        pasos = f"Usar ruta de circunvalación verde. Distancia: {distancia_real_km:.1f}km."
        return {"pasos": pasos, "tiempo_estimado_h": tiempo_final_h}

