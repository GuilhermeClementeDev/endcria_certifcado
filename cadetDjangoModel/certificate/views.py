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

    def put(self, request, pk=None):
        try:
        # Buscar o certificado pelo ID
            certificate = Certificate.objects.get(pk=pk)
        except Certificate.DoesNotExist:
            return Response({"error": "Certificate not found"},status=status.HTTP_404_NOT_FOUND)
    # Serializar os dados com a instância existente
        serialized = CertificateSerializer(certificate, data=request.data, partial=False)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    # Atualizar os dados do certificado
        certificate = serialized.save()  # Salva as alterações
        return Response(CertificateSerializer(certificate).data, status=status.HTTP_200_OK)



#class  SkillListCreateAPIView(APIView):
