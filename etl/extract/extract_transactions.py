import logging
import os
import pandas as pd
import timeit
from config.db_config import load_db_config
from etl.extract.extract_query import execute_extract_query
from utils.sql_utils import import_sql_query
from utils.db_utils import get_db_connection
from utils.logging_utils import setup_logger, log_extract_success

# Configure the logger
logger = setup_logger(
    __name__,
    'extract_data.log',
    level=logging.DEBUG
)

EXTRACT_TRANSACTIONS_QUERY_FILE = os.path.join(
    os.path.dirname(__file__),
    '../sql/extract_transactions.sql'
)

EXPECTED_IMPORT_RATE = 0.001

TYPE = 'TRANSACTIONS from database'


def extract_transactions() -> pd.DataFrame:
    try:
        # Set up performance recording for transaction extraction
        start_time = timeit.default_timer()
        transactions = extract_transactions_execution()
        extract_transactions_execution_time = (
            timeit.default_timer() - start_time
        )

        log_extract_success(
            logger,
            TYPE,
            transactions.shape,
            extract_transactions_execution_time,
            EXPECTED_IMPORT_RATE
        )
        return transactions
    except Exception as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Failed to extract data: {e}")
        raise Exception(f"Failed to extract data: {e}")


def extract_transactions_execution() -> pd.DataFrame:
    # Import the SQL query
    # Connect to the database
    # Execute the query
    # Return the dataframe as a result
    connection_details = load_db_config()['source_database']
    print(connection_details)
    query = import_sql_query(EXTRACT_TRANSACTIONS_QUERY_FILE)
    connection = get_db_connection(connection_details)
    transactions_df = execute_extract_query(query, connection)
    connection.close()
    # print(transactions_df)
    # Initially added to debug during dev - remove before production
    return transactions_df


# def log_transactions_success(transactions_shape, execution_time):
#     logger.setLevel(logging.INFO)
#     logger.info("Data extraction successful!")
#     logger.info(
#         f"Extracted {transactions_shape[0]} rows "
#         f"and {transactions_shape[1]} columns"
#     )
#     logger.info(f"Execution time: {execution_time} seconds")

#     if (execution_time / transactions_shape[0] <= EXPECTED_IMPORT_RATE):
#         logger.info(
#             "Execution time per row: "
#             f"{execution_time / transactions_shape[0]} seconds"
#         )
#     else:
#         logger.setLevel(logging.WARNING)
#         logger.warning(
#             F"Execution time per row exceeds {EXPECTED_IMPORT_RATE}: "
#             f"{execution_time / transactions_shape[0]} seconds"
#         )
