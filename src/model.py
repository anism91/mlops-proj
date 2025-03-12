from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Charger un modèle pré-entraîné (ex: bert-base-uncased)
MODEL_NAME = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=3)  # 3 classes de sentiment

# Vérifier si CUDA est disponible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
