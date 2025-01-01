from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from transformers import pipeline

app = FastAPI()

model = pipeline('sentiment-analysis')

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to SentiSense API"}

@app.post("/analyze/")
def analyze_sentiment(input: TextInput):
    try:
        # Preprocess the input text to handle unescaped characters
        processed_text = preprocess_text(input.text)
        # Perform sentiment analysis
        result = model(processed_text)
        return {"label": result[0]["label"], "score": result[0]["score"]}
    except ValidationError as ve:
        raise HTTPException(status_code=422, detail="Invalid input format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def preprocess_text(text: str) -> str:
    """
    Preprocess the input text to handle unescaped characters or invalid strings.
    """
    try:
        # Attempt to escape unescaped quotes or handle JSON-like strings
        if isinstance(text, str):
            return text.encode("utf-8").decode("unicode_escape")
        return text
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing text: {str(e)}")