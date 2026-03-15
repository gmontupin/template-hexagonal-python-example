from src.domain.ports.health_repository import HealthCheckPort
from src.domain.models.health import HealthStatus


class CheckServiceHealthUseCase:
    def __init__(self, adapter: HealthCheckPort):
        self.adapter = adapter

    def execute(self) -> HealthStatus:
        """Lógica de negocio: delegar el chequeo al adaptador y devolver el resultado."""
        return self.adapter.check_service()
