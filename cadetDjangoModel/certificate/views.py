from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse

from rest_framework import status

from .models import Certificate
from .serializers import CertificateSerializer

class  CertificateListCreateAPIView(APIView):
    def put(self, request):
        serialized = CertificateSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serialized.validated_data
        serialized.create(valid_data)
        return Response(serialized.data, status=status.HTTP_201_CREATED)


