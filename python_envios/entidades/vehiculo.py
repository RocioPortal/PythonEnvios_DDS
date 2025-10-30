"""
Entidades para Vehículos.
Define la clase base abstracta y las clases concretas
que serán creadas por el Factory Method.
"""
# --- Standard library imports ---
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

# --- Clases Concretas ---

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
