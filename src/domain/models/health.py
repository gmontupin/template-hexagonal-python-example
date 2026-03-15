from dataclasses import dataclass
import datetime
from enum import Enum


class HealthState(Enum):
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"


@dataclass
class HealthStatus:
    service_name: str
    status: HealthState  # Usamos el Enum en lugar de un string
    latency_ms: float
    timestamp: datetime.datetime
