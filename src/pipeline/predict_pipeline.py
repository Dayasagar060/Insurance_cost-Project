import pandas as pd
import joblib 
from src.constant import BEST_MODEL_PATH, ARTIFACTS_DIR
import os


class PredictPipeline:

    def __init__(self):
        self.model_path = BEST_MODEL_PATH
        self.preprocessor_path = os.path.join(ARTIFACTS_DIR, "preprocessor.pkl")
        self.model = joblib.load(self.model_path)
        self.preprocessor = joblib.load(self.preprocessor_path)

    def predict(self, input_df):
        input_df['age_bmi_interaction'] = input_df['age'] * input_df['bmi']

        X_processed = self.preprocessor.transform(input_df)
        predictions = self.model.predict(X_processed)
        return predictions