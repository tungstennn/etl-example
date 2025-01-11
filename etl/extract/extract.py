import pandas as pd
from etl.extract.extract_transactions import extract_transactions
from etl.extract.extract_customers import extract_customers


def extract_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    transactions = extract_transactions()
    customers = extract_customers()
    print(transactions)
    print(customers)
    return (transactions, customers)
