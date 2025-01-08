import os
from typing import Dict
from dotenv import load_dotenv


def load_db_config() -> Dict[str, Dict[str, str]]:
    """
    Load database configuration from environment variables
    Set this with the appropriate values in the .env file
    or in the deployment environment.
    Run with the ENV environment variable set to the
    appropriate environment, so for tests:
        Unix: ENV=test python scripts/run_etl.py
        Windows PS: $env:ENV="test"; python scripts\run_etl.py
        Windows CMD: set ENV=test && python scripts\run_etl.py
    Other environments are dev and prod
    :return: Dictionary containing source and target database
    connection parameters.
    """
    # env = os.getenv('ENV', 'dev')
    env = os.getenv('ENV')

    # Throw an error or load the appropriate .env file
    if env is None:
        raise KeyError('ENV variable not set')

    env_file = '.env' if env == 'prod' else f'.env.{env}'
    load_dotenv(env_file)

    config = {
        'source_database': {
            'dbname': os.getenv('SOURCE_DB_NAME'),
            'user': os.getenv('SOURCE_DB_USER'),
            'password': os.getenv('SOURCE_DB_PASSWORD'),
            'host': os.getenv('SOURCE_DB_HOST'),
            'port': os.getenv('SOURCE_DB_PORT')
        },
        'target_database': {
            'dbname': os.getenv('TARGET_DB_NAME'),
            'user': os.getenv('TARGET_DB_USER'),
            'password': os.getenv('TARGET_DB_PASSWORD'),
            'host': os.getenv('TARGET_DB_HOST'),
            'port': os.getenv('TARGET_DB_PORT')
        }
    }

    return config
