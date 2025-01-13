import pandas as pd


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
    return customers


def standardise_is_active(is_active_value: str) -> bool:
    if str(is_active_value).lower() == 'active' or str(is_active_value) == '1':
        return True
    else:
        return False
