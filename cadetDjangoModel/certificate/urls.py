from django.urls import path

# Class APIView para melhor personalização:
from .views import CertificateListCreateAPIView

urlpatterns = [
    path('certificate/', CertificateListCreateAPIView.as_view()),
]
