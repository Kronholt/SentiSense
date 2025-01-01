#SentiSense API
SentiSense API is a lightweight and fast web application built with FastAPI that provides sentiment analysis capabilities using a pre-trained AI model. It analyzes text input to determine whether the sentiment is positive or negative, along with a confidence score.

##Features
Sentiment Analysis: Classifies input text as POSITIVE or NEGATIVE and provides a confidence score.
FastAPI Framework: Built with FastAPI for performance and ease of use.
Pre-trained Model: Uses Hugging Face's distilbert-base-uncased-finetuned-sst-2-english for accurate and efficient sentiment analysis.
##Endpoints
Root Endpoint
URL: /
Method: GET
Description: Returns a welcome message.
Response:
json
Copy code
{
  "message": "Welcome to SentiSense API"
}
Sentiment Analysis Endpoint
URL: /analyze/
Method: POST
Description: Accepts a string of text and returns its sentiment.
Request Body:
json
Copy code
{
  "text": "Your input text here"
}
Response:
json
Copy code
{
  "label": "POSITIVE",
  "score": 0.987654
}
Installation and Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo/sentisense-api.git
cd sentisense-api
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
uvicorn main:app --reload
Open your browser and navigate to:

API Documentation: http://127.0.0.1:8000/docs
API Root: http://127.0.0.1:8000/
Running Tests
Install pytest if not already installed:

bash
Copy code
pip install pytest
Run the tests:

bash
Copy code
pytest
Technologies Used
FastAPI: Web framework for building APIs.
Transformers: Hugging Face library for AI models.
Uvicorn: ASGI server for running the FastAPI app.
Python: Core programming language.
Future Enhancements
Add support for additional languages and models.
Include batch processing for analyzing multiple inputs at once.
Build a frontend interface for easier interaction with the API.