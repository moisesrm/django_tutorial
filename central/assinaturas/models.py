from django.db import models
from anomalias.models import Anomalia
# Create your models here.
class Assinatura(models.Model):
    login_required = True
    id_anomalia = models.ForeignKey(Anomalia,on_delete=models.CASCADE)
    nome = models.CharField("Nome",max_length=200)
    descricao = models.CharField("Descrição",max_length=200)
    assinatura = models.CharField("Assinatura",max_length=200)
    ativo = models.IntegerField("Ativo",default=1)
    data_cad = models.DateTimeField("Data de Cadastro",auto_now_add=True)