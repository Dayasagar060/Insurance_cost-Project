import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging
from src.exceptions import CustomException


class TrainingPipeline:

    def run_pipeline(self):
        try:
            logging.info("Training pipeline started")
            print("Starting data ingestion...")
            DataIngestion().initiate_data_ingestion()
            print("Starting data transformation...")
            DataTransformation().initiate_data_transformation()
            print("Starting model training...")
            ModelTrainer().train_and_save_model()
            print("Training pipeline completed successfully.")
            logging.info("Training pipeline completed successfully")
        except Exception as e:
            logging.exception("Pipeline failed")
            raise CustomException(e, sys)