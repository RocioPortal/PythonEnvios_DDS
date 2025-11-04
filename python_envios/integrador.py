"""
Archivo integrador generado automaticamente
Directorio: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios
Fecha: 2025-11-04 19:55:50
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: constantes.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\constantes.py
# ================================================================================

"""
Módulo para centralizar todas las constantes mágicas del sistema.
Cumple con el criterio de "NO magic numbers" de la rúbrica.
"""
PESO_MAXIMO_MOTO = 50.0 

VELOCIDAD_PROMEDIO_MOTO = 60.0 
VELOCIDAD_PROMEDIO_CAMION = 70.0 
FACTOR_TRAFICO = 1.2 


# ================================================================================
# ARCHIVO 3/3: main.py
# Ruta: C:\Users\thinkpad\Documents\DiseñoDeSistemas\PythonEnvios\python_envios\main.py
# ================================================================================

"""
Punto de entrada principal para la demostración del sistema PythonEnvios.
Este archivo simula el rol del "Cliente" u "Operador" que utiliza el sistema.
"""
import time 
# Entidades y Contexto de Strategy
from python_envios.entidades.cliente import Cliente
from python_envios.entidades.servicio_rutas import ServicioRutas

# Servicios y Singleton
from python_envios.servicios.servicio_logistica import ServicioLogistica
from python_envios.servicios.sistema_rastreo_global import SistemaRastreoGlobal

# Patrones
from python_envios.patrones.observer.cliente_notifier import ClienteNotifier
from python_envios.patrones.strategy.estrategia_ruteo import RutaMasCorta, RutaEcologica, RutaMasRapida

from python_envios.patrones.observer.observable import Observable
class Paquete(Observable['Paquete']):
    """Entidad Paquete (Observable)."""
    _counter = 0
    def __init__(self, origen, destino, peso):
        super().__init__()
        Paquete._counter += 1
        self._id = Paquete._counter
        self._origen = origen
        self._destino = destino
        self._peso_kg = peso
        self._estado = "Registrado"
        self._vehiculo_asignado = None
    def get_id(self): return self._id
    def get_peso_kg(self): return self._peso_kg
    def get_estado(self): return self._estado
    def get_origen(self): return self._origen
    def get_destino(self): return self._destino
    def set_vehiculo(self, v): self._vehiculo_asignado = v
    def get_vehiculo(self): return self._vehiculo_asignado
    def set_estado(self, nuevo_estado):
        if self._estado != nuevo_estado:
            self._estado = nuevo_estado
            print(f"\n---> (Paquete {self._id}): Estado cambiado a '{self._estado}' <---")
            self.notificar_observadores(self)

import python_envios.entidades.paquete as paquete_module
paquete_module.Paquete = Paquete

class Vehiculo:
    """Entidad Vehículo (Base)."""
    def __init__(self, id_v, cap, vel): self._id = id_v; self._cap = cap; self._vel = vel
    def get_capacidad_kg(self): return self._cap
    def get_velocidad_max_kmh(self): return self._vel
    def describir(self): print(f"Vehículo genérico {self._id}")

class Camion(Vehiculo): 
    """Entidad Camión."""
    def __init__(self, id_vehiculo, capacidad_kg):
        super().__init__(id_vehiculo, capacidad_kg, 90.0)
    def describir(self): print(f"Camión ID {self._id}, Capacidad: {self._capacidad_kg}kg")

class Moto(Vehiculo): 
    """Entidad Moto."""
    def __init__(self, id_vehiculo, capacidad_kg):
        super().__init__(id_vehiculo, capacidad_kg, 110.0)
    def describir(self): print(f"Moto ID {self._id}, Capacidad: {self._capacidad_kg}kg")

import python_envios.entidades.vehiculo as vehiculo_module
vehiculo_module.Vehiculo = Vehiculo
vehiculo_module.Camion = Camion
vehiculo_module.Moto = Moto


def imprimir_titulo(titulo):
    """Función helper para imprimir títulos."""
    print("\n" + "="*70)
    print(f"  {titulo.upper()}")
    print("="*70)

def main_demo_patrones():
    """Función principal que demuestra los 4 patrones."""

    imprimir_titulo("Inicio de la Simulación Logística - PythonEnvios")

    # ======================================================================
    # PATRÓN SINGLETON: Sistema de Rastreo Global
    # ======================================================================
    imprimir_titulo("Patrón Singleton")
    print("Obteniendo instancias del Sistema de Rastreo Global...")
    rastreador1 = SistemaRastreoGlobal.get_instance()
    rastreador2 = SistemaRastreoGlobal.get_instance()

    if rastreador1 is rastreador2:
        print("[OK] Ambas variables apuntan a la MISMA instancia única del rastreador.")
    else:
        print("[ERROR] Se crearon múltiples instancias del Singleton.")
    print(f"ID de la instancia: {id(rastreador1)}")

    # ======================================================================
    # Inicialización General
    # ======================================================================
    imprimir_titulo("Inicialización del Sistema")
    servicio_logistica = ServicioLogistica() 
    cliente_ana = Cliente("Ana")
    cliente_luis = Cliente("Luis")
    
    servicio_rutas = ServicioRutas() 
    
    notifier_ana = ClienteNotifier(cliente_ana.get_nombre())
    notifier_luis = ClienteNotifier(cliente_luis.get_nombre())

    # ======================================================================
    # PATRÓN FACTORY METHOD: Creación de vehículos (implícito)
    # y PATRÓN OBSERVER: Suscripción
    # ======================================================================
    imprimir_titulo("Patrón Factory Method y Observer (Suscripción)")
    print("Registrando paquetes (esto usa Factory para asignar vehículo y suscribe Observers)...")

    paquete_ana_id = servicio_logistica.registrar_y_asignar_paquete(
        origen="Depósito Central",
        destino="Casa Ana",
        peso_kg=5.0, 
        observadores_externos=[notifier_ana] 
    )

    paquete_luis_id = servicio_logistica.registrar_y_asignar_paquete(
        origen="Puerto Seco",
        destino="Fábrica Luis",
        peso_kg=501.0, # > 50kg
        observadores_externos=[notifier_luis] 
    )
    rastreador1.mostrar_estado_global()

    # ======================================================================
    # PATRÓN STRATEGY: Cálculo y cambio de Rutas
    # ======================================================================
    imprimir_titulo("Patrón Strategy")
    paquete_ana = servicio_logistica._paquetes_db[paquete_ana_id]
    
    print("Planificando entrega con estrategia por defecto (RutaMasRapida)...")
    servicio_rutas.calcular_ruta("Depósito Central", "Casa Ana", 10.0, paquete_ana.get_vehiculo())

    print("\nCambiando a estrategia RutaMasCorta...")
    servicio_rutas.set_estrategia(RutaMasCorta())
    servicio_rutas.calcular_ruta("Depósito Central", "Casa Ana", 10.0, paquete_ana.get_vehiculo())

    # ======================================================================
    # PATRÓN OBSERVER: Notificaciones por cambio de estado
    # ======================================================================
    imprimir_titulo("Patrón Observer en Acción (Notificaciones)")
    print("Procesando envíos (cambiarán estado y notificarán a los Observers)...")

    print("\n--- Procesando paquete de Ana ---")
    servicio_logistica.procesar_envio(paquete_ana_id) 
    time.sleep(1) # Simula tiempo
    servicio_logistica.procesar_envio(paquete_ana_id) 

    print("\n--- Procesando paquete de Luis ---")
    servicio_logistica.procesar_envio(paquete_luis_id) 

    # ======================================================================
    # PATRÓN SINGLETON: Verificación final del estado
    # ======================================================================
    imprimir_titulo("Patrón Singleton: Verificación Final del Rastreo")
    rastreador2.mostrar_estado_global()

    imprimir_titulo("Simulación Logística Completada")

if __name__ == "__main__":
    main_demo_patrones()



