import os
from train import train_model

def test_model_training():
    model = train_model()
    assert model is not None
    assert os.path.exists("model.pkl")
