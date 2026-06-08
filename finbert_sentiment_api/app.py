from fastapi import FastAPI
from pydantic import BaseModel

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

import torch
import torch.nn.functional as F

app = FastAPI(
    title = "Finbert Sentiment API"
)

MODEL_NAME = "ProsusAI/finbert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

class TextRequest(BaseModel):
    request: str

    @app.get("/")
    def health_check():
        return {
            "status": "running"
        }
    
    @app.post("/analyze")
    def analyze_sentiment(request: TextRequest):
        inputs = tokenizer(
            request.request,
            return_tensors = "pt",
            truncation = True,
            padding = True
        )

        with torch.no_grad():
            outputs = model(**inputs)

        probs = F.softmax(
            outputs.logits,
            dim = -1
        )

        predicted_class = torch.argmax(
            probs,
            dim = 1
        ).item()

        sentiment = model.config.id2labels[predicted_class]

        confidence = probs[0, predicted_class].item()

        return {
            "text": request.request,
            "sentiment": sentiment,
            "confidence": round(confidence,4)
        }
    