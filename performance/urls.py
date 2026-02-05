from django.urls import path
from .views import predict_performance, health_check

urlpatterns = [
    path('predict/', predict_performance),
    path('health/', health_check),
]
