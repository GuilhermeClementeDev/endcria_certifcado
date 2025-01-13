from rest_framework import serializers
from .models import Certificate, Requirements

class CertificateSerializer(serializers.ModelSerializer):
    requirements_required = serializers.PrimaryKeyRelatedField(
        queryset=Requirements.objects.all(), many=True
    )

    class Meta:
        model = Certificate
        fields = ['id', 'name', 'description', 'requirements_required', 'issued_at']

    def create(self, validated_data):
        # Extraindo as habilidades
        #isso é para não dar erro!!!!!
        #literalmente ta refazendo por conta do manytomany
        skills = validated_data.pop('requirements_required', [])
        # Criando o certificado
        certificate = Certificate.objects.create(**validated_data)
        # Associando as habilidades
        certificate.requirements_required.set(skills)
        return certificate

class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'
