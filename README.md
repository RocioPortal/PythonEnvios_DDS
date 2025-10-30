Sistema de Gestión Logística - PythonEnvios
Alumna: Rocio Portal 
Legajo: 63217
Ingeniería en Informática

Sistema de gestión logística para el envío de paquetes, demostrando la implementación de patrones de diseño clave en Python, similar en estructura al parcial de PythonForestal.

Tabla de Contenidos

Contexto del Dominio

Características Principales

Arquitectura del Sistema

Patrones de Diseño Implementados

Estructura del Proyecto

Uso (Ejemplo)

Contexto del Dominio

PythonEnvios simula una plataforma para coordinar la entrega de paquetes. El sistema debe:

Gestionar Paquetes: Registrar paquetes con origen, destino, peso y estado.

Gestionar Flota de Vehículos: Utilizar distintos vehículos (Camión, Moto) con capacidades y velocidades diferentes.

Optimizar Rutas: Calcular la mejor ruta para cada entrega según diferentes criterios (más rápida, más corta).

Notificar Estado: Informar a los interesados (clientes, sistema central) sobre los cambios en el estado del paquete (en tránsito, entregado).

Rastreo Centralizado: Mantener un registro único y global del estado de todos los envíos activos.

Características Principales

Creación Flexible de Vehículos: Usa Factory Method para instanciar el vehículo adecuado (Camión, Moto) según las necesidades del envío (ej. peso del paquete).

Optimización de Rutas: Emplea el patrón Strategy para seleccionar dinámicamente el algoritmo de cálculo de ruta (Más Rápida, Más Corta).

Notificaciones en Tiempo Real: Implementa el patrón Observer para que los paquetes (Observable) notifiquen a los clientes y al sistema de rastreo (Observers) sobre cambios de estado.

Rastreo Global Único: Utiliza el patrón Singleton para garantizar una única instancia del SistemaRastreoGlobal, accesible desde cualquier parte del sistema.

Arquitectura del Sistema

El sistema sigue principios SOLID y una separación conceptual idéntica a PythonForestal:

Entidades: (Paquete, Vehiculo, Cliente, ServicioRutas) - Datos puros y contexto de Strategy.

Servicios: (ServicioLogistica, SistemaRastreoGlobal) - Lógica de negocio, Singleton y Observer.

Patrones: Implementaciones aisladas (VehiculoFactory, EstrategiaRuteo, Observable).

Presentación: (main.py) - Orquestación y demostración.

Patrones de Diseño Implementados

SINGLETON:

Clase: SistemaRastreoGlobal

Propósito: Garantizar una única instancia para el seguimiento de todos los paquetes activos. Provee acceso global y centralizado al estado de los envíos.

FACTORY METHOD:

Clase: VehiculoFactory

Propósito: Encapsular la lógica de creación de diferentes tipos de Vehiculo (Camión, Moto). Permite añadir nuevos tipos de vehículos sin modificar el código cliente.

OBSERVER:

Clases: Paquete (Observable), ClienteNotifier, SistemaRastreoGlobal (Observers)

Propósito: Desacoplar el Paquete de los componentes que necesitan reaccionar a sus cambios de estado (ej. "en tránsito", "entregado"). El paquete notifica a sus observadores suscritos automáticamente.

STRATEGY:

Clases: EstrategiaRuteo (Interfaz), RutaMasRapida, RutaMasCorta (Implementaciones), ServicioRutas (Contexto).

Propósito: Permitir que el ServicioRutas seleccione y utilice diferentes algoritmos para calcular la ruta de entrega de un paquete de forma intercambiable.

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
    |   +-- servicio_rutas.py # Contexto de Strategy
    |
    +-- servicios/
    |   +-- __init__.py
    |   +-- servicio_logistica.py
    |   +-- sistema_rastreo_global.py # Singleton y Observer
    |
    +-- patrones/
    |   +-- __init__.py
    |   +-- factory/
    |   |   +-- vehiculo_factory.py
    |   +-- observer/
    |   |   +-- observable.py
    |   |   +-- observer.py
    |   |   +-- cliente_notifier.py
    |   +-- strategy/
    |       +-- estrategia_ruteo.py
    |
    +-- excepciones/
        +-- __init__.py
        +-- logistica_exception.py


Uso (Ejemplo)

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
ruta = servicio_rutas.calcular_ruta("Origen A", "Destino B")

# Procesar envío (cambia estado y notifica observers)
logistica.procesar_envio(paquete_id)

# Consultar estado (usa Singleton)
logistica.mostrar_estado_global()
