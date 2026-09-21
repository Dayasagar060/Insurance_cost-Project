import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib

from src.constant import INGESTED_TRAIN_PATH, ARTIFACTS_DIR
from src.logger import logging



class DataTransformation:

    def __init__(self):
        os.makedirs(ARTIFACTS_DIR, exist_ok=True)
        logging.info("Data transformation directories created.")
        self.input_path = INGESTED_TRAIN_PATH
        self.processed_out = os.path.join(ARTIFACTS_DIR, 'all_processed.csv')
        self.preprocessor_out = os.path.join(ARTIFACTS_DIR, 'preprocessor.pkl')


    def initiate_data_transformation(self):
        logging.info("Initiating data transformation...")
        df = pd.read_csv(self.input_path)
        logging.info("Data loaded successfully.")

        df['age_bmi_interaction'] = df['age'] * df['bmi']
        logging.info("Feature engineering completed.")

        X = df.drop(columns=['charges'])
        y = df['charges']

        numeric_cols = ['age', 'bmi', 'children', 'age_bmi_interaction']
        categorical_cols = ['sex', 'smoker', 'region']

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numeric_cols),
                ('cat', OneHotEncoder(drop='first' ), categorical_cols)
            ],
            remainder='drop'
        )
        X_processed = preprocessor.fit_transform(X)
        cat_features = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_cols)
        #we want the names of preocessed catgorical features because the features name would be chanhged due to one hot encoding
        all_features = numeric_cols + list(cat_features)

        processed_df = pd.DataFrame(X_processed, columns=all_features)
        processed_df['charges'] = y.values
        processed_df.to_csv(self.processed_out, index=False)
        logging.info(f"Transformed data saved to {self.processed_out}.")

        joblib.dump(preprocessor, self.preprocessor_out)
        logging.info(f"Preprocessor object saved to {self.preprocessor_out}.")

        return self.processed_out, self.preprocessor_out