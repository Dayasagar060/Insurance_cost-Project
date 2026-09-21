import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.pipeline.train_pipeline import TrainingPipeline

def test_train_pipeline():
    try:
        TrainingPipeline().run_pipeline()
        print("Test passed: Training pipeline ran successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
        raise

if __name__ == "__main__":
    test_train_pipeline()