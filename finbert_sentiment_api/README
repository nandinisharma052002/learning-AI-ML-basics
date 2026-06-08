# FinBERT Sentiment API

A simple FastAPI application that performs financial sentiment analysis using FinBERT, a BERT model fine-tuned on financial text.

## Features

* Accepts financial text through a REST API
* Uses Hugging Face's ProsusAI/finbert model
* Returns sentiment classification:

  * Positive
  * Negative
  * Neutral
* Returns confidence score
* Dockerized for easy deployment

## API Endpoint

### POST /analyze

Request:

```json
{
  "text": "The company reported strong quarterly profits."
}
```

Response:

```json
{
  "text": "The company reported strong quarterly profits.",
  "sentiment": "positive",
  "confidence": 0.9876
}
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Run with Docker

```bash
docker build -t finbert-api .
docker run -p 8000:8000 finbert-api
```

## Learning Objectives

This project was created to practice:

* FastAPI
* Hugging Face Transformers
* FinBERT
* REST API development
* Docker containerization
