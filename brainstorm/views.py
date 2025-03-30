from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ContentAnalysisResult, ContentGap, ResearchQuestion
from .serializers import ContentAnalysisResultSerializer, ContentGapSerializer, ResearchQuestionSerializer
from .utils import fetch_news_articles, analyze_text_with_infranodus, generate_research_questions

@api_view(['GET'])
def fetch_news(request):
    try:
        news_data = fetch_news_articles()
        return Response(news_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def analyze_text(request):
    try:
        text = request.data.get('text')
        if not text:
            return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        analysis_result = analyze_text_with_infranodus(text)
        serializer = ContentAnalysisResultSerializer(data=analysis_result)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def generate_questions(request):
    try:
        analysis_result_id = request.data.get('analysis_result_id')
        if not analysis_result_id:
            return Response({'error': 'Analysis result ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        analysis_result = ContentAnalysisResult.objects.get(id=analysis_result_id)
        content_gaps = ContentGap.objects.filter(analysis_result=analysis_result)
        research_questions = generate_research_questions(content_gaps)
        
        serializer = ResearchQuestionSerializer(data=research_questions, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ContentAnalysisResult.DoesNotExist:
        return Response({'error': 'Analysis result not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
