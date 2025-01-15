import pandas as pd
from typing import Tuple
from etl.transform.clean_transactions import clean_transactions
from etl.transform.clean_customers import clean_customers
from utils.file_utils import save_dataframe_to_csv

HIGH_VALUE_LOWER_BOUND = 500


def transform_data(data) -> Tuple[pd.DataFrame]:
    cleaned_transactions = clean_transactions(data[0])
    cleaned_customers = clean_customers(data[1])
    merged_data = merge_transactions_customers(
        cleaned_transactions,
        cleaned_customers
    )
    # Create the aggregated data for high value customers
    # This approach would be suitable if the end users want us
    # to create separate tables of data in the database
    high_value_customers = get_high_value_customers(merged_data)
    save_dataframe_to_csv(
        high_value_customers,
        'etl/data/processed/',
        'high_value_customers.csv'
    )

    # Clean high-value customers to remove missing values for age /country
    # This approach would be suitable if the end users want us
    # to create separate tables of data in the database
    cleaned_high_value_customers = high_value_customers.dropna(
        subset=['age', 'country']
    )
    save_dataframe_to_csv(
        cleaned_high_value_customers,
        'etl/data/processed/',
        'cleaned_high_value_customers.csv'
    )

    return (merged_data, high_value_customers, cleaned_high_value_customers)


def merge_transactions_customers(
    transactions: pd.DataFrame,
    customers: pd.DataFrame
) -> pd.DataFrame:
    merged_data = pd.merge(transactions, customers, on='customer_id')

    # Save the merged data to a CSV file
    output_dir = 'etl/data/processed/'
    file_name = 'merged_data.csv'
    save_dataframe_to_csv(merged_data, output_dir, file_name)

    return merged_data


def get_high_value_customers(data: pd.DataFrame) -> pd.DataFrame:
    # Get the total transaction value for each customer
    data = data.groupby('customer_id').agg(
        total_spend=('amount', 'sum'),
        avg_transaction_value=('amount', 'mean'),
        name=('name', 'first'),
        age=('age', 'first'),
        country=('country', 'first'),
        is_active=('is_active', 'first')
    ).reset_index()

    # Get the high value customers
    high_value_customers = data[
        data['total_spend'] > HIGH_VALUE_LOWER_BOUND
    ]

    return high_value_customers


"""
ADDITIONAL FUNCTIONALITY NEEDED:

Logging

ADDITIONAL TESTS NEEDED TO BE DONE:

CLEANING:

Given the extracted data, when duplicates are removed, then 100% of duplicates should be removed.
Given the extracted data, when missing, then 100% of missing should be resolved.
Given the extracted data, when invalid values are handled, then 100% of invalid fields should be resolved.
Given the extracted data, when data cleaning is performed, then it should complete in less than 1 second per 1,000 rows.

DOCUMENTATION

"""  # noqa