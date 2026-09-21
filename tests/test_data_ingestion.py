import sys
import os
import pandas as pd

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from src.components.data_ingestion import DataIngestion


def test_data_ingestion():

    dst = DataIngestion().initiate_data_ingestion()

    ingested_data = pd.read_csv(dst)

    assert os.path.exists(dst)

    print(
        f"Data ingestion test passed. "
        f"Ingested data saved to {dst}"
    )


if __name__ == "__main__":
    test_data_ingestion()