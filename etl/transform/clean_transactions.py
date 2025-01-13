import pandas as pd
from utils.date_utils import standardise_date


def clean_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    # Remove rows with missing values
    # Standardise date format
    # Remove duplicates
    transactions = remove_missing_values(transactions)
    transactions = standardise_date_format(transactions)
    transactions = transactions.drop_duplicates()
    transactions['amount'] = transactions['amount'].astype('float64')
    return transactions


def remove_missing_values(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions = transactions.dropna(subset='transaction_date')
    transactions = transactions.dropna(subset=['amount'])
    transactions = transactions[transactions['amount'] != 'INVALID']
    return transactions


def standardise_date_format(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['transaction_date'] = (
        transactions['transaction_date'].apply(standardise_date)
    )
    transactions['transaction_date'] = (
        transactions['transaction_date'].dt.strftime('%d/%m/%Y')
    )
    transactions = transactions.dropna(subset=['transaction_date'])
    return transactions
