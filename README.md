# Service Health Monitor

Este es un proyecto de ejemplo en Python que demuestra la implementación de la **Arquitectura Hexagonal** (también conocida como Puertos y Adaptadores) para monitorear el estado de salud de un servicio externo.

El objetivo principal es tener un núcleo de negocio (dominio) desacoplado de los detalles de infraestructura, permitiendo cambiar fácilmente las tecnologías externas (como el servicio a monitorear o la forma de notificar) sin afectar la lógica de negocio.

## ✨ Características

- Verifica el estado de salud de un servicio externo (actualmente, la API de GitHub).
- Mide la latencia de la respuesta.
- Implementado con **Arquitectura Hexagonal** para un diseño limpio y mantenible.
- Separación clara entre lógica de negocio, casos de uso e infraestructura.
- Incluye pruebas unitarias y de integración.
- Configurado con [Poetry](https://python-poetry.org/) para la gestión de dependencias.

## 🏗️ Estructura del Proyecto (Arquitectura Hexagonal)

El código está organizado siguiendo los principios de la Arquitectura Hexagonal:

- `src/domain`: El corazón de la aplicación. Contiene los modelos de negocio (`HealthStatus`) y las interfaces o **puertos** (`HealthCheckPort`) que definen los contratos que la infraestructura debe cumplir. No tiene dependencias de frameworks o tecnologías externas.

- `src/application`: Orquesta el flujo de datos. Contiene los **casos de uso** (`CheckServiceHealthUseCase`) que utilizan los puertos del dominio para ejecutar la lógica de negocio.

- `src/infrastructure`: Contiene la implementación concreta de los puertos. Los **adaptadores** (`GitHubHealthAdapter`) se conectan con el mundo exterior (APIs, bases de datos, etc.).

```
service-health-monitor/
├── src/
│   ├── application/
│   │   └── use_cases/
│   │       └── check_service.py   # Caso de uso
│   ├── domain/
│   │   ├── models/
│   │   │   └── health.py          # Modelo de negocio
│   │   └── ports/
│   │       └── health_repository.py # Puerto
│   ├── infrastructure/
│   │   └── adapters/
│   │       └── github_health_adapter.py # Adaptador
│   └── main.py                    # Punto de entrada
└── tests/
    ├── unit/
    └── integration/
```

## 🚀 Instalación y Configuración

Asegúrate de tener instalados **Python 3.9+** y **Poetry**.

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/service-health-monitor.git
    cd service-health-monitor
    ```

2.  **Instala las dependencias con Poetry:**
    ```bash
    poetry install
    ```

## 🏃 Uso

Para ejecutar el monitor de salud, simplemente ejecuta el script principal desde la raíz del proyecto:

```bash
poetry run python src/main.py
```

Verás una salida en la consola similar a esta:

```
--- Health Check Monitor ---
Verificando estado de salud del servicio...
Servicio: GitHub API
Estado: 🟢 Healthy
Latencia: 123.45 ms
Fecha/Hora: 2023-10-27 10:00:00
----------------------------
```

## ✅ Ejecutar Pruebas

El proyecto cuenta con pruebas unitarias y de integración. Para ejecutarlas, usa `pytest`:

```bash
poetry run pytest
```
