import pandas as pd
from etl.transform.clean_transactions import clean_transactions
from etl.transform.clean_customers import clean_customers


def transform_data(data) -> pd.DataFrame:
    cleaned_transactions = clean_transactions(data[0])
    cleaned_customers = clean_customers(data[1])
    merged_data = merge_transactions_customers(
        cleaned_transactions,
        cleaned_customers
    )
    return merged_data


def merge_transactions_customers(
    transactions: pd.DataFrame,
    customers: pd.DataFrame
) -> pd.DataFrame:
    merged_data = pd.merge(transactions, customers, on='customer_id')

    # Save the merged data to a CSV file
    merged_data.to_csv(
        '../../data/processed/merged_data.csv',
        index=False
    )

    return merged_data


"""
ADDITIONAL TESTS NEEDED TO BE DONE:

CLEANING:

Given the extracted data, when duplicates are removed, then 100% of duplicates should be removed.
Given the extracted data, when missing, then 100% of missing should be resolved.
Given the extracted data, when invalid values are handled, then 100% of invalid fields should be resolved.
Given the extracted data, when data cleaning is performed, then it should complete in less than 1 second per 1,000 rows.

DOCUMENTATION

"""  # noqa