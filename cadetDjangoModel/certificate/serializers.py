from rest_framework import serializers
from .models import Certificate, Skill

class CertificateSerializer(serializers.ModelSerializer):
    skills_required = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), many=True
    )

    class Meta:
        model = Certificate
        fields = ['id', 'name', 'description', 'skills_required', 'issued_at']

    def create(self, validated_data):
        # Extraindo as habilidades
        #isso é para não dar erro!!!!!
        #literalmente ta refazendo por conta do manytomany
        skills = validated_data.pop('skills_required', [])
        # Criando o certificado
        certificate = Certificate.objects.create(**validated_data)
        # Associando as habilidades
        certificate.skills_required.set(skills)
        return certificate

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
