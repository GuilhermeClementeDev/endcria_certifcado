from django.db import models
from cadet.models import Cadet

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="teste")
    student = models.ForeignKey(Cadet, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)

