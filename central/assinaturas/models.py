from django.db import models

# Create your models here.
class Assinatura(models.Model):
    login_required = True
    nome = models.CharField(max_length=200)
    