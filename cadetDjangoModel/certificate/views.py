from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.exceptions import PermissionDenied

# from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from .models import Certificate, Requirements, Cadet, CertificadoPDF
from .serializers import CertificateSerializer, RequirementsSerializer
from .permissions import has_permission
from django.template.loader import render_to_string
from weasyprint import HTML


class PermissionBaseAPIView(APIView):
    def check_permissions(self, request):
        user_id = request.headers.get("X-User-ID", 1)
        role_id = request.headers.get("X-Role-ID", 2)

        # Verifique se os parâmetros necessários estão presentes
        if not user_id or not role_id:
            raise PermissionDenied("ID de usuário ou papel não fornecido.")

        # Verifica se o usuário tem permissão para acessar a rota
        has_permission(user_id, role_id, "certificate", request.method)


    def dispatch(self, request, *args, **kwargs):
        # Chama a verificação de permissões antes de processar a requisição
        self.check_permissions(request)
        return super().dispatch(request, *args, **kwargs)






class CertificateListCreateAPIView(PermissionBaseAPIView):
    def get(self, request):
        # Processa a requisição GET após a verificação de permissão
        certificates = Certificate.objects.all()
        serialized = CertificateSerializer(certificates, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Processa a requisição POST após a verificação de permissão
        serialized = CertificateSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serialized.validated_data
        certificate = serialized.create(valid_data)
        return Response(CertificateSerializer(certificate).data, status=status.HTTP_201_CREATED)


class  CertificateRetrieveUpdateDeleteAPIView(APIView):
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

    def delete(self, request, pk):
        try:
            # Buscar o certificado pelo ID
            certificate = Certificate.objects.get(id=pk)
        except Certificate.DoesNotExist:
            return Response({"error": "Certificate not found"}, status=status.HTTP_404_NOT_FOUND)

        # Deletar o certificado
        certificate.delete()
        return Response({"message": "Certificate deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class  RequirementsListCreateAPIView(APIView):
    def get(self, request):
        certificates = Requirements.objects.all()
        serialized = RequirementsSerializer(certificates, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)




class  CertificateListAPIView(APIView):
    def get(self, request):
        certificates = Certificate.objects.all()
        serialized = CertificateSerializer(certificates, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class  CertificatePdfAPIView(APIView):
    def get(self, request, pk):
        certificate = Certificate.objects.get(id=pk)
        serialized = CertificateSerializer(certificate)
        return Response(serialized.data, status=status.HTTP_200_OK)


class CertificateGeneretePdfAPIView(APIView):
    def get(self, request,id_user,pk):
        try:

            # Recupera o certificado
            certificado = Certificate.objects.get(pk=pk)

            #pegar o usuario
            cadet = Cadet.objects.get(intra_id = id_user)

            certificadoPDF = CertificadoPDF.objects.create(cadet=cadet,certificate=certificado)

            # Renderiza o template HTML
            html_string = render_to_string('certificado.html', {'certificado': certificado})

            # Gera o PDF
            pdf = HTML(string=html_string).write_pdf()

            # Retorna o PDF como resposta
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="certificado_{certificado.id}.pdf"'
            return response
        except Certificate.DoesNotExist:
            return Response({'error': 'Certificado não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
