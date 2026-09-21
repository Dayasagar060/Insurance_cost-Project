import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.components.model_trainer import ModelTrainer

def test_model_trainer():
    model_out = ModelTrainer().train_and_save_model()
    assert os.path.exists(model_out), f"Trained model file not found: {model_out}"
    print(f"Test passed: Model saved at {model_out}")   


if __name__ == "__main__":
    test_model_trainer()