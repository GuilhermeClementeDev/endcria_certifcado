from django.urls import path

# Class APIView para melhor personalização:
from .views import CertificateListCreateAPIView, RequirementsListCreateAPIView, CertificateRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('staff/certificate/', CertificateListCreateAPIView.as_view(),name='certificate-list'),
    path('staff/certificate/<pk>/', CertificateRetrieveUpdateDeleteAPIView.as_view(), name='certificate-update'),
    path('requirements/', RequirementsListCreateAPIView.as_view(),name='Requirements-list'),
]
