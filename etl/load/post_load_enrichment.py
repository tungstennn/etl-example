import os
import logging
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from config.db_config import load_db_config
from utils.db_utils import create_db_engine
from utils.file_utils import INDEXES_PATH, QUERY_PATH
from utils.logging_utils import setup_logger
from utils.sql_utils import import_sql_query

# Configure the logger
logger = setup_logger(__name__, 'database_query.log', level=logging.DEBUG)

HIGH_VALUE_CUSTOMER_LOWER_LIMIT = {
    'total_spend_threshold': 500
}

QUERY_FILE_NAMES = {
    'hvcv': 'high_value_customers_view.sql',
    'hvccv': 'high_value_customers_cleaned_view.sql'
}


def enrich_database_data():
    apply_indexes()
    create_views()


def apply_indexes():
    # Access the etl/sql/indexes folder
    # For each SQL file in the folder:
    # Import the SQL query from the file
    # Create a connection to the target database
    # Execute the query to create the index
    # for each file in the folder INDEXES_PATH
    # read in the SQL and then execute it
    try:
        files = os.listdir(INDEXES_PATH)
        connection_details = load_db_config()['target_database']
        engine = create_db_engine(connection_details)
        Session = sessionmaker(bind=engine)
        session = Session()
        for file in files:
            sql = import_sql_query(os.path.join(INDEXES_PATH, file))
            executable_sql = text(sql)
            session.execute(executable_sql)
            logger.info(f"Index created: {file}")
        session.commit()
    except OSError as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Error accessing directory {INDEXES_PATH}: {e}")
        raise
    except Exception as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Error creating index: {e}")
        raise
    finally:
        session.close()


def create_views():
    # Create an SQL query in a file that creates a view of high value customers
    # Import the SQL query from the file
    # Create a connection to the target database
    try:
        for query_name, query_file in QUERY_FILE_NAMES.items():
            sql = import_sql_query(os.path.join(QUERY_PATH, query_file))
            executable_sql = text(sql)
            connection_details = load_db_config()['target_database']
            engine = create_db_engine(connection_details)
            Session = sessionmaker(bind=engine)
            session = Session()
            session.execute(
                executable_sql,
                HIGH_VALUE_CUSTOMER_LOWER_LIMIT
            )
            logger.info(f"{query_file} view created")
            session.commit()
    except Exception as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Error creating high value customers view: {e}")
        raise
    finally:
        session.close()
