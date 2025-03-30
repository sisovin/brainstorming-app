from django.db import models

class ContentAnalysisResult(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    analysis_date = models.DateTimeField(auto_now_add=True)
    infranodus_response = models.JSONField()

    def __str__(self):
        return self.title

class ContentGap(models.Model):
    analysis_result = models.ForeignKey(ContentAnalysisResult, on_delete=models.CASCADE)
    gap_description = models.TextField()
    detected_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gap in {self.analysis_result.title}"

class ResearchQuestion(models.Model):
    content_gap = models.ForeignKey(ContentGap, on_delete=models.CASCADE)
    question_text = models.TextField()
    generated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
