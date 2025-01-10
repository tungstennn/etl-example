import os
import pandas as pd
from config.db_config import load_db_config
from etl.extract.extract_query import execute_extract_query
from utils.sql_utils import import_sql_query
from utils.db_utils import get_db_connection

EXTRACT_TRANSACTIONS_QUERY_FILE = os.path.join(
    os.path.dirname(__file__),
    '../sql/extract_transactions.sql'
)
DB_CONFIG = load_db_config()


def extract_transactions() -> pd.DataFrame:
    # Import the SQL query
    # Connect to the database
    # Execute the query
    # Return the dataframe as a result

    query = import_sql_query(EXTRACT_TRANSACTIONS_QUERY_FILE)
    connection = get_db_connection(DB_CONFIG['source_database'])
    transactions_df = execute_extract_query(query, connection)
    connection.close()
    # print(transactions_df)
    # Initially added to debug during dev - remove before production
    return transactions_df
