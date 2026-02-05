from rest_framework import serializers
from .models import StudentPerformance

class StudentPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPerformance
        fields = '__all__'

class PredictionInputSerializer(serializers.Serializer):
    hours_studied = serializers.IntegerField(
        min_value=1, max_value=24,
        help_text="Number of hours studied per day"
    )
    previous_scores = serializers.IntegerField(
        min_value=0, max_value=100,
        help_text="Previous academic scores (0-100)"
    )
    extracurricular = serializers.BooleanField(
        help_text="Whether student participates in extracurricular activities"
    )
    sleep_hours = serializers.IntegerField(
        min_value=1, max_value=24,
        help_text="Number of hours of sleep per day"
    )
    sample_papers = serializers.IntegerField(
        min_value=0, max_value=20,
        help_text="Number of sample papers practiced"
    )

class PredictionOutputSerializer(serializers.Serializer):
    predicted_performance_index = serializers.FloatField(
        help_text="Predicted performance index score"
    )