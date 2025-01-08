import os
import sys
import pytest
from unittest import mock
from config.db_config import load_db_config
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))


@mock.patch('config.db_config.load_dotenv')
@mock.patch.dict(os.environ, {
    'ENV': 'test',
    'SOURCE_DB_NAME': 'test_db',
    'SOURCE_DB_USER': 'test_user',
    'SOURCE_DB_PASSWORD': 'test_password',
    'SOURCE_DB_HOST': 'localhost',
    'SOURCE_DB_PORT': '5432'
})
def test_load_db_config(mock_load_dotenv):
    config = load_db_config()
    assert config['source_database']['dbname'] == 'test_db'
    assert config['source_database']['user'] == 'test_user'
    assert config['source_database']['password'] == 'test_password'
    assert config['source_database']['host'] == 'localhost'
    assert config['source_database']['port'] == '5432'
    mock_load_dotenv.assert_called_once_with('.env.test')


# Added after integration test failed and added ENV == None handling
@mock.patch('config.db_config.load_dotenv')
def test_load_db_config_no_env(mock_load_dotenv):
    with mock.patch.dict(os.environ, {}, clear=True):
        with mock.patch('config.db_config.load_dotenv') as mock_load_dotenv:
            with pytest.raises(KeyError):
                load_db_config()
            mock_load_dotenv.assert_not_called()
