Sistema de Gestión Logística - PythonEnvios
Alumna: Pilar Rocio Portal Romano   
Legajo: 63217
Ingeniería en informática

Sistema de gestión logística para el envío de paquetes, demostrando la implementación de patrones de diseño clave en Python. Este proyecto simula la lógica de negocio central de una empresa de envíos, aplicando principios de diseño de software para mantenibilidad y extensibilidad.

Tabla de Contenidos

Contexto del Dominio

Características Principales

Arquitectura del Sistema

Patrones de Diseño Implementados

Estructura del Proyecto

Ejemplo de Uso

Contexto del Dominio

PythonEnvios aborda los desafíos de una empresa de logística moderna. El sistema debe:

Gestionar Paquetes: Registrar paquetes con origen, destino, peso y un estado de seguimiento (Registrado, En Tránsito, Entregado).

Gestionar Flota de Vehículos: Asignar el vehículo correcto (Camión, Moto) según las características del paquete (ej. peso).

Optimizar Rutas: Calcular la mejor ruta para una entrega según diferentes criterios (la más rápida vs. la más corta).

Notificar Estado: Informar a los interesados (clientes, sistema central) en tiempo real sobre los cambios en el estado del paquete.

Rastreo Centralizado: Mantener un registro único y global del estado de todos los envíos activos.

Características Principales

Creación Flexible de Vehículos: Usa Factory Method para instanciar el vehículo adecuado (Camión, Moto) según las necesidades del envío (ej. peso del paquete).

Optimización de Rutas: Emplea el patrón Strategy para seleccionar dinámicamente el algoritmo de cálculo de ruta (RutaMasRapida, RutaMasCorta).

Notificaciones en Tiempo Real: Implementa el patrón Observer para que los Paquetes (Observables) notifiquen a los Clientes y al SistemaRastreoGlobal (Observers) sobre cambios de estado.

Rastreo Global Único: Utiliza el patrón Singleton para garantizar una única instancia del SistemaRastreoGlobal, accesible desde cualquier parte del sistema.

Arquitectura del Sistema

El sistema sigue principios SOLID y una separación de capas clara:

Entidades: Clases de datos puras (Paquete, Vehiculo, Cliente) y Contextos de patrones (ServicioRutas).

Servicios: Clases con lógica de negocio (ServicioLogistica) y el Singleton (SistemaRastreoGlobal).

Patrones: Implementaciones aisladas de los patrones (VehiculoFactory, EstrategiaRuteo, Observable/Observer).

Presentación: main.py orquesta la demostración.

Patrones de Diseño Implementados

1. SINGLETON

Clase: SistemaRastreoGlobal

Propósito: Garantizar una única instancia para el seguimiento de todos los paquetes activos. Provee un punto de acceso global y centralizado al estado de todos los envíos, evitando datos duplicados o inconsistentes.

2. FACTORY METHOD

Clase: VehiculoFactory

Propósito: Encapsular la lógica de creación de diferentes tipos de Vehiculo (Camion, Moto). El ServicioLogistica pide un vehículo basado en el peso, sin necesidad de saber qué clase concreta se debe instanciar.

3. OBSERVER

Clases:

Paquete (Observable): El sujeto que mantiene un estado.

ClienteNotifier (Observer): Un observador concreto que reacciona a los cambios.

SistemaRastreoGlobal (Observer): El Singleton también actúa como observador para actualizar su lista.

Propósito: Desacoplar el Paquete de los componentes que necesitan reaccionar a sus cambios de estado (ej. "En Tránsito", "Entregado"). El paquete notifica a sus observadores suscritos automáticamente.

4. STRATEGY

Clases:

EstrategiaRuteo (Interfaz): Define el contrato para un algoritmo de cálculo de ruta.

RutaMasRapida, RutaMasCorta (Implementaciones): Algoritmos concretos.

ServicioRutas (Contexto): Mantiene una referencia a una estrategia y la utiliza para calcular la ruta.

Propósito: Permitir que el ServicioRutas seleccione y utilice diferentes algoritmos para calcular la ruta de entrega de un paquete de forma intercambiable, sin cambiar el servicio que lo usa.

Estructura del Proyecto

PythonEnvios/
|
+-- .gitignore
+-- main.py
+-- README.md
+-- USER_STORIES.md
|
+-- python_envios/
    |
    +-- __init__.py
    +-- constantes.py
    |
    +-- entidades/
    |   +-- __init__.py
    |   +-- paquete.py
    |   +-- vehiculo.py
    |   +-- cliente.py
    |   +-- servicio_rutas.py  # Contexto de Strategy
    |
    +-- servicios/
    |   +-- __init__.py
    |   +-- servicio_logistica.py
    |   +-- sistema_rastreo_global.py # Singleton y Observer
    |
    +-- patrones/
        |   +-- __init__.py
        |   +-- factory/
        |   |   +-- __init__.py
        |   |   +-- vehiculo_factory.py
        |   +-- observer/
        |   |   +-- __init__.py
        |   |   +-- observable.py
        |   |   +-- observer.py
        |   |   +-- cliente_notifier.py
        |   +-- strategy/
        |       +-- __init__.py
        |       +-- estrategia_ruteo.py


Ejemplo de Uso

# main.py
from python_envios.servicios.servicio_logistica import ServicioLogistica
from python_envios.entidades.cliente import Cliente
from python_envios.entidades.servicio_rutas import ServicioRutas
from python_envios.patrones.strategy.estrategia_ruteo import RutaMasCorta
# ... otros imports

# Servicios y Singleton
logistica = ServicioLogistica()
cliente_ana = Cliente("Ana")
servicio_rutas = ServicioRutas() # Contexto de Strategy

# Crear y enviar paquete (usa Factory, Observer internamente)
paquete_id = logistica.registrar_y_asignar_paquete("Origen A", "Destino B", 5.0, [cliente_ana])

# Seleccionar estrategia de ruteo (Strategy)
servicio_rutas.set_estrategia(RutaMasCorta())
ruta = servicio_rutas.calcular_ruta("Origen A", "Destino B", 10.0, logistica.get_paquete(paquete_id).get_vehiculo())

# Procesar envío (cambia estado y notifica observers)
logistica.procesar_envio(paquete_id)

# Consultar estado (usa Singleton)
logistica.mostrar_estado_global()
