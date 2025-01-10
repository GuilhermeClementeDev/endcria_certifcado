from django.db import models
from cadet.models import Cadet

class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="teste")
    skills_required = models.ManyToManyField(Skill, related_name="certificates")
    issued_at = models.DateTimeField(auto_now_add=True)

class UserSkill(models.Model):
    user = models.ForeignKey(
        Cadet,
        on_delete=models.CASCADE,
        related_name="user_skills"
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="user_skills"
    )
