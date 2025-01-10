import timeit
from etl.extract.extract_transactions import extract_transactions


def test_extract_transactions_returns_all_data():
    expected_shape = (10500, 4)
    # Call the function to get the DataFrame
    df = extract_transactions()

    # Verify the dimensions of the DataFrame
    assert df.shape == expected_shape, (
        f"Expected DataFrame shape to be {expected_shape}, but got {df.shape}"
    )


def test_extract_transaction_performance():
    # Note the change in the performance expectation
    expected_execution_time_per_row = 0.001  # i.e. 1ms per row
    # Measure the execution time
    execution_time = timeit.timeit(
        "extract_transactions()",
        globals=globals(),
        number=1
    )

    # Call the function to get the DataFrame
    df = extract_transactions()

    # Mean Time per Row
    actual_execution_time_per_row = execution_time / df.shape[0]

    # Assert that the execution time is within an acceptable range
    assert actual_execution_time_per_row <= expected_execution_time_per_row, (
        f"Expected execution time to be less than or equal to "
        f"{str(expected_execution_time_per_row)} seconds, but got "
        f"{str(actual_execution_time_per_row)} seconds"
    )
