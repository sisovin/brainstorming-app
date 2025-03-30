import os
import requests
from dotenv import load_dotenv

load_dotenv()

INFRANODUS_API_KEY = os.getenv('INFRANODUS_API_KEY')
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')

def call_infranodus_api(text):
    url = "https://api.infranodus.com/analyze"
    headers = {
        "Authorization": f"Bearer {INFRANODUS_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def fetch_news_articles():
    url = "https://newsapi.org/v2/top-headlines"
    headers = {
        "X-Api-Key": RAPIDAPI_KEY
    }
    params = {
        "country": "us",
        "category": "technology"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json().get('articles', [])

def generate_research_questions(content_gaps):
    questions = []
    for gap in content_gaps:
        question = f"What are the implications of {gap.gap_description}?"
        questions.append(question)
    return questions
