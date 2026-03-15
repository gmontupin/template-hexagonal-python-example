from unittest.mock import Mock
from src.application.use_cases.check_service import CheckServiceHealthUseCase
from src.domain.ports.health_repository import HealthCheckPort
from src.domain.models.health import HealthStatus, HealthState
import datetime


def test_use_case_executes_and_returns_adapter_result():
    # Arrange
    # 1. Creamos un resultado simulado que esperamos que el adaptador devuelva
    mock_health_status = HealthStatus(
        service_name="Mock Service",
        status=HealthState.HEALTHY,
        latency_ms=50.0,
        timestamp=datetime.datetime.now(),
    )

    # 2. Creamos un mock del adaptador que "finge" ser un HealthCheckPort
    mock_adapter = Mock(spec=HealthCheckPort)
    mock_adapter.check_service.return_value = mock_health_status

    # 3. Inyectamos el mock en el caso de uso
    use_case = CheckServiceHealthUseCase(adapter=mock_adapter)

    # Act
    result = use_case.execute()

    # Assert
    # Verificamos que el método del adaptador fue llamado y que el resultado es el esperado
    mock_adapter.check_service.assert_called_once()
    assert result == mock_health_status
    assert result.service_name == "Mock Service"
