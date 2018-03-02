from django.db import models

# Create your models here.
class Aparelho(models.Model):
    login_required = True
    descricao = models.TextField("Descrição",max_length=200)
    bssid = models.TextField("BSSID",max_length=200)
    mac = models.TextField("Mac",max_length=200)
    num_conectados = models.IntegerField('Num_Conectados',default=0)
    sinal = models.TextField("Sinal",max_length=200)
    canal = models.IntegerField('Num_Conectados',default=0)
    frequencia = models.TextField("Frequencia",max_length=200)
    ativo = models.IntegerField('Ativo',default=0)