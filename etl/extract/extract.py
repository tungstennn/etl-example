import pandas as pd
from etl.extract.extract_transactions import extract_transactions


def extract_data() -> pd.DataFrame:
    transactions = extract_transactions()

    return transactions
