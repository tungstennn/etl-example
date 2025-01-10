import pytest
from unittest.mock import call
from etl.extract.extract_transactions import (
    extract_transactions,
    log_transactions_success
)


def test_extract_transactions_logs_error(mocker):
    # Mock the logger
    mock_logger = mocker.patch("etl.extract.extract_transactions.logger")

    # Patch the function to raise an exception
    mocker.patch(
        "etl.extract.extract_transactions.extract_transactions_execution",
        side_effect=Exception("Exception message")
    )

    # Test that the exception is raised
    with pytest.raises(Exception, match="Exception message"):
        extract_transactions()

    # Verify that the error was logged
    mock_logger.error.assert_called_once_with(
        "Failed to extract data: Exception message"
    )


def test_log_transactions_success(mocker):
    mock_logger = mocker.patch('etl.extract.extract_transactions.logger')
    transactions_shape = (10500, 4)
    execution_time = 0.5
    log_transactions_success(transactions_shape, execution_time)

    mock_logger.info.assert_has_calls([
        call("Data extraction successful!"),
        call(
            f"Extracted {transactions_shape[0]} rows "
            f"and {transactions_shape[1]} columns"
        ),
        call(f"Execution time: {execution_time} seconds"),
        call(
            f"Execution time per row: "
            f"{execution_time / transactions_shape[0]} seconds"
        )
    ])


def test_log_transaction_warnings(mocker):
    mock_logger = mocker.patch('etl.extract.extract_transactions.logger')
    transactions_shape = (10500, 4)
    execution_time = 11.5
    log_transactions_success(transactions_shape, execution_time)

    mock_logger.warning.assert_called_once_with(
        "Execution time per row exceeds 1ms: "
        f"{execution_time / transactions_shape[0]} seconds"
    )

