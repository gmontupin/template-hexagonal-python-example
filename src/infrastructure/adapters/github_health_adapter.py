import http.client
import time
from datetime import datetime
from src.domain.models.health import HealthStatus, HealthState
from src.domain.ports.health_repository import HealthCheckPort


class GitHubHealthAdapter(HealthCheckPort):
    def __init__(self, host: str = "api.github.com"):
        self.host = host

    def check_service(self) -> HealthStatus:
        start_time = time.time()
        headers = {"User-Agent": "Python/HealthCheckMonitor"}
        conn = http.client.HTTPSConnection(self.host, timeout=5)

        try:
            conn.request("GET", "/", headers=headers)
            response = conn.getresponse()
            status = (
                HealthState.HEALTHY if response.status == 200 else HealthState.UNHEALTHY
            )
        except Exception:
            status = HealthState.UNHEALTHY
        finally:
            conn.close()

        latency = (time.time() - start_time) * 1000

        return HealthStatus(
            status=status,
            latency_ms=round(latency, 2),
            timestamp=datetime.now(),
            service_name="GitHub API",
        )
