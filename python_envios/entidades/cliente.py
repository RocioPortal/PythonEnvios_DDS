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
