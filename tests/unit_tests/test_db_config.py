import os
import pytest
from config.db_config import load_db_config, DatabaseConfigError


def test_load_db_config(mocker):
    # Mock environment variables
    mocker.patch.dict(os.environ, {
        'SOURCE_DB_NAME': 'test_source_db',
        'SOURCE_DB_USER': 'test_user',
        'SOURCE_DB_PASSWORD': 'test_password',
        'SOURCE_DB_HOST': 'localhost',
        'SOURCE_DB_PORT': '5432',
        'TARGET_DB_NAME': 'test_target_db',
        'TARGET_DB_USER': 'test_user',
        'TARGET_DB_PASSWORD': 'test_password',
        'TARGET_DB_HOST': 'localhost',
        'TARGET_DB_PORT': '5432'
    })

    config = load_db_config()

    assert config['source_database']['dbname'] == 'test_source_db'
    assert config['source_database']['user'] == 'test_user'
    assert config['source_database']['password'] == 'test_password'
    assert config['source_database']['host'] == 'localhost'
    assert config['source_database']['port'] == '5432'
    assert config['target_database']['dbname'] == 'test_target_db'
    assert config['target_database']['user'] == 'test_user'
    assert config['target_database']['password'] == 'test_password'
    assert config['target_database']['host'] == 'localhost'
    assert config['target_database']['port'] == '5432'


def test_load_db_config_missing_env_var_port_defaults(mocker):
    # Mock environment variables with some missing
    mocker.patch.dict(os.environ, {
        'SOURCE_DB_NAME': 'test_source_db',
        'SOURCE_DB_USER': 'test_user',
        'SOURCE_DB_PASSWORD': 'test_password',
        'SOURCE_DB_HOST': 'localhost',
        # 'SOURCE_DB_PORT': '5432',  # Missing
        'TARGET_DB_NAME': 'test_target_db',
        'TARGET_DB_USER': 'test_user',
        'TARGET_DB_PASSWORD': 'test_password',
        'TARGET_DB_HOST': 'localhost',
        'TARGET_DB_PORT': '5432'
    })

    config = load_db_config()

    assert config['source_database']['dbname'] == 'test_source_db'
    assert config['source_database']['user'] == 'test_user'
    assert config['source_database']['password'] == 'test_password'
    assert config['source_database']['host'] == 'localhost'
    assert config['source_database']['port'] == '5432'  # Default value
    assert config['target_database']['dbname'] == 'test_target_db'
    assert config['target_database']['user'] == 'test_user'
    assert config['target_database']['password'] == 'test_password'
    assert config['target_database']['host'] == 'localhost'
    assert config['target_database']['port'] == '5432'


# def test_load_db_config_missing_env_var_host_errors(mocker):
#     # Mock environment variables with some missing
#     mocker.patch.dict(os.environ, {
#         'SOURCE_DB_NAME': 'test_source_db',
#         'SOURCE_DB_USER': 'test_user',
#         'SOURCE_DB_PASSWORD': 'test_password',
#         'SOURCE_DB_HOST': 'error', # missing so default used
#         'SOURCE_DB_PORT': '5432',
#         'TARGET_DB_NAME': 'test_target_db',
#         'TARGET_DB_USER': 'test_user',
#         'TARGET_DB_PASSWORD': 'test_password',
#         'TARGET_DB_HOST': 'localhost',
#         'TARGET_DB_PORT': '5432'
#     })

#     with pytest.raises(DatabaseConfigError, load_db_config):
#         load_db_config()

    # assert config['source_database']['dbname'] == 'test_source_db'
    # assert config['source_database']['user'] == 'test_user'
    # assert config['source_database']['password'] == 'test_password'
    # assert config['source_database']['host'] == 'localhost'
    # assert config['source_database']['port'] == '5432'  # Default value
    # assert config['target_database']['dbname'] == 'test_target_db'
    # assert config['target_database']['user'] == 'test_user'
    # assert config['target_database']['password'] == 'test_password'
    # assert config['target_database']['host'] == 'localhost'
    # assert config['target_database']['port'] == '5432'

# import os
# import pytest
# from unittest import mock
# from config.db_config import load_db_config


# @mock.patch('config.db_config.load_dotenv')
# @mock.patch.dict(os.environ, {
#     'ENV': 'test',
#     'SOURCE_DB_NAME': 'test_db',
#     'SOURCE_DB_USER': 'test_user',
#     'SOURCE_DB_PASSWORD': 'test_password',
#     'SOURCE_DB_HOST': 'localhost',
#     'SOURCE_DB_PORT': '5432'
# })
# def test_load_db_config(mock_load_dotenv):
#     config = load_db_config()
#     assert config['source_database']['dbname'] == 'test_db'
#     assert config['source_database']['user'] == 'test_user'
#     assert config['source_database']['password'] == 'test_password'
#     assert config['source_database']['host'] == 'localhost'
#     assert config['source_database']['port'] == '5432'
#     mock_load_dotenv.assert_called_once_with('.env.test')


# # Added after integration test failed and added ENV == None handling
# @mock.patch('config.db_config.load_dotenv')
# def test_load_db_config_no_env(mock_load_dotenv):
#     with mock.patch.dict(os.environ, {}, clear=True):
#         with mock.patch('config.db_config.load_dotenv') as mock_load_dotenv:
#             with pytest.raises(KeyError):
#                 load_db_config()
#             mock_load_dotenv.assert_not_called()
