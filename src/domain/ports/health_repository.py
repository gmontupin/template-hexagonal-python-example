from abc import ABC, abstractmethod
from src.domain.models.health import HealthStatus


class HealthCheckPort(ABC):
    @abstractmethod
    def check_service(self) -> HealthStatus:
        """Puerto para realizar un chequeo de salud de un servicio externo."""
        pass
