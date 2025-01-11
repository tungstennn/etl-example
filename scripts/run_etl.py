import os
import sys
from config.env_config import setup_env
from etl.extract.extract import extract_data
from etl.transform.transform import transform_data
from etl.load.load import load_data


def main():
    print("Setting up environment...")
    setup_env(sys.argv)
    print("Environment setup complete.")

    print("Extracting data...")
    data = extract_data()
    print("Data extraction complete.")

    print("Transforming data...")
    data = transform_data(data)
    print("Data transformation complete.")

    print("Loading data...")
    load_data(data)
    print("Data loading complete.")

    print(
        f'ETL pipeline run successfully in '
        f'{os.getenv("ENV", "error")} environment!'
    )


if __name__ == '__main__':
    main()
