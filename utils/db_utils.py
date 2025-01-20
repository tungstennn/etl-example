from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError, OperationalError
import logging
from utils.logging_utils import setup_logger


class DatabaseConnectionError(Exception):
    pass


class QueryExecutionError(Exception):
    pass


# Configure the logger
logger = setup_logger(__name__, 'database.log', level=logging.DEBUG)


# Issues being caused by using psycopg2 - better refactor to use SQLAlchemy
# def get_db_connection(connection_params):
#     try:
#         connection = psycopg2.connect(**connection_params)
#         logger.setLevel(logging.INFO)
#         logger.info("Successfully connected to the database.")
#         return connection
#     except psycopg2.Error as e:
#         logger.setLevel(logging.ERROR)
#         logger.error(f"Failed to connect to the database: {e}")
#         raise DatabaseConnectionError(
#             f"Failed to connect to the database: {e}"
#         )


def get_db_connection(connection_params):
    try:
        engine = create_db_engine(connection_params)
        connection = engine.connect()
        logger.setLevel(logging.INFO)
        logger.info("Successfully connected to the database.")
        return connection
    except OperationalError as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Operational error when connecting to the database: {e}")
        raise DatabaseConnectionError(
            f"Operational error when connecting to the database: {e}"
        )
    except SQLAlchemyError as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Failed to connect to the database: {e}")
        raise DatabaseConnectionError(
            f"Failed to connect to the database: {e}"
        )
    except Exception as e:
        raise Exception(f"An error occurred: {e}")


def create_db_engine(connection_params):
    try:
        if (
            not connection_params.get('user') or
            not connection_params.get('dbname') or
            not connection_params.get('host') or
            not connection_params.get('port')
        ):
            raise ValueError('User not provided')

        engine = create_engine(
            f"postgresql+psycopg2://{connection_params['user']}"
            f":{connection_params['password']}@{connection_params['host']}"
            f":{connection_params['port']}/{connection_params['dbname']}"
        )
        logger.setLevel(logging.INFO)
        logger.info("Successfully created the database engine.")
        return engine
    except ValueError as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Invalid Connection Parameters: {e}")
        raise DatabaseConnectionError(
            f"Invalid Connection Parameters: {e}"
        )
