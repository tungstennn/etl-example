import psycopg2
import logging
from utils.logging_utils import setup_logger


class DatabaseConnectionError(Exception):
    pass


class QueryExecutionError(Exception):
    pass


# Configure the logger
logger = setup_logger(__name__, '../../logs/database.log')


def get_db_connection(connection_params):
    try:
        connection = psycopg2.connect(**connection_params)
        logger.setLevel(logging.INFO)
        logger.info("Successfully connected to the database.")
        return connection
    except psycopg2.Error as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Failed to connect to the database: {e}")
        raise DatabaseConnectionError(
            f"Failed to connect to the database: {e}"
        )
