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

    # Save the dataframe as a CSV for logging purposes
    transactions.to_csv(
        '../../data/processed/cleaned_transactions.csv',
        index=False
    )

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

"""
ADDITIONAL TESTS NEEDED TO BE DONE:

CLEANING:

Given the extracted data, when duplicates are removed, then 100% of duplicates should be removed.
Given the extracted data, when missing, then 100% of missing should be resolved.
Given the extracted data, when invalid values are handled, then 100% of invalid fields should be resolved.
Given the extracted data, when data cleaning is performed, then it should complete in less than 1 second per 1,000 rows.

DOCUMENTATION

"""  # noqa