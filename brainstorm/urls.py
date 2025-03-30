from django.urls import path
from . import views

urlpatterns = [
    path('fetch-news/', views.fetch_news, name='fetch_news'),
    path('analyze-text/', views.analyze_text, name='analyze_text'),
    path('generate-questions/', views.generate_questions, name='generate_questions'),
]
