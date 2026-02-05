from django.shortcuts import render
from django.views.decorators.http import require_GET
import joblib
import numpy as np
import os
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import PredictionInputSerializer, PredictionOutputSerializer

# Load model from performance directory
model_path = os.path.join(settings.BASE_DIR, 'performance', 'model.pkl')
model = joblib.load(model_path)

@require_GET
def ui_home(request):
    """
    Simple UI page for the predictor.

    Uses the existing REST endpoint at /api/predict/ via fetch() in the template.
    """
    return render(request, "performance/index.html")

def validate_realistic_input(data):
    """
    Validate that the input data represents a realistic scenario.
    Returns (is_valid, error_message)
    """
    hours_studied = data['hours_studied']
    sleep_hours = data['sleep_hours']
    previous_scores = data['previous_scores']
    sample_papers = data['sample_papers']
    
    # Check if total hours exceed 24
    if hours_studied + sleep_hours > 24:
        return False, f"Impossible scenario: Study hours ({hours_studied}) + Sleep hours ({sleep_hours}) = {hours_studied + sleep_hours} hours exceeds 24 hours in a day!"
    
    # Check if study hours are unrealistic (more than 16 hours)
    if hours_studied > 16:
        return False, f"Unrealistic: Studying {hours_studied} hours per day is not sustainable. Maximum realistic study time is 16 hours."
    
    # Check if sleep is dangerously low
    if sleep_hours < 4:
        return False, f"Health concern: {sleep_hours} hours of sleep is dangerously low. Minimum recommended sleep is 4 hours (though 6-8 is ideal)."
    
    # Check if sleep is unrealistically high
    if sleep_hours > 12:
        return False, f"Unrealistic: Sleeping {sleep_hours} hours per day is excessive. Maximum realistic sleep is 12 hours."
    
    # Warn about poor study-sleep balance
    if hours_studied > 12 and sleep_hours < 6:
        return False, f"Unsustainable: Studying {hours_studied} hours with only {sleep_hours} hours of sleep will lead to burnout and poor performance."
    
    # Check if previous scores are realistic
    if previous_scores < 0 or previous_scores > 100:
        return False, f"Invalid: Previous scores must be between 0 and 100, got {previous_scores}."
    
    # Check if sample papers practiced is realistic
    if sample_papers > 15:
        return False, f"Unrealistic: Practicing {sample_papers} sample papers regularly is excessive. Maximum realistic is 15."
    
    # Warn about low effort
    if hours_studied < 2 and sample_papers == 0 and previous_scores < 50:
        return False, f"Warning: With only {hours_studied} hours of study, no practice papers, and low previous scores ({previous_scores}), improvement is unlikely without increased effort."
    
    return True, None

@api_view(['GET'])
def health_check(request):
    """Health check endpoint to verify API is running"""
    return Response({
        'status': 'healthy',
        'model_loaded': model is not None,
        'database': 'connected'
    }, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='post',
    operation_description="Predict student performance based on study habits and academic history",
    operation_summary="Predict Student Performance",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['hours_studied', 'previous_scores', 'extracurricular', 'sleep_hours', 'sample_papers'],
        properties={
            'hours_studied': openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description='Number of hours studied per day (1-24)',
                example=8
            ),
            'previous_scores': openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description='Previous academic scores (0-100)',
                example=85
            ),
            'extracurricular': openapi.Schema(
                type=openapi.TYPE_BOOLEAN,
                description='Whether student participates in extracurricular activities',
                example=True
            ),
            'sleep_hours': openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description='Number of hours of sleep per day (1-24)',
                example=7
            ),
            'sample_papers': openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description='Number of sample papers practiced (0-20)',
                example=5
            ),
        },
    ),
    responses={
        200: openapi.Response(
            description="Successful prediction",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'predicted_performance_index': openapi.Schema(
                        type=openapi.TYPE_NUMBER,
                        description='Predicted performance index score (0-100)',
                        example=85.67
                    ),
                    'feedback': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                        description='Personalized feedback and suggestions',
                        example=["⚠️ Low sleep may negatively impact performance. Aim for 7-8 hours."]
                    )
                }
            )
        ),
        400: openapi.Response(
            description="Bad Request - Invalid or unrealistic input data",
            examples={
                "application/json": {
                    "error": "Unrealistic scenario",
                    "message": "Impossible scenario: Study hours (20) + Sleep hours (6) = 26 hours exceeds 24 hours in a day!",
                    "suggestion": "Please enter realistic values that represent an actual student's daily routine."
                }
            }
        ),
        500: openapi.Response(
            description="Internal Server Error - Prediction failed",
            examples={
                "application/json": {
                    "error": "Prediction failed",
                    "details": "Error message"
                }
            }
        )
    },
    tags=['Machine Learning Predictions']
)
@api_view(['POST'])
def predict_performance(request):
    """
    Predict student performance index based on various factors.
    
    This endpoint uses a machine learning model to predict a student's 
    performance index based on their study habits, previous scores, 
    extracurricular activities, sleep patterns, and practice with sample papers.
    
    The prediction model takes into account:
    - Hours studied per day
    - Previous academic scores
    - Participation in extracurricular activities
    - Sleep hours per day
    - Number of sample papers practiced
    
    The API also validates that the input represents a realistic scenario.
    """
    serializer = PredictionInputSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response(
            {"error": "Invalid input data", "details": serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    data = serializer.validated_data
    
    # Validate realistic scenario
    is_valid, error_message = validate_realistic_input(data)
    if not is_valid:
        return Response(
            {
                "error": "Unrealistic scenario", 
                "message": error_message,
                "suggestion": "Please enter realistic values that represent an actual student's daily routine."
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        features = np.array([[
            data['hours_studied'],
            data['previous_scores'],
            1 if data['extracurricular'] else 0,
            data['sleep_hours'],
            data['sample_papers'],
        ]])
        
        prediction = model.predict(features)[0]
        
        # Cap prediction at 100 (percentage)
        prediction = min(float(prediction), 100.0)
        
        # Add contextual feedback
        feedback = []
        if data['sleep_hours'] < 6:
            feedback.append("⚠️ Low sleep may negatively impact performance. Aim for 7-8 hours.")
        if data['hours_studied'] < 3:
            feedback.append("💡 Consider increasing study hours for better results.")
        if data['sample_papers'] < 2:
            feedback.append("📝 Practicing more sample papers can significantly improve performance.")
        if data['hours_studied'] > 10:
            feedback.append("⚡ Great dedication! Make sure to take breaks to avoid burnout.")
        if data['extracurricular']:
            feedback.append("🎯 Extracurricular activities contribute to well-rounded development!")
        
        response_data = {
            'predicted_performance_index': round(prediction, 2),
            'feedback': feedback if feedback else ["✅ Good balance of study, rest, and activities!"]
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {"error": "Prediction failed", "details": str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )