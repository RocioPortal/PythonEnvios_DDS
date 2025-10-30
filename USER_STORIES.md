Historias de Usuario - Sistema de Gestión Logística (PythonEnvios)

Proyecto: PythonEnvios
Version: 1.0.0

Índice

Epic 1: Gestión de Paquetes

Epic 2: Gestión de Flota

Epic 3: Optimización de Rutas

Epic 4: Notificaciones y Rastreo

Historias Técnicas (Patrones de Diseño)

Epic 1: Gestión de Paquetes

US-001: Registrar Nuevo Paquete

Como empleado de logística,
Quiero registrar un nuevo paquete con origen, destino y peso,
Para iniciar el proceso de envío.

Criterios de Aceptación:

✓ Paquete debe tener ID único, origen, destino, peso, y estado inicial ("Registrado").

✓ Peso debe ser positivo.

US-002: Actualizar Estado del Paquete

Como sistema de logística,
Quiero actualizar el estado de un paquete (ej. "En Tránsito", "Entregado"),
Para reflejar su progreso en la cadena de envío.

Criterios de Aceptación:

✓ El paquete debe permitir cambiar su estado.

✓ Cada cambio de estado debe notificar a los observadores suscritos (Patrón Observer).

Epic 2: Gestión de Flota

US-003: Crear Diferentes Tipos de Vehículos

Como administrador de flota,
Quiero poder crear vehículos de tipo Camion y Moto,
Para tener una flota que se adapte a diferentes tamaños de envíos.

Criterios de Aceptación:

✓ Deben existir clases para Camion y Moto que hereden de Vehiculo.

✓ Cada tipo debe tener atributos específicos (capacidad_kg, velocidad_max).

✓ La creación debe hacerse a través de VehiculoFactory (Patrón Factory Method).

US-004: Asignar Vehículo a Paquete

Como sistema de logística,
Quiero asignar el vehículo más adecuado a un paquete basado en su peso,
Para optimizar la entrega.

Criterios de Aceptación:

✓ Usar VehiculoFactory para obtener la instancia del vehículo.

✓ Si peso_kg > 50, asignar Camion.

✓ Si peso_kg <= 50, asignar Moto.

✓ El paquete debe registrar qué vehículo fue asignado.

Epic 3: Optimización de Rutas

US-005: Calcular Ruta de Entrega

Como planificador de rutas,
Quiero calcular la ruta óptima para un envío,
Para minimizar el tiempo o la distancia.

Criterios de Aceptación:

✓ El ServicioRutas (Contexto) debe calcular la ruta usando una EstrategiaRuteo.

✓ Deben existir al menos 2 estrategias: RutaMasRapida y RutaMasCorta (Patrón Strategy).

US-006: Cambiar Estrategia de Ruteo

Como administrador del sistema,
Quiero cambiar la estrategia de cálculo de rutas,
Para adaptarme a diferentes prioridades (ej. tráfico vs. distancia).

Criterios de Aceptación:

✓ El ServicioRutas debe permitir cambiar su EstrategiaRuteo en tiempo de ejecución.

✓ El cálculo de ruta debe usar la estrategia actualmente configurada.

Epic 4: Notificaciones y Rastreo

US-007: Notificar Cliente sobre Cambio de Estado

Como cliente,
Quiero recibir notificaciones cuando el estado de mi paquete cambie,
Para estar informado sobre mi envío.

Criterios de Aceptación:

✓ El Cliente debe poder suscribirse a notificaciones de un Paquete.

✓ Debe existir un ClienteNotifier que implemente la interfaz Observer.

✓ Cuando el Paquete cambie de estado, ClienteNotifier debe ser notificado (Patrón Observer).

US-008: Rastrear Todos los Paquetes Activos

Como operador del sistema,
Quiero ver el estado actual de todos los paquetes en tránsito,
Para tener una visión global de las operaciones.

Criterios de Aceptación:

✓ Debe existir un SistemaRastreoGlobal como Singleton.

✓ El SistemaRastreoGlobal debe actuar como Observer de todos los paquetes nuevos.

✓ Debe proveer un método para mostrar el estado de todos los paquetes que rastrea.

Historias Técnicas (Patrones de Diseño)

US-TECH-001: Implementar Singleton para Rastreo Global

Como arquitecto,
Quiero asegurar una única instancia de SistemaRastreoGlobal,
Para mantener un estado de rastreo consistente y centralizado.

Criterios de Aceptación:

✓ Implementar Patrón Singleton thread-safe.

✓ Usar get_instance().

✓ La instancia debe ser única en todo el sistema.

US-TECH-002: Implementar Factory Method para Vehículos

Como arquitecto,
Quiero usar Factory Method en VehiculoFactory,
Para desacoplar la creación de vehículos de la lógica de asignación.

Criterios de Aceptación:

✓ VehiculoFactory con método estático crear_vehiculo(peso_paquete).

✓ Usar un diccionario o lógica de decisión (no if/elif) para seleccionar el método de creación.

✓ Retornar tipo base Vehiculo.

US-TECH-003: Implementar Observer para Estados de Paquete

Como arquitecto,
Quiero que Paquete sea Observable y ClienteNotifier/SistemaRastreoGlobal sean Observers,
Para lograr notificaciones desacopladas.

Criterios de Aceptación:

✓ Clase base Observable y interfaz Observer.

✓ Paquete hereda de Observable.

✓ ClienteNotifier y SistemaRastreoGlobal implementan Observer.

✓ Paquete.set_estado() llama a notificar_observadores().

US-TECH-004: Implementar Strategy para Cálculo de Rutas

Como arquitecto,
Quiero usar Strategy para los algoritmos de ruteo,
Para permitir flexibilidad y extensibilidad en la planificación.

Criterios de Aceptación:

✓ Interfaz EstrategiaRuteo (ABC) con método calcular_ruta().

✓ Implementaciones concretas (RutaMasRapida, RutaMasCorta).

✓ ServicioRutas (Contexto) tiene una referencia a EstrategiaRuteo.

✓ ServicioRutas permite cambiar la estrategia (set_estrategia).

✓ ServicioRutas.calcular_ruta() delega el cálculo a la estrategia actual.