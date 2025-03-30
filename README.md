# Brainstorming App

## Project Structure

```
brainstorm_app/
│── brainstorm_app/            # Main project folder
│   │── __init__.py
│   │── settings.py            # Django settings (Add installed apps & API keys here)
│   │── urls.py                # Main URL configuration
│   │── wsgi.py
│   │── asgi.py
│   └── celery.py              # Celery configuration (for task scheduling)
│
│── brainstorm/                # Brainstorming API app
│   │── migrations/            # Database migrations
│   │── __init__.py
│   │── models.py              # Database models for content analysis
│   │── serializers.py         # Serializers to convert models into JSON
│   │── views.py               # API views for processing data
│   │── urls.py                # App-specific API endpoints
│   │── tasks.py               # Background tasks (e.g., scheduled news analysis)
│   └── utils.py               # Helper functions (InfraNodus API calls)
│
│── templates/                 # Django HTML templates (if needed)
│   └── index.html             # Optional frontend
│
│── static/                    # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
│── scripts/                   # External scripts (for API automation)
│   ├── fetch_news.py          # Script to fetch daily news via RapidAPI
│   ├── analyze_text.py        # Script to send data to InfraNodus
│   └── generate_questions.py  # Script to process content gaps
│
│── requirements.txt           # Required Python packages
│── manage.py                  # Django’s command-line utility
│── db.sqlite3                 # SQLite database (or configure PostgreSQL/MySQL)
│── .env                       # Environment variables (API keys, secret keys)
│── Dockerfile                 # Docker configuration (if needed)
│── README.md                  # Project documentation
```

## Project Breakdown

1. `brainstorm/models.py`
   - Stores content analysis results, gaps, and research questions.
2. `brainstorm/serializers.py`
   - Converts model data into JSON format for API responses.
3. `brainstorm/views.py`
   - API endpoints to:
     - Fetch news data (via RapidAPI)
     - Send text to InfraNodus API
     - Process responses and generate research questions
4. `brainstorm/tasks.py`
   - Celery background tasks to:
     - Automatically fetch news daily and analyze content gaps.
     - Schedule InfraNodus API calls.
5. `brainstorm/utils.py`
   - Helper functions to:
     - Call InfraNodus API for content analysis.
     - Fetch news articles from RapidAPI.
     - Format and generate research questions.
6. `scripts/` Folder
   - `fetch_news.py`: Fetches latest news from RapidAPI.
   - `analyze_text.py`: Sends text data to InfraNodus for analysis.
   - `generate_questions.py`: Extracts content gaps and creates research questions.

## How the Automation Works

### Workflow #1: News Analysis & Content Gap Detection

1. Fetch trending news from RapidAPI.
2. Send news content to InfraNodus for analysis.
3. Detect missing connections (content gaps).
4. Generate a research question that fills the gap.

### Workflow #2: Research Question Generation for Any Content

1. Input any article, paper, or blog post.
2. Analyze key topics using InfraNodus API.
3. Identify content gaps.
4. Generate research questions for further exploration.

## How to Set Up the Project

1. **Install Dependencies**
   ```sh
   pip install django djangorestframework requests celery redis python-dotenv
   ```

2. **Set Up Environment Variables (.env)**
   ```sh
   INFRANODUS_API_KEY=your_infranodus_api_key
   RAPIDAPI_KEY=your_rapidapi_key
   ```

3. **Run Migrations**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start Development Server**
   ```sh
   python manage.py runserver
   ```

5. **Start Celery for Background Tasks**
   ```sh
   celery -A brainstorm_app worker --loglevel=info
   ```

6. **Generate example views.py and tasks.py files?**
