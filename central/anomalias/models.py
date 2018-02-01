from django.db import models

# Create your models here.
class Anomalia(models.Model):
    login_required = True
    descricao = models.TextField("Descrição",max_length=200)
    identificador = models.TextField("Identificador",max_length=200)
    ativo = models.IntegerField('Ativo',default=1)
    prioridade = models.IntegerField('Prioridade',default=1)