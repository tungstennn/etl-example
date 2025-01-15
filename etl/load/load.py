import os
import pandas as pd
import logging
from config.db_config import load_db_config, DatabaseConfigError
from utils.db_utils import (
    get_db_connection,
    DatabaseConnectionError,
    QueryExecutionError
)
from utils.logging_utils import setup_logger
from etl.load.post_load_enrichment import enrich_database_data


# Configure the logger
logger = setup_logger(__name__, 'database_query.log', level=logging.DEBUG)


LOAD_QUERY_FILES = {
    'load_merged_data': os.path.join(
        os.path.dirname(__file__), 'load_merged_data.sql'),
    'load_high_value_customers': os.path.join(
        os.path.dirname(__file__), 'load_high_value_customers.sql'),
    'load_cleaned_high_value_customers': os.path.join(
        os.path.dirname(__file__), 'load_cleaned_high_value_customers.sql')
}


def load_data(data: tuple):
    (
        merged_data,
        high_value_customers,
        cleaned_high_value_customers
    ) = data

    # Save merged data to an SQL table in target database
    create_merged_data_table(merged_data)

    # Perform post-load enrichment of the data in the database
    enrich_database_data()

    return None


def create_merged_data_table(data: pd.DataFrame):
    try:
        connection_details = load_db_config()['target_database']
        connection = get_db_connection(connection_details)
        data.to_sql(
            'transactions_by_customers',
            connection,
            if_exists='replace',
            index=False
        )
    except DatabaseConfigError as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Target database not configured correctly: {e}")
        raise
    except DatabaseConnectionError as e:
        logger.setLevel(logging.ERROR)
        logger.error(
            f"Failed to connect to the database when creating merged table:"
            f" {e}"
        )
        raise
    except pd.errors.DatabaseError as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Failed to create merged data table: {e}")
        raise QueryExecutionError(f"Failed to execute query: {e}")
    finally:
        connection.close()
        logger.info("Successfully closed database connection.")
