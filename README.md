**Alumna:** Pilar Rocío Portal Romano  
**Legajo:** 63217  
**Carrera:** Ingeniería en Informática  

# Sistema de Gestión Logística - PythonEnvios

Sistema de gestión logística para el envío de paquetes, demostrando la implementación de patrones de diseño clave en Python.  
Este proyecto simula la lógica de negocio central de una empresa de envíos, aplicando principios de diseño de software para mantenibilidad y extensibilidad.

---

## Tabla de Contenidos
- [Contexto del Dominio](#contexto-del-dominio)
- [Características Principales](#características-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Patrones de Diseño Implementados](#patrones-de-diseño-implementados)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Ejemplo de Uso](#ejemplo-de-uso)

---

## Contexto del Dominio

**PythonEnvios** aborda los desafíos de una empresa de logística moderna.  
El sistema debe:

- **Gestionar Paquetes:** Registrar paquetes con origen, destino, peso y un estado de seguimiento (`Registrado`, `En Tránsito`, `Entregado`).
- **Gestionar Flota de Vehículos:** Asignar el vehículo correcto (`Camión`, `Moto`) según las características del paquete (por ejemplo, el peso).
- **Optimizar Rutas:** Calcular la mejor ruta para una entrega según diferentes criterios (la más rápida vs. la más corta).
- **Notificar Estado:** Informar a los interesados (clientes, sistema central) en tiempo real sobre los cambios en el estado del paquete.
- **Rastreo Centralizado:** Mantener un registro único y global del estado de todos los envíos activos.

---

## Características Principales

- **Creación Flexible de Vehículos:**  
  Usa el patrón *Factory Method* para instanciar el vehículo adecuado (`Camión`, `Moto`) según el peso del paquete.

- **Optimización de Rutas:**  
  Emplea el patrón *Strategy* para seleccionar dinámicamente el algoritmo de cálculo de ruta (`RutaMasRapida`, `RutaMasCorta`).

- **Notificaciones en Tiempo Real:**  
  Implementa el patrón *Observer* para que los `Paquetes` (Observables) notifiquen a los `Clientes` y al `SistemaRastreoGlobal` (Observers) sobre cambios de estado.

- **Rastreo Global Único:**  
  Utiliza el patrón *Singleton* para garantizar una única instancia del `SistemaRastreoGlobal`, accesible desde cualquier parte del sistema.

---

## Arquitectura del Sistema

El sistema sigue principios **SOLID** y una **separación clara por capas**:

- **Entidades:** Clases de datos puras (`Paquete`, `Vehiculo`, `Cliente`) y contextos de patrones (`ServicioRutas`).
- **Servicios:** Lógica de negocio (`ServicioLogistica`) y el `SistemaRastreoGlobal` (Singleton + Observer).
- **Patrones:** Implementaciones aisladas de los patrones (`VehiculoFactory`, `EstrategiaRuteo`, `Observable`/`Observer`).
- **Presentación:** `main.py` orquesta la demostración del sistema.

---

## Patrones de Diseño Implementados

### 1. SINGLETON
- **Clase:** `SistemaRastreoGlobal`  
- **Propósito:** Garantizar una única instancia para el seguimiento de todos los paquetes activos.  
  Provee un punto de acceso global y evita datos duplicados o inconsistentes.

---

### 2. FACTORY METHOD
- **Clase:** `VehiculoFactory`  
- **Propósito:** Encapsular la lógica de creación de diferentes tipos de `Vehiculo` (`Camion`, `Moto`).  
  El `ServicioLogistica` solicita un vehículo basado en el peso, sin conocer la clase concreta.

---

### 3. OBSERVER
- **Clases:**
  - `Paquete` (Observable)  
  - `ClienteNotifier` (Observer)  
  - `SistemaRastreoGlobal` (Observer y Singleton)

- **Propósito:** Desacoplar el `Paquete` de los componentes que reaccionan a sus cambios de estado.  
  Los observadores son notificados automáticamente ante actualizaciones como “En Tránsito” o “Entregado”.

---

### 4. STRATEGY
- **Clases:**
  - `EstrategiaRuteo` (Interfaz)  
  - `RutaMasRapida`, `RutaMasCorta` (Implementaciones concretas)  
  - `ServicioRutas` (Contexto)

- **Propósito:** Permitir que `ServicioRutas` seleccione y utilice diferentes algoritmos de cálculo de ruta de forma intercambiable, sin modificar su lógica interna.

---

## Estructura del Proyecto

PythonEnvios/
│
├── .gitignore
├── main.py
├── README.md
├── USER_STORIES.md
│
└── python_envios/
├── init.py
├── constantes.py
│
├── entidades/
│ ├── init.py
│ ├── paquete.py
│ ├── vehiculo.py
│ ├── cliente.py
│ ├── servicio_rutas.py # Contexto de Strategy
│
├── servicios/
│ ├── init.py
│ ├── servicio_logistica.py
│ ├── sistema_rastreo_global.py # Singleton + Observer
│
└── patrones/
├── init.py
├── factory/
│ ├── init.py
│ ├── vehiculo_factory.py
├── observer/
│ ├── init.py
│ ├── observable.py
│ ├── observer.py
│ ├── cliente_notifier.py
└── strategy/
├── init.py
├── estrategia_ruteo.py


---

## Ejemplo de Uso

```python
# main.py
from python_envios.servicios.servicio_logistica import ServicioLogistica
from python_envios.entidades.cliente import Cliente
from python_envios.entidades.servicio_rutas import ServicioRutas
from python_envios.patrones.strategy.estrategia_ruteo import RutaMasCorta
# ... otros imports

# Servicios y Singleton
logistica = ServicioLogistica()
cliente_ana = Cliente("Ana")
servicio_rutas = ServicioRutas()  # Contexto de Strategy

# Crear y enviar paquete (usa Factory y Observer internamente)
paquete_id = logistica.registrar_y_asignar_paquete(
    "Origen A", "Destino B", 5.0, [cliente_ana]
)

# Seleccionar estrategia de ruteo (Strategy)
servicio_rutas.set_estrategia(RutaMasCorta())
ruta = servicio_rutas.calcular_ruta(
    "Origen A", "Destino B", 10.0,
    logistica.get_paquete(paquete_id).get_vehiculo()
)

# Procesar envío (cambia estado y notifica observers)
logistica.procesar_envio(paquete_id)

# Consultar estado (usa Singleton)
logistica.mostrar_estado_global()
