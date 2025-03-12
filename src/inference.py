import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Charger le modèle entraîné
MODEL_NAME = "bert-base-uncased"
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model.eval()  # Mode évaluation

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
    sentiment = torch.argmax(logits).item()
    return ["Négatif", "Neutre", "Positif"][sentiment]

# Exemple d'utilisation
if __name__ == "__main__":
    text = input("Entrez un texte : ")
    print(f"Sentiment prédit : {predict_sentiment(text)}")
