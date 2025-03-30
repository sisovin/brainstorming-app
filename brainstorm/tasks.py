from celery import shared_task
from .utils import fetch_news_articles, analyze_text_with_infranodus, generate_research_questions
from .models import ContentAnalysisResult, ContentGap, ResearchQuestion

@shared_task
def fetch_and_analyze_news():
    try:
        news_data = fetch_news_articles()
        for article in news_data:
            analysis_result = analyze_text_with_infranodus(article['content'])
            content_analysis_result = ContentAnalysisResult.objects.create(
                title=article['title'],
                content=article['content'],
                infranodus_response=analysis_result
            )
            content_gaps = analysis_result.get('gaps', [])
            for gap in content_gaps:
                content_gap = ContentGap.objects.create(
                    analysis_result=content_analysis_result,
                    gap_description=gap
                )
                research_questions = generate_research_questions([content_gap])
                for question in research_questions:
                    ResearchQuestion.objects.create(
                        content_gap=content_gap,
                        question_text=question
                    )
    except Exception as e:
        # Log the error or handle it as needed
        print(f"Error in fetch_and_analyze_news task: {e}")

@shared_task
def analyze_text_and_generate_questions(text):
    try:
        analysis_result = analyze_text_with_infranodus(text)
        content_analysis_result = ContentAnalysisResult.objects.create(
            title="Custom Text Analysis",
            content=text,
            infranodus_response=analysis_result
        )
        content_gaps = analysis_result.get('gaps', [])
        for gap in content_gaps:
            content_gap = ContentGap.objects.create(
                analysis_result=content_analysis_result,
                gap_description=gap
            )
            research_questions = generate_research_questions([content_gap])
            for question in research_questions:
                ResearchQuestion.objects.create(
                    content_gap=content_gap,
                    question_text=question
                )
    except Exception as e:
        # Log the error or handle it as needed
        print(f"Error in analyze_text_and_generate_questions task: {e}")
