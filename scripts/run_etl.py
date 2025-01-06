import os
from etl.extract.extract import extract_data
from etl.transform.transform import transform_data
from etl.load.load import load_data


def main():

    # Extract data
    data = extract_data()

    # Transform data
    data = transform_data(data)

    # Load data
    load_data(data)

    print(
        f'ETL pipeline run successfully in '
        f'{os.getenv('ENV', 'error')} environment!'
    )


if __name__ == '__main__':
    main()
