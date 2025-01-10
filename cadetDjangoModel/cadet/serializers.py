from rest_framework import serializers
from .models import Cadet, Roles

class   CadetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadet
        fields = '__all__'

class   RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'