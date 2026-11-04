import torch
from transformers import AutoModelForSequenceClassification

# 少パラメータモデルのロード
model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased')