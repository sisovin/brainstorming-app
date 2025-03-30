import os
import requests
from dotenv import load_dotenv

load_dotenv()

INFRANODUS_API_KEY = os.getenv('INFRANODUS_API_KEY')

def analyze_text(text):
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

if __name__ == "__main__":
    sample_text = "Your sample text here."
    analysis_result = analyze_text(sample_text)
    print(analysis_result)
