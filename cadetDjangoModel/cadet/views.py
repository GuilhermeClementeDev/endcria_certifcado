from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse

from rest_framework import status

from .models import Cadet, Roles
from .serializers import CadetSerializer, RolesSerializer


class   CadetListCreateAPIView(APIView):
    def get(self, request):
        cadets = Cadet.objects.all()
        serialized = CadetSerializer(cadets, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized = CadetSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serialized.validated_data
        serialized.create(valid_data)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

class   CadetRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        cadet = Cadet.objects.get(id=pk)
        serialized = CadetSerializer(cadet)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        cadet = Cadet.objects.get(id=pk)
        serialized = CadetSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serialized.validated_data
        serialized.update(cadet, valid_data)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

class   RolesListCreateAPIView(APIView):
    def get(self, request):
        roles = Roles.objects.all()
        serialized = RolesSerializer(roles, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized = RolesSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serialized.validated_data
        serialized.create(valid_data)
        return Response(serialized.data, status=status.HTTP_200_OK)

class   RolesRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        role = Roles.objects.get(id=pk)
        serialized = RolesSerializer(role)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serialized = RolesSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        role = Roles.objects.get(id=pk)
        valid_data = serialized.validated_data
        serialized.update(role, valid_data)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        pass

    def delete(self, request, pk):
        pass



# @api_view(['GET', 'POST'])
# def cadetView(request):
#     if request.method == 'GET':
#         cadet = Cadet.objects.all()
#         serializer = CadetSerializer(cadet, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)
#         #return HttpResponse(serializer.data)
#     elif request.method == 'POST':
#         serializer = CadetSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         validated_data = serializer.validated_data
#         serializer.create(validated_data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def RolesView(request):
#     if request.method == 'GET':
#         roles = Roles.objects.all()
#         serializer = RolesSerializer(roles, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = RolesSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         validated_data = serializer.validated_data
#         serializer.create(validated_data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)