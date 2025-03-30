import os
import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')

def fetch_latest_news():
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

if __name__ == "__main__":
    news_articles = fetch_latest_news()
    for article in news_articles:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("\n")
