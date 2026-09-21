import os
import pandas as pd
import joblib

from sklearn.linear_model import Lasso

from src.constant import ARTIFACTS_DIR, BEST_MODEL_PATH, MODELS_DIR
from src.logger import logging


class ModelTrainer:

    def __init__(self):

        # Input: processed data
        self.data_path = os.path.join(
            ARTIFACTS_DIR,
            'all_processed.csv'
        )

        # Output: trained model
        self.model_out = BEST_MODEL_PATH

        # Saved preprocessor
        self.preprocessor_path = os.path.join(
            ARTIFACTS_DIR,
            'preprocessor.pkl'
        )

    def train_and_save_model(self):

        logging.info("Starting model training...")

        # 1. Load processed data
        df = pd.read_csv(self.data_path)
        logging.info("Processed data loaded successfully.")

        # 2. Separate features and target
        X = df.drop(columns=['charges'])
        y = df['charges']

        # 3. Create Lasso model
        model = Lasso(
            alpha=0.01,
            max_iter=2000,
            random_state=1
        )

        # 4. Train model
        model.fit(X, y)
        logging.info("Model training completed.")

        # 5. Create models folder if it doesn't exist
        os.makedirs(MODELS_DIR, exist_ok=True)

        # 6. Save trained model
        joblib.dump(model, self.model_out)
        logging.info(
            f"Trained model saved to {self.model_out}."
        )

        # 7. Return trained model
        return self.model_out