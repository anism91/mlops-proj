import torch
from src.model import model, tokenizer


def test_model_output_shape():
    test_text = "Ce film était nulle"
    inputs = tokenizer(test_text, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
    assert logits.shape == (1, 3), f"Expected output shape (1, 3), got {logits.shape}"
