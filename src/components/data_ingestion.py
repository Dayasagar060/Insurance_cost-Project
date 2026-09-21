import os
import pandas as pd

from src.constant import (
    RAW_DATA_PATH,
    INGESTED_TRAIN_PATH,
    ARTIFACTS_DIR
)

from src.logger import logging


class DataIngestion:

    def __init__(self):
        os.makedirs(ARTIFACTS_DIR, exist_ok=True)
        logging.info("Data ingestion directories created.")

    def initiate_data_ingestion(self):

        logging.info("Starting data ingestion process.")

        try:
            df = pd.read_csv(RAW_DATA_PATH)

            logging.info(
                f"Raw data read successfully from {RAW_DATA_PATH}."
            )

            df.to_csv(INGESTED_TRAIN_PATH, index=False)

            logging.info(
                f"Ingested data saved to {INGESTED_TRAIN_PATH}."
            )

            return INGESTED_TRAIN_PATH

        except Exception as e:
            logging.error(f"Error during data ingestion: {e}")
            raise e
