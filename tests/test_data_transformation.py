import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.components.data_transformation import DataTransformation


def test_data_transformation():
    processed_out, preprocessor_out = DataTransformation().initiate_data_transformation()
    assert os.path.exists(processed_out), f"Processed data file not found: {processed_out}"
    assert os.path.exists(preprocessor_out), f"Preprocessor file not found: {preprocessor_out}"
    print(f"Test passed: Outputs exist at {processed_out}, {preprocessor_out}")

if __name__ == "__main__":
    test_data_transformation()