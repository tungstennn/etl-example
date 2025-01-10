import logging
import timeit
from etl.extract.extract_transactions import extract_transactions
from utils.logging_utils import setup_logger

# Configure the logger
logger = setup_logger(
    __name__,
    'extract_data.log',
    level=logging.DEBUG
)


def extract_data():
    try:
        # Set up performance recording for transaction extraction
        start_time = timeit.default_timer()
        transactions = extract_transactions()
        extract_transactions_execution_time = (
            timeit.default_timer() - start_time
        )

        log_transactions_success(
            transactions.shape,
            extract_transactions_execution_time
        )
    except Exception as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Failed to extract data: {e}")
        raise Exception(f"Failed to extract data: {e}")


def log_transactions_success(transactions_shape, execution_time):
    logger.setLevel(logging.INFO)
    logger.info("Data extraction successful!")
    logger.info(
        f"Extracted {transactions_shape[0]} rows "
        f"and {transactions_shape[1]} columns"
    )
    logger.info(f"Execution time: {execution_time} seconds")

    if (execution_time / transactions_shape[0] <= 0.001):
        logger.info(
            "Execution time per row: "
            f"{execution_time / transactions_shape[0]} seconds"
        )
    else:
        logger.setLevel(logging.WARNING)
        logger.warning(
            "Execution time per row exceeds 1ms: "
            f"{execution_time / transactions_shape[0]} seconds"
        )
