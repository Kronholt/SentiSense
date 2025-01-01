from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to SentiSense API"}

def test_analyze_sentiment_valid():
    # Valid input with properly escaped quotes
    response = client.post("/analyze/", json={"text": "\"I love this product!\""})
    assert response.status_code == 200
    assert response.json()["label"] in ["POSITIVE", "NEGATIVE"]
    assert response.json()["score"] > 0

def test_analyze_sentiment_unescaped_quotes():
    # Input with unescaped quotes (backend should handle this gracefully)
    response = client.post("/analyze/", json={"text": '"I hate this product," he said.'})
    assert response.status_code == 200
    assert response.json()["label"] in ["POSITIVE", "NEGATIVE"]
    assert response.json()["score"] > 0

def test_analyze_sentiment_empty_text():
    # Empty text input
    response = client.post("/analyze/", json={"text": ""})
    assert response.status_code == 200
    assert response.json()["label"] in ["POSITIVE", "NEGATIVE"]
    assert response.json()["score"] > 0  # Even empty strings might return a valid score

def test_analyze_sentiment_numeric_input():
    # Numeric input (not valid for sentiment analysis)
    response = client.post("/analyze/", json={"text": "12345"})
    assert response.status_code == 200
    assert response.json()["label"] in ["POSITIVE", "NEGATIVE"]
    assert response.json()["score"] > 0

def test_analyze_sentiment_special_characters():
    # Input with special characters
    response = client.post("/analyze/", json={"text": "!!!"})
    assert response.status_code == 200
    assert response.json()["label"] in ["POSITIVE", "NEGATIVE"]
    assert response.json()["score"] > 0
