from rest_framework import serializers
from .models import ContentAnalysisResult, ContentGap, ResearchQuestion

class ContentAnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentAnalysisResult
        fields = '__all__'

class ContentGapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentGap
        fields = '__all__'

class ResearchQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchQuestion
        fields = '__all__'
