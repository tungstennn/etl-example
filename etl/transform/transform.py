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
    return merged_data
