import os
import requests
from dotenv import load_dotenv
from brainstorm.utils import call_infranodus_api, generate_research_questions

load_dotenv()

INFRANODUS_API_KEY = os.getenv('INFRANODUS_API_KEY')

def extract_content_gaps(text):
    analysis_result = call_infranodus_api(text)
    content_gaps = analysis_result.get('gaps', [])
    return content_gaps

def create_research_questions(text):
    content_gaps = extract_content_gaps(text)
    research_questions = generate_research_questions(content_gaps)
    return research_questions

if __name__ == "__main__":
    sample_text = "Your sample text here."
    questions = create_research_questions(sample_text)
    for question in questions:
        print(question)
