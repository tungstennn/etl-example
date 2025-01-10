# ![Digital Futures Academy](https://github.com/digital-futures-academy/DataScienceMasterResources/blob/main/Resources/datascience-notebook-header.png?raw=`true`)

## ETL Pipeline Project Walkthrough

---

---

## Activity 6: Extract Data

In this activity, you will extract data from the source and load it into a pandas DataFrame, bearing in mind the User Story, Sub-Tasks, Acceptance Criteria and the Definition of Done.

---

## User Story

```txt
As a Data Analyst,   
I want access to a single, clean, and accurate dataset combining customer demographics and transaction data,   
So that I can analyze customer behaviour without worrying about data inconsistencies and can rely on it for analysis without manual checks.
```

## Definition of Done

### Code Quality

- Code follows the project's coding standards and best practices.
  - ***SQL***:
    - **Query Performance**: Queries should execute in less than 2 seconds for typical operations.
    - **Readability and Maintainability**: Queries should be formatted for readability with consistent indentation, meaningful aliases, and comments.
    - **Use of Best Practices**: Follow best practices such as avoiding `SELECT *`, using `JOIN`s appropriately, and ensuring proper *indexing*.
    - **Linting**: SQL code should be linted for syntax errors and compliance with best practices.
  - ***Python***:
    - **PEP 8 Compliance**: Code should follow PEP 8 guidelines. Use a linter (e.g., flake8) to ensure compliance.
    - **Code Readability**: Use meaningful variable names, consistent indentation, and comments to explain complex logic.
    - **Modularity**: Functions and classes should be used to encapsulate logic and promote reuse.
    - **Error Handling**: Use `try-except` blocks to handle exceptions and provide meaningful error messages.
  - ***Pandas***:
    - **Efficient Data Manipulation**: Use vectorised operations instead of loops for data manipulation.
    - **Memory Usage**: Use appropriate data types and avoid loading unnecessary data into memory.
    - **Data Validation**: Check for missing values, data types, and data ranges before performing operation
- Code is reviewed and approved by at least one other team member.
- Code is free of critical and high-severity bugs.

---

### Testing

- **Unit tests** are written and cover all new functionality.
- **Integration tests** are written and cover interactions between components.
- **Component tests** are written and validate individual parts of the system.
- All tests pass successfully.
- ***Test coverage*** meets the the ***90%*** threshold for the project.

---

### Documentation

- Code is documented with clear and concise comments.
- User-facing documentation is updated to reflect new or changed functionality.
- Any relevant diagrams or flowcharts are updated.

---

### Performance

- Performance benchmarks are met (e.g., data extraction and cleaning times are within acceptable limits).
  - **Database Extraction**: *Less than 1ms per row* for *10,500 rows* with *4 fields*.
  - **CSV Extraction**: *Less than 30 seconds* for *5,200 rows* with *5 columns*.
  - **Data Cleaning**: *Less than 1 second* per *1,000 rows*.
  - **Data Transformation**: *Joins* and *aggregations* take *less than 5 seconds* per *10,000 rows*.
  - **Data Loading**: *Less than 5 seconds* per *10,000 rows*.
  - **End-to-End Processing**: The entire ETL process *completes within 30 minutes* for a full dataset.
  - No significant performance regressions are introduced.

---

### Data Quality

- Data is validated for accuracy, completeness, and consistency.
  - **Accuracy**: *99%* of records are accurate.
  - **Completeness**: *100%* of expected columns and rows are present.
  - **Consistency**: *100%* of records have consistent formats and values.
  - **Integrity**: *100%* of records maintain integrity constraints.
  - **Error Rate**: *Less than 1%* error rate.
  - **Validation Time**: *Less than 1 second* per *1,000 rows*.
- Data cleaning rules are applied, and logs are generated for any issues encountered.
  - **Duplicate Removal Rate**: *100%* of duplicates removed (e.g., 0% duplicates remain).
  - **Null Handling Rate**: *100%* of missing or invalid fields resolved.
  - **Data Completeness**: *100%* of *expected* *columns* and *rows* are present.
  - **Data Consistency**: *100%* of records have consistent formats.
  - **Cleaning Time**: *Less than 1 second* per *1,000 rows*.
  - **Error Rate**: *Less than 1%* error rate.
- Data transformation logic is verified and tested.

---

### Deployment

- Code is deployed to the appropriate environment (e.g., staging, production).
- Deployment scripts and configurations are updated as needed.
- Deployment is verified and tested in the target environment.

---

### Acceptance Criteria

- All acceptance criteria for the user story are met.
- The user story is demonstrated to and accepted by the product owner or relevant stakeholders.

---

### Metrics and Monitoring

- Relevant metrics (e.g., record count accuracy, extraction performance) are collected and reviewed.
- Monitoring and alerting are set up for critical components.

---

### Compliance

- All work complies with relevant legal, regulatory, and security requirements.

---

---

## User Story Acceptance Criteria

### Data Extraction

- Given the database contains 10,500 rows with 4 fields, when the data is extracted, then it should complete in less than 1ms per row. #16
- Given the CSV file contains 5,200 rows with 5 columns, when the data is extracted, then it should complete in less than 30 seconds. #17

### Data Cleaning

- Given the extracted data, when duplicates are removed, then 100% of duplicates should be removed. #14
- Given the extracted data, when missing values are handled, then 100% of missing should be resolved. #12
- Given the extracted data, when invalid values are handled, then 100% of invalid fields should be resolved. #13
- Given the extracted data, when data cleaning is performed, then it should complete in less than 1 second per 1,000 rows. #15

### Data Transformation

- Given the cleaned data, when the customer demographics dataset (CSV) and transaction dataset (database) are merged, then the merge should be performed correctly using the customer_id field as the key. #18
- Given the cleaned data, when calculating the total amount spent by each customer, then the total_spent field should be accurate and reflect the sum of all amount values for each customer_id. #20
- Given the cleaned data, when filtering for active customers, then only customers with is_active set to True should be included. #19

### Data Quality

- Given the transformed dataset, when data validation is performed, then 99% of records should be accurate. #8
- Given the transformed dataset, when data validation is performed, then 100% of expected columns and rows should be present. #11
- Given the transformed dataset, when data validation is performed, then 100% of records should have consistent formats and values. #10
- Given the transformed dataset, when data validation is performed, then 100% of records should maintain integrity constraints. #9
- Given the transformed dataset, when data validation is performed, then it should complete in less than 1 second per 1,000 rows. advanced-sql#20

### Documentation - User Story 1 #22

- Code should be documented with clear and concise comments.
- User-facing documentation should be updated to reflect new or changed functionality.

### Testing Acceptance Criteria - User Story 1 #21

- Unit tests should cover all new functionality.
- Integration tests should cover interactions between components.
- All tests should pass successfully.
- Test coverage should meet the project's required threshold of 90%.

---

#### What's the Plan?

1. Extract data from the source.
2. Load the data into a pandas DataFrame.
3. Verify the data extraction process.
4. Document the data extraction process.

---

#### How do we Execute the Plan?

1. Extract data from the source.
   - Connect to the database.
   - Write a SQL query to extract the data.

---

#### What do we Need to Test?

Let's refer the the Acceptance Criteria checklists:

```txt
Given the database contains 10,500 rows with 4 fields,  
when the data is extracted,  
then it should complete in less than 1 minute.
```

- ***Performance Test***:
  - [ ] - Verify that the data extraction completes in less than 1ms per row (regardless of the number of rows).
- ***Functional Tests***:
  - [ ] - Verify that the data extraction retrieves exactly 4 fields per row.
- ***Data Integrity Tests***:
  - [ ] - Verify data consistency between the extracted data and the source database.
  - [ ] - Verify data accuracy for a sample of rows.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles a database connection error gracefully
  - [ ] - Verify that the code handles a database query error gracefully
  - [ ] - Verify that the code handles a database timeout error gracefully
- ***Code Quality Tests***:
  - [ ] - SQL queries pass linting and formatting checks.
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] Test coverage on the database extraction script is at least 90%.

---

#### What do we Already Know?

1. The database connection details - supplied by the `db_config.py` file.
2. Extract all fields and rows from the transactions table in the database.
3. The expected number of rows and fields in the database.
4. The expected time for data extraction.

---

#### Test-Driven Development Opportunities

Let's think about the functionality of the code and what we expect.

In connecting the database, our previous experience is that we need to use a library call to `connect` to the database and that we will return some form of `connection` object.

We also know that the `connect` function requires some details of the database to connect to, so we can write a test that asserts that the `connect` function is called as part of our database connection function.

The second thing we can assert here is that our function returns the connection object created by the `connect` function.

In the first instance, we can now test drive a ***unit test*** for creating a database connection, where we will mock the `connect` function and it's return.

> Remember:
>
> Test-driven development has 3 rules:
>
> 1. You are not allowed to write any production code unless it is to make a failing unit test pass.
> 2. You are not allowed to write any more of a unit test than is sufficient to fail, and compilation failures are failures.
> 3. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

<!--
```python
import pytest
from unittest.mock import patch, MagicMock
from db_utils import get_db_connection

def test_get_db_connection(mocker):
    connection_params = {
        'dbname': 'test_db',
        'user': 'test_user',
        'password': 'test_password',
        'host': 'test_host',
        'port': 'test_port'
    }

    mock_connection = MagicMock()
    mock_connect = mocker.patch('psycopg2.connect', return_value=mock_connection)

    connection = get_db_connection(connection_params)

    mock_connect.assert_called_once_with(**connection_params)
    assert connection == mock_connection
```
-->

Once the test is written and failing (as we haven't written the `get_db_connection` function yet), we can write the function to make the test pass.

<!--
```python
import psycopg2

def get_db_connection(connection_params):
    return psycopg2.connect(**connection_params)
```
-->

#### Error Conditions

And then we should consider error conditions.  What happens if:

- The connection details are incorrect?
- The database is not available?
- The database is not accepting connections?
- The connection times out?

<!--
```python
import psycopg2

class DatabaseConnectionError(Exception):
    pass

def get_db_connection(connection_params):
    try:
        return psycopg2.connect(**connection_params)
    except psycopg2.Error as e:
        raise DatabaseConnectionError(f"Failed to connect to the database: {e}")

import pytest
from unittest.mock import patch, MagicMock
import logging
from db_utils import get_db_connection, DatabaseConnectionError

def test_get_db_connection_success(mocker):
    connection_params = {
        'dbname': 'test_db',
        'user': 'test_user',
        'password': 'test_password',
        'host': 'test_host',
        'port': 'test_port'
    }

    mock_connection = MagicMock()
    mock_connect = mocker.patch('psycopg2.connect', return_value=mock_connection)
    mock_logger = mocker.patch('db_utils.logging.getLogger')

    connection = get_db_connection(connection_params)

    mock_connect.assert_called_once_with(**connection_params)
    assert connection == mock_connection
    mock_logger().info.assert_called_once_with("Successfully connected to the database.")

def test_get_db_connection_failure(mocker):
    connection_params = {
        'dbname': 'test_db',
        'user': 'test_user',
        'password': 'test_password',
        'host': 'test_host',
        'port': 'test_port'
    }

    mock_connect = mocker.patch('psycopg2.connect', side_effect=psycopg2.Error("Connection error"))
    # mock_logger = mocker.patch('db_utils.logging.getLogger')

    with pytest.raises(DatabaseConnectionError) as excinfo:
        get_db_connection(connection_params)

    assert str(excinfo.value) == "Failed to connect to the database: Connection error"
    mock_connect.assert_called_once_with(**connection_params)
    # mock_logger().error.assert_called_once_with("Failed to connect to the database: Connection error")
```
-->

#### Logging

Let's look back at Acceptance Criteria - Logging and Monitoring are set up for critical components.  We should consider logging these errors to a file for the time being.  We can set up a logger for use across the application.  Since this is configuration, there is no real need to test that this works but it should be linted correctly.  We want to log to the console and to a file.  Console logging is useful for debugging and file logging is useful for monitoring.

The logger is set up here: [logging_utils.py](../utils/logging_utils.py)

We will then call `setup_logger` in any file we want to use the logger in and supply the logger name and the log file to write to.

This will help us to meet the following Definition of Done criteria:

```markdown
### Metrics and Monitoring

- Relevant metrics (e.g., record count accuracy, extraction performance) are collected and reviewed.
- Monitoring and alerting are set up for critical components.
```

### Testing that Logging Happens in the Database Connection Function

We should test that the logging happens both on success and failure.  We can mock the logger and assert that the `info` and `error` methods are called at appropriate times.  As we are reusing the connection details in the tests, we will make them a fixture.

<!--
```python
import pytest
import psycopg2
from unittest.mock import MagicMock
from utils.db_utils import get_db_connection, DatabaseConnectionError

@pytest.fixture
def connection_params():
    return {
        'dbname': 'test_db',
        'user': 'test_user',
        'password': 'test_password',
        'host': 'test_host',
        'port': 'test_port'
    }

def test_get_db_connection_success(mocker, connection_params):
    mock_connection = MagicMock()
    mock_connect = mocker.patch(
        'psycopg2.connect', return_value=mock_connection
    )

    connection = get_db_connection(connection_params)

    mock_connect.assert_called_once_with(**connection_params)
    assert connection == mock_connection

def test_get_db_connection_success_logging(mocker, connection_params):
    mock_logger = mocker.patch('utils.db_utils.logger')
    mock_connection = MagicMock()
    mocker.patch('psycopg2.connect', return_value=mock_connection)

    get_db_connection(connection_params)

    mock_logger.info.assert_called_once_with(
        "Successfully connected to the database."
    )

def test_get_db_connection_failure(mocker, connection_params):
    mock_connect = mocker.patch(
        'psycopg2.connect',
        side_effect=psycopg2.Error("Connection error")
    )
    mock_logger = mocker.patch('utils.db_utils.logger')

    with pytest.raises(DatabaseConnectionError) as excinfo:
        get_db_connection(connection_params)

    assert str(excinfo.value) == (
        "Failed to connect to the database: Connection error"
    )
    mock_connect.assert_called_once_with(**connection_params)
    mock_logger.error.assert_called_once_with(
        "Failed to connect to the database: Connection error"
    )

```
-->

We then need to write the production code to make the tests pass.

<!--
```python
import psycopg2
import logging
from utils.logging_utils import setup_logger

class DatabaseConnectionError(Exception):
    pass

# Configure the logger
logger = setup_logger(__name__, '../../logs/database.log')

def get_db_connection(connection_params):
    try:
        connection = psycopg2.connect(**connection_params)
        logger.setLevel(logging.INFO)
        logger.info("Successfully connected to the database.")
        return connection
    except psycopg2.Error as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Failed to connect to the database: {e}")
        raise DatabaseConnectionError(
            f"Failed to connect to the database: {e}"
        )
```
--->

---

### How about an Integration Test?

We can also write an integration test to ensure that the database connection is working as expected.  We should try connect to our test database and assert that we can connect successfully.  Its an integration test as we are combining 2 bits of code with an external system to make sure that they work together.

<!--
```python
import pytest
from db_utils import get_db_connection
from config.db_config import get_db_config, DatabaseConnectionError

def test_db_connection():
    connection_params = get_db_config()['source_database']
    connection = get_db_connection(connection_params)

    # Assert that the connection has a cursor method
    assert hasattr(connection, 'cursor')

    # Optionally, you can also check if the connection is open
    assert connection.closed == 0  # 0 means the connection is open

    # Clean up by closing the connection
    connection.close()
```
-->

#### Edge Cases

When testing database connections, we should consider the following edge cases:

1. **Invalid Connection Parameters:**
   - Test with incorrect database name, user, password, host, or port to ensure the function handles connection failures gracefully.
2. **Database Unavailability:**
   - Test when the database server is down or unreachable to ensure the function handles this scenario properly.
3. **Timeouts:**
   - Test for connection timeouts to ensure the function handles slow or unresponsive database servers.
4. **Environment Variables Missing:**
   - Test when required environment variables are missing to ensure the function handles this scenario properly.
5. **Connection Already Closed:**
   - Test the behaviour when trying to use a connection that has already been closed.

<!--
```python
import pytest
from db_utils import get_db_connection, DatabaseConnectionError
from config.db_config import get_db_config

def test_db_connection_success():
    connection_params = get_db_config()['source_database']
    connection = get_db_connection(connection_params)

    # Assert that the connection has a cursor method
    assert hasattr(connection, 'cursor')

    # Optionally, you can also check if the connection is open
    assert connection.closed == 0  # 0 means the connection is open

    # Clean up by closing the connection
    connection.close()

def test_db_connection_invalid_params():
    connection_params = {
        'dbname': 'invalid_db',
        'user': 'invalid_user',
        'password': 'invalid_password',
        'host': 'invalid_host',
        'port': 'invalid_port'
    }

    with pytest.raises(DatabaseConnectionError):
        get_db_connection(connection_params)

def test_db_connection_unavailable():
    connection_params = get_db_config()['source_database']
    connection_params['host'] = 'unreachable_host'

    with pytest.raises(DatabaseConnectionError):
        get_db_connection(connection_params)

def test_db_connection_timeout(mocker):
    connection_params = get_db_config()['source_database']
    mocker.patch('psycopg2.connect', side_effect=psycopg2.OperationalError("timeout"))

    with pytest.raises(DatabaseConnectionError):
        get_db_connection(connection_params)

def test_db_connection_missing_env_vars(mocker):
    mocker.patch.dict('os.environ', {}, clear=True)
    with pytest.raises(KeyError):
        get_db_config()

def test_db_connection_already_closed():
    connection_params = get_db_config()['source_database']
    connection = get_db_connection(connection_params)
    connection.close()

    assert connection.closed == 1  # 1 means the connection is closed
    with pytest.raises(psycopg2.InterfaceError):
        connection.cursor()

```
-->

See the [Activity-6-Solution](./activity-6-solution.md#refactoring) for the full code.

---

### Linting Python Code

We can run the command `run_test lint` to see if our code passes just the linting test.

The linting section of the `run_tests.py` script has been modified to ensure that a linting error stops the process and returns a non-zero exit code.

We have added the linting to the script that executes all other tests, so that the code is linted each time the tests are run.  The tests run will not pass if linting fails.

[run_tests.py](../tests/run_tests.py)

You will notice that we have the following config file linting option called `.flake8`.  This contains a list of directories to exclude from linting.  We can also add options here to ignore certain rules, errors or warnings.

[.flake8](../.flake8)

We have also added a `.coveragerc` file to the project so that we can clean up the original string in the `run_tests.py` script and have the configuration in a separate file.

[.coveragerc](../.coveragerc)

---

### State of Play

So far we have addressed accessing the database and are now confident that as long as the correct environment variables are set and the database is available, we can connect to it.

We have covered off the following items from the Acceptance Criteria:

- ***Reliability Tests***:
  - [ ] - Verify that the code handles a database connection error gracefully
  - [ ] - Verify that the code handles a database timeout error gracefully
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ - ] Test coverage on the database extraction script is at least 90%.

We will, of course, need to keep an eye on the Code Quality Tests as we add more code to the project, but so far so good!

---

### Next Steps

The next step is to write the SQL query to extract the data from the database.  We will need to consider the following from the Acceptance Criteria::

- ***Performance Test***:
  - [ ] - Verify that the data extraction completes in less than 1 minute (regardless of the number of rows).
- ***Functional Tests***:
  - [ ] - Verify that the data extraction retrieves exactly 4 fields per row.
- ***Data Integrity Tests***:
  - [ ] - Verify data consistency between the extracted data and the source database.
  - [ ] - Verify data accuracy for a sample of rows.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles a database query error gracefully
- ***Code Quality Tests***:
  - [ ] - SQL queries pass linting and formatting checks.
  - [ ] - Python scripts pass linting and formatting checks.
  - [ - ] Test coverage on the database extraction script is at least 90%.

We will also need to consider any of the Acceptance Criteria for the User Story and the Definition of Done (such as logging metrics, etc).

---

### Approach

1. Write the SQL query to extract the data from the database.
2. Write a function to import the SQL query.
3. Write a function to use the imported query to create a Pandas DataFrame.
4. Write tests to verify the functionality of the functions.
5. Write tests to verify the performance of the functions.
6. Write tests to ensure the reliability of the functions in error cases.

---

### SQL Query

The database contains a table called `transactions` with the following fields:

- `transaction_id`: The unique identifier for each transaction.
- `customer_id`: The unique identifier for the customer for the transaction.
- `amount`: The value of each transaction.
- `transaction_date`: The date the transaction was recorded on.

To follow the linting rules, we need to make sure we don't use a `SELECT *`. To help with linting and code maintainability, we'll write the SQL in a `.sql` file and then import this.  This file will line in the `sql` folder in the `etl` folder.

To be able to lint this using ***SQLFluff*** our run tests script has some code to detect and lint the SQL files we place here.  We have also created a `.sqlfluff` file to ignore certain rules, errors or warnings and provide a other rules for our particular project.

---

### QUICK QUESTION

> What is the SQL query that we need to write to extract the data from the database?
>
> Answers in CHAT please!

---

## Executing the SQL Query in Python

We will need to write a function to execute the SQL query and return the results.  We will also need to write tests to verify the functionality of the function.

The tests we need can be anticipated, so we can test-drive the function by writing the tests first.  But first we can unit test that the SQL query is imported and that we call the query.  We are going to be importing the result into a pandas DataFrame, so we can verify our logic before integrating by verifying that the function we write calls the pandas `read_sql_query` function.  The function will need to take a query and a connection object as parameters and we'll mock these in our unit test before using the actual query and connection object in our integration test.

<!--
```python
from unittest.mock import MagicMock
from etl.extract.extract_query import execute_extract_query

def test_function_calls_pandas_read_sql_query(mocker):
    mock_read_sql = mocker.patch('pandas.read_sql_query')
    mock_connection = MagicMock()
    query = "SELECT * FROM transactions"

    execute_extract_query(query, mock_connection)

    mock_read_sql.assert_called_once_with(query, mock_connection)

```
-->

Once we have the failing test, we can go about passing it by writing the function.

<!--
```python
import pandas as pd

def execute_extract_query(query, connection):
    pd.read_sql_query(query, connection)

```
-->

Now we think about error cases - what happens if the query is incorrect, or the connection is closed, or the connection is invalid?

Write tests for the scenario and then verify that the production code handles the error - don't forget the logging requirements!

1. Test that the function raises an exception if the query is invalid - the exception should be a `QueryExecutionError` - which is a custom error we will need to write.

<!--
```python
import pytest
from etl.extract.extract_query import execute_extract_query, QueryExecutionError

def test_execute_extract_query_invalid_query(mocker):
    mock_read_sql = mocker.patch('pandas.read_sql_query', side_effect=pd.errors.DatabaseError("Invalid query"))
    mock_connection = MagicMock()
    query = "SELECT * FROM transactions"

    with pytest.raises(QueryExecutionError):
        execute_extract_query(query, mock_connection)

    mock_read_sql.assert_called_once_with(query, mock_connection)
```

<!--
```python
import pandas as pd

class QueryExecutionError(Exception):
    pass

def execute_extract_query(query, connection):
    try:
        return pd.read_sql_query(query, connection)
    except pd.errors.DatabaseError as e:
        raise QueryExecutionError(f"Failed to execute query: {e}")

```
-->

1. Test that the error is logged when the query is invalid.

<!--
```python
import pytest

import pandas as pd
from unittest.mock import MagicMock, call
from etl.extract.extract_query import (
    execute_extract_query,
    QueryExecutionError
)

def test_execute_extract_query_invalid_query_logging(mocker):
    # Mock the logger
    mock_logger = mocker.patch('etl.extract.extract_query.logger')

    # Mock the pandas read_sql_query function to raise a DatabaseError
    mocker.patch(
        'pandas.read_sql_query',
        side_effect=pd.errors.DatabaseError("Invalid query")
    )
    mock_connection = MagicMock()
    query = "SELECT unrecognized_column FROM transactions"

    with pytest.raises(QueryExecutionError):
        execute_extract_query(query, mock_connection)

    print(mock_logger.error.call_args_list)

    mock_logger.error.assert_has_calls([
        call("Failed to execute query: Invalid query"),
        call(f"The query that failed was: {query}")
    ])
```
-->

<!--
```python
import pandas as pd
import logging
from utils.logging_utils import setup_logger

class QueryExecutionError(Exception):
    pass

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
```
-->

We will log the other metrics required here when we have more of the function written.

---

### Write a utils function to import the SQL query passing in the filename

We can write a function to import the SQL query from a file.  This will help with linting and code maintainability.  There is no need to unit test the import part function as it will be covered in a later integration test.  We should however, log the import of the query and its success or failure and test that this is done correctly!

<!--
```python
import pytest
from utils.db_utils import QueryExecutionError
from utils.sql_utils import import_sql_query

def test_import_sql_query_success_logging(mocker):
    # Setup
    filename = "tests/unit_tests/test_data/test_query.sql"
    expected_query = "SELECT * FROM test_table"
    mocker.patch("builtins.open", mocker.mock_open(read_data=expected_query))
    mock_logger = mocker.patch("utils.sql_utils.logger")

    # Run
    result = import_sql_query(filename)

    # Check
    mock_logger.info.assert_called_once_with(
        f"Successfully imported query from {filename}"
    )
    assert result == expected_query

def test_import_sql_query_failure_logging(mocker):
    # Setup
    filename = "tests/unit_tests/test_data/missing_query.sql"
    error_message = f"Failed to import query: {filename} not found"
    mocker.patch(
        "builtins.open",
        side_effect=FileNotFoundError(error_message)
    )
    mock_logger = mocker.patch("utils.sql_utils.logger")

    # Run and check
    with pytest.raises(QueryExecutionError):
        import_sql_query(filename)

    mock_logger.error.assert_called_once_with(error_message)
```
-->

The failing tests lead us to write the function.

<!--
```python
import logging
from utils.logging_utils import setup_logger
from utils.db_utils import QueryExecutionError

logger = setup_logger(__name__, '../logs/database_query.log')

def import_sql_query(filename):
    try:
        with open(filename, 'r') as file:
            imported_query = file.read().replace('\n', ' ').strip()
            logger.info(f"Successfully imported query from {filename}")
            return imported_query
    except FileNotFoundError as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Failed to import query: {filename} not found")
        raise QueryExecutionError(f"Failed to import query: {e}")
```
-->

---

#### Progress Check

- [x] - 1. Create a connection to the database.
- [x] - 2. Write a SQL query to extract the data.
- [x] - 3. Write a function to import the SQL query.
- [x] - 4. Write a function to execute the SQL query.
- [ ] - 5. Put them all together to extract the transactions data.

---

### 5. Put them all together to extract the transactions data

We can now write a function to put all of this together to extract the transactions data.  We will need to write tests to verify the functionality of the function.

This file will live in the `etl/extract` folder and will be called `extract_transactions.py`.

It will be tested via integration - although we will need to add some logging to the successful part of the execute_extract_query function to meet the Acceptance Criteria and Definition of Done.

We will also need to write tests to verify the performance of the function and to ensure the criteria for these are met.

These Acceptance Criteria are:

### Data Extraction

- Given the database contains 10,500 rows with 4 fields, when the data is extracted, then it should complete in less than ***1ms per row***. #16

---

----

### Summary of New Files and Existing File Changes for Extracting Transactions

#### New Production Files

1. [etl/sql/extract_transactions.sql](../etl/sql/extract_transactions.sql)
   - Contains:
     - The SQL query to extract all 4 fields for all records from the transactions table in the database.
2. [utils/sql_utils.py](../utils/sql_utils.py)
   - Contains:
     - Function to import the SQL query from a file. (`utils.sql_utils.import_sql_query()`)
3. [etl/extract/extract_query.py](../etl/extract/extract_query.py)
   - Contains:
     - Call to run the query and return the results as a DataFrame. (`etl.extract.extract_query.execute_extract_query()`)
4. [extract_transactions.py](../etl/extract/extract_transactions.py)
   - Contains calls to:
     - Import the SQL query (`utils.sql_utils.import_sql_query()`)
     - Connect to the database (`utils.db_utils.get_db_connection()`)
     - Execute the query and return the DataFrame as a result (`etl.extract.extract_query.execute_extract_query()`)

#### Modified Production Files

1. [utils/db_utils.py](../utils/db_utils.py)
   - Added a custom exception for query execution errors. (`utils.db_utils.QueryExecutionError`)
2. [etl/extract/extract.py](../etl/extract/extract.py)
   - Set up a logger for this module. (`etl.extract.extract.logger`)
   - Added a try/except block
     - `try` block:
       - Set up performance recording.
       - Get the transactions data from the source (call to `etl.extract.extract_transactions()`)
       - Log the success of the data extraction.
     - `except` block:
       - Log the failure of the data extraction.
       - Raise an Exception to be handled by the calling function.
   - Added a function called `log_transactions_success()` to log the success of the data extraction.
      - Logs success
      - Logs the number of rows and columns extracted
      - Logs the time taken to extract the data
      - Logs the performance of the data extraction
        - If the performance is above the threshold, logs an info message
        - If the performance is below the threshold, logs a warning

---

#### New Test Files

#### Unit Tests

1. [tests/unit_tests/test_extract_query.py](../tests/unit_tests/test_extract_query.py)
   - Contains tests:
     - `test_function_calls_pandas_read_sql_query()`
     - `test_execute_extract_query_invalid_query()`
     - `test_execute_extract_query_invalid_query_logging()`
2. [tests/unit_tests/test_sql_utils.py](../tests/unit_tests/test_sql_utils.py)
   - Contains tests:
     - `test_import_sql_query_success_logging()`
     - `test_import_sql_query_failure_logging()`

#### Integration Tests

1. [tests/integration_tests/test_extract_transactions_integration.py](../tests/integration_tests/test_extract_transactions_integration.py)
   - Contains tests:
     - `test_extract_transactions_returns_all_data()`
     - `test_extract_transactions_performance()`

---

## User Story 1 Progress Check

### Definition of Done

[/] Means ***IN PROGRESS*** and [x] means ***DONE***.

#### Code Quality

- Code follows the project's coding standards and best practices.
  - ***SQL***:
    - [/] - **Query Performance**: Queries should execute in less than 2 seconds for typical operations.
    - [/] - **Readability and Maintainability**: Queries should be formatted for readability with consistent indentation, meaningful aliases, and comments.
    - [/] - **Use of Best Practices**: Follow best practices such as avoiding `SELECT *`, using `JOIN`s appropriately, and ensuring proper *indexing*.
    - [/] - **Linting**: SQL code should be linted for syntax errors and compliance with best practices.
  - ***Python***:
    - [/] - **PEP 8 Compliance**: Code should follow PEP 8 guidelines. Use a linter (e.g., flake8) to ensure compliance.
    - [/] - **Code Readability**: Use meaningful variable names, consistent indentation, and comments to explain complex logic.
    - [/] - **Modularity**: Functions and classes should be used to encapsulate logic and promote reuse.
    - [/] - **Error Handling**: Use `try-except` blocks to handle exceptions and provide meaningful error messages.
  - ***Pandas***:
    - **Efficient Data Manipulation**: Use vectorised operations instead of loops for data manipulation.
    - **Memory Usage**: Use appropriate data types and avoid loading unnecessary data into memory.
    - **Data Validation**: Check for missing values, data types, and data ranges before performing operation
- Code is reviewed and approved by at least one other team member.
- Code is free of critical and high-severity bugs.

---

### Testing

- [/] - **Unit tests** are written and cover all new functionality.
- [/] - **Integration tests** are written and cover interactions between components.
- **Component tests** are written and validate individual parts of the system.
- [/] - All tests pass successfully.
- [/] - ***Test coverage*** meets the the ***90%*** threshold for the project.

---

### Documentation

- [/] -Code is documented with clear and concise comments.
- User-facing documentation is updated to reflect new or changed functionality.
- [/] -Any relevant diagrams or flowcharts are updated.

---

### Performance

- Performance benchmarks are met (e.g., data extraction and cleaning times are within acceptable limits).
  - [x] **Database Extraction**: *Less than 1ms per row* for *rows* with *4 fields*.
  - **CSV Extraction**: *Less than 30 seconds* for *5,200 rows* with *5 columns*.
  - **Data Cleaning**: *Less than 1 second* per *1,000 rows*.
  - **Data Transformation**: *Joins* and *aggregations* take *less than 5 seconds* per *10,000 rows*.
  - **Data Loading**: *Less than 5 seconds* per *10,000 rows*.
  - **End-to-End Processing**: The entire ETL process *completes within 30 minutes* for a full dataset.
  - No significant performance regressions are introduced.

---

### Data Quality

- Data is validated for accuracy, completeness, and consistency.
  - **Accuracy**: *99%* of records are accurate.
  - **Completeness**: *100%* of expected columns and rows are present.
  - **Consistency**: *100%* of records have consistent formats and values.
  - **Integrity**: *100%* of records maintain integrity constraints.
  - **Error Rate**: *Less than 1%* error rate.
  - **Validation Time**: *Less than 1 second* per *1,000 rows*.
- Data cleaning rules are applied, and logs are generated for any issues encountered.
  - **Duplicate Removal Rate**: *100%* of duplicates removed (e.g., 0% duplicates remain).
  - **Null Handling Rate**: *100%* of missing or invalid fields resolved.
  - **Data Completeness**: *100%* of *expected* *columns* and *rows* are present.
  - **Data Consistency**: *100%* of records have consistent formats.
  - **Cleaning Time**: *Less than 1 second* per *1,000 rows*.
  - **Error Rate**: *Less than 1%* error rate.
- Data transformation logic is verified and tested.

---

### Deployment

- Code is deployed to the appropriate environment (e.g., staging, production).
- Deployment scripts and configurations are updated as needed.
- Deployment is verified and tested in the target environment.

---

## Acceptance Criteria

### Data Extraction

- [x] - Given the database contains 10,500 rows with 4 fields, when the data is extracted, then it should complete in less than 1ms per row. #16

#### Checklist

- ***Performance Test***:
  - [x] - Verify that the data extraction completes in less than 1 minute (regardless of the number of rows).
- ***Functional Tests***:
  - [x] - Verify that the data extraction retrieves exactly 4 fields per row.
- ***Data Integrity Tests***:
  - [x] - Verify data consistency between the extracted data and the source database.
  - [x] - Verify data accuracy for a sample of rows.
- ***Reliability Tests***:
  - [x] - Verify that the code handles a database connection error gracefully
  - [x] - Verify that the code handles a database query error gracefully
  - [x] - Verify that the code handles a database timeout error gracefully
- ***Code Quality Tests***:
  - [x] - SQL queries pass linting and formatting checks.
  - [x] - Python scripts pass linting and formatting checks.
  - [x] - Test coverage on the database extraction script is at least 90%.
