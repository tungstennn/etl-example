import psycopg2
import pytest
from utils.db_utils import get_db_connection, DatabaseConnectionError
from config.db_config import load_db_config


def test_db_connection_success():
    connection_params = load_db_config()['source_database']
    connection = get_db_connection(connection_params)

    # Assert that the connection has a cursor method
    assert hasattr(connection, 'cursor')

    # Optionally, you can also check if the connection is open
    assert connection.closed == 0  # 0 means the connection is open

    # Clean up by closing the connection
    connection.close()


# Should be a unit test?
def test_db_connection_invalid_params():
    connection_params = {
        'dbname': 'invalid_db',
        'user': 'invalid_user',
        'password': 'invalid_password',
        'host': 'invalid_host',
        'port': 'invalid_port'
    }

    with pytest.raises(DatabaseConnectionError):
        get_db_connection(connection_params)

# There should be more tests here that change the invalid parameter
# Each different invalidity produces a different error message


def test_db_connection_unavailable():
    connection_params = load_db_config()['source_database']
    connection_params['host'] = 'unreachable_host'

    with pytest.raises(DatabaseConnectionError):
        get_db_connection(connection_params)


# Move to be unit test
# def test_db_connection_timeout(mocker):
#     connection_params = load_db_config()['source_database']
#     mocker.patch(
#         'psycopg2.connect',
#         side_effect=psycopg2.OperationalError("timeout")
#         # https://www.psycopg.org/docs/errors.html
#     )

#     with pytest.raises(DatabaseConnectionError):
#         get_db_connection(connection_params)


# def test_db_connection_missing_env_vars(mocker):
#     mocker.patch.dict('os.environ', {}, clear=True)
#     # psycopg2 inserts default values for some missing parameters!
#     with pytest.raises(KeyError):
#         load_db_config()


def test_db_connection_already_closed():
    connection_params = load_db_config()['source_database']
    connection = get_db_connection(connection_params)
    connection.close()

    assert connection.closed == 1  # 1 means the connection is closed
    with pytest.raises(psycopg2.InterfaceError):
        connection.cursor()
