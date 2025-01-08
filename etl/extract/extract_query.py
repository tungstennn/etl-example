import pandas as pd
import logging
from utils.logging_utils import setup_logger
from utils.db_utils import QueryExecutionError


# Configure the logger
logger = setup_logger(__name__, '../../logs/database_query.log')


def execute_extract_query(query, connection):
    try:
        return pd.read_sql_query(query, connection)
    except pd.errors.DatabaseError as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Failed to execute query: {e}")
        logger.error(f"The query that failed was: {query}")
        raise QueryExecutionError(f"Failed to execute query: {e}")
