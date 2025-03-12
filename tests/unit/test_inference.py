from src.inference import predict_sentiment
import sys
import os
sys.path.append(os.path.abspath("src"))


def test_inference():
    sentiment = predict_sentiment("This movie is amazing!")
    assert sentiment in ["Négatif", "Neutre", "Positif"], f"Unexpected sentiment: {sentiment}"

