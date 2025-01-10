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

""" This was causing errors when trying to set the environment!
Python sets this as soon as the module is imported
So when run_etl.py imports this module, it sets runs the function
Meaning that the environment variables are NOT set before the script is run
"""
# DB_CONFIG = load_db_config()
# Now called directly in the extract_transactions function


def extract_transactions() -> pd.DataFrame:
    # Import the SQL query
    # Connect to the database
    # Execute the query
    # Return the dataframe as a result
    connection_details = load_db_config()['source_database']
    query = import_sql_query(EXTRACT_TRANSACTIONS_QUERY_FILE)
    connection = get_db_connection(connection_details)
    transactions_df = execute_extract_query(query, connection)
    connection.close()
    # print(transactions_df)
    # Initially added to debug during dev - remove before production
    return transactions_df
