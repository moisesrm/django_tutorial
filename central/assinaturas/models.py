from django.db import models

# Create your models here.
class Assinatura(models.Model):
    nome = models.CharField(max_length=200)
    