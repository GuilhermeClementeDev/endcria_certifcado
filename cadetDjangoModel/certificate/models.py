from django.db import models
from cadet.models import Roles
from cadet.models import Cadet

class Requirements(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="teste")
    requirements_required = models.ManyToManyField(Requirements)
    issued_at = models.DateTimeField(auto_now_add=True)



class Route(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class Permission(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    can_view = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)


class UserRequirements(models.Model):
    user = models.ForeignKey(
        Cadet,
        on_delete=models.CASCADE,
        related_name="user_skills"
    )
    requirements = models.ForeignKey(
        Requirements,
        on_delete=models.CASCADE,
        related_name="user_skills"
    )
