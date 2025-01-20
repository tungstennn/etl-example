import pandas as pd
from utils.file_utils import save_dataframe_to_csv


def clean_customers(customers: pd.DataFrame) -> pd.DataFrame:
    # Remove rows with missing values
    # Standardise country string to uppercase
    # Standardise the is_active column
    # Remove duplicates
    customers = customers.dropna(subset=['country', 'is_active'])
    customers.loc[:, 'country'] = customers['country'].str.upper()
    customers.loc[:, 'is_active'] = customers['is_active'].apply(
        standardise_is_active
    )
    customers = customers.drop_duplicates()
    # Set the is_active column to boolean
    customers['is_active'] = customers['is_active'].astype(bool)

    # Save the dataframe as a CSV for logging purposes
    output_dir = 'etl/data/processed'
    file_name = 'cleaned_customers.csv'
    save_dataframe_to_csv(customers, output_dir, file_name)

    return customers


def standardise_is_active(value: str) -> bool:
    if pd.isna(value):
        return False
    if isinstance(value, bool):
        return value
    if value.lower() in ['active', '1', 'true']:
        return True
    return False  # Default to False for any other cases


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