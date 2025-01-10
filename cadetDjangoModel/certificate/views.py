from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse

from rest_framework import status

from .models import Certificate, Skill
from .serializers import CertificateSerializer, SkillSerializer

class  CertificateListCreateAPIView(APIView):
    def get(self, request):
        certificates = Certificate.objects.all()
        serialized = CertificateSerializer(certificates, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized = CertificateSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serialized.validated_data
        certificate = serialized.create(valid_data)
        return Response(CertificateSerializer(certificate).data, status=status.HTTP_201_CREATED)

class   CertificateRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        certificate = Certificate.objects.get(id=pk)
        serialized = CertificateSerializer(certificate)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            # Buscar o certificado pelo ID
            certificate = Certificate.objects.get(id=pk)
        except Certificate.DoesNotExist:
            return Response({"error": "Certificate not found"},status=status.HTTP_404_NOT_FOUND)
    # Serializar os dados com a instância existente
        serialized = CertificateSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

        valid_data = serialized._validated_data
        serialized.update(certificate, valid_data)
        return Response(serialized.data, status=status.HTTP_200_OK)



class  SkillListCreateAPIView(APIView):
    def get(self, request):
        certificates = Skill.objects.all()
        serialized = SkillSerializer(certificates, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
