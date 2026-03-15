from src.infrastructure.adapters.github_health_adapter import GitHubHealthAdapter
from src.application.use_cases.check_service import CheckServiceHealthUseCase
from src.domain.models.health import HealthState


def main():
    """Punto de entrada: Ensamblaje de la arquitectura hexagonal."""

    # 1. Elegimos el adaptador (Infraestructura)
    github_adapter = GitHubHealthAdapter()

    # 2. Inyectamos el adaptador en el caso de uso (Aplicación)
    service_checker = CheckServiceHealthUseCase(github_adapter)

    # 3. Ejecutamos la lógica y mostramos el resultado
    print("--- Health Check Monitor ---")
    print("Verificando estado de salud del servicio...")

    health_status = service_checker.execute()

    print(f"Servicio: {health_status.service_name}")
    print(
        f"Estado: {'🟢 ' if health_status.status == HealthState.HEALTHY else '🔴 '}{health_status.status.value}"
    )
    print(f"Latencia: {health_status.latency_ms} ms")
    print(f"Fecha/Hora: {health_status.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    print("----------------------------")


if __name__ == "__main__":
    main()
