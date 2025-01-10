from django.urls import path

# Class APIView para melhor personalização:
from .views import

urlpatterns = [
    path('cadets/', .as_view(), name='cadet-list'),
	path('staff/', .as_view(), name='cadet-list')
]
