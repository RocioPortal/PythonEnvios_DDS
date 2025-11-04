"""
Archivo integrador generado automaticamente
Directorio: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\factory
Fecha: 2025-11-04 19:55:50
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\factory\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: vehiculo_factory.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\patrones\factory\vehiculo_factory.py
# ================================================================================

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



