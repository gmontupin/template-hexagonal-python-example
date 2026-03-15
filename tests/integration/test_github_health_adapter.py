from src.infrastructure.adapters.github_health_adapter import GitHubHealthAdapter
from src.domain.models.health import HealthStatus, HealthState


def test_github_adapter_returns_valid_health_status():
    # Arrange
    adapter = GitHubHealthAdapter()

    # Act
    result = adapter.check_service()

    # Assert
    assert isinstance(result, HealthStatus)
    assert result.service_name == "GitHub API"
    assert isinstance(result.latency_ms, float)
    # Verificamos que el estado sea un miembro del Enum HealthState
    assert isinstance(result.status, HealthState)
