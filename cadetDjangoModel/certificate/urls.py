from django.urls import path

# Class APIView para melhor personalização:
from .views import CertificateListCreateAPIView, SkillListCreateAPIView, CertificateRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('certificate/', CertificateListCreateAPIView.as_view(),name='certificate-list'),
    path('certificate/<pk>/', CertificateRetrieveUpdateDeleteAPIView.as_view(), name='certificate-update'),
    path('skill/', SkillListCreateAPIView.as_view(),name='skill-list'),
]
