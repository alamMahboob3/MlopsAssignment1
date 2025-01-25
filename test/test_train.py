# tests/test_train.py
import os

def test_model_file_exists():
    assert os.path.exists("model.pkl"), "model.pkl does not exist"
    print("model.pkl exists")

test_model_file_exists()