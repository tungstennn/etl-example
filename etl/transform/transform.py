import pandas as pd
from etl.transform.clean_transactions import clean_transactions
from etl.transform.clean_customers import clean_customers


def transform_data(data=None) -> pd.DataFrame:
    cleaned_transactions = clean_transactions(data)
    cleaned_customers = clean_customers(data)
    # merged_data = merge_transactions_customers(
    #     cleaned_transactions,
    #     cleaned_customers
    # )
    return (cleaned_transactions, cleaned_customers)


# def merge_transactions_customers(
#     transactions: pd.DataFrame,
#     customers: pd.DataFrame
# ) -> pd.DataFrame:
#     return pd.merge(transactions, customers, on='customer_id')
