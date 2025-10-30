"""
Módulo para centralizar todas las constantes mágicas del sistema.
Cumple con el criterio de "NO magic numbers" de la rúbrica.
"""

# --- Factory Method ---
PESO_MAXIMO_MOTO = 50.0 # Paquetes de más de 50kg van en Camión

# --- Strategy ---
VELOCIDAD_PROMEDIO_MOTO = 60.0 # km/h
VELOCIDAD_PROMEDIO_CAMION = 70.0 # km/h (más rápido en autopista)
FACTOR_TRAFICO = 1.2 # Simula un 20% de retraso por tráfico
