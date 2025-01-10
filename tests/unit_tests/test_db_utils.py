import pytest
import psycopg2
from unittest.mock import MagicMock
from utils.db_utils import get_db_connection, DatabaseConnectionError


@pytest.fixture
def connection_params():
    return {
        'dbname': 'test_db',
        'user': 'test_user',
        'password': 'test_password',
        'host': 'test_host',
        'port': 'test_port'
    }


def test_get_db_connection_success(mocker, connection_params):
    # Arrange
    mock_connection = MagicMock()
    mock_connect = mocker.patch(
        'psycopg2.connect', return_value=mock_connection
    )
    # Act
    connection = get_db_connection(connection_params)
    # Assert
    mock_connect.assert_called_once_with(**connection_params)
    assert connection == mock_connection


def test_get_db_connection_success_logging(mocker, connection_params):
    mock_logger = mocker.patch('utils.db_utils.logger')
    mock_connection = MagicMock()
    mocker.patch('psycopg2.connect', return_value=mock_connection)

    get_db_connection(connection_params)

    mock_logger.info.assert_called_once_with(
        "Successfully connected to the database."
    )


def test_get_db_connection_failure(mocker, connection_params):
    mock_connect = mocker.patch(
        'psycopg2.connect',
        side_effect=psycopg2.Error("Connection error")
    )
    mock_logger = mocker.patch('utils.db_utils.logger')

    with pytest.raises(DatabaseConnectionError) as excinfo:
        get_db_connection(connection_params)

    assert str(excinfo.value) == (
        "Failed to connect to the database: Connection error"
    )
    mock_connect.assert_called_once_with(**connection_params)
    mock_logger.error.assert_called_once_with(
        "Failed to connect to the database: Connection error"
    )


def test_get_db_connection_timeout_failure(mocker, connection_params):
    mocker.patch(
        'psycopg2.connect',
        side_effect=psycopg2.OperationalError("timeout")
    )
    mock_logger = mocker.patch('utils.db_utils.logger')

    with pytest.raises(DatabaseConnectionError) as excinfo:
        get_db_connection(connection_params)

    assert str(excinfo.value) == (
        "Failed to connect to the database: timeout"
    )
    mock_logger.error.assert_called_once_with(
        "Failed to connect to the database: timeout"
    )
