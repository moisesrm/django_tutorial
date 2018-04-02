from django.db import models
from access_points.models import AccessPoint

# Create your models here.
class Device(models.Model):
    login_required = True
    id_access_point = models.IntegerField("Access Point",default=0)
    mac = models.TextField("Mac",max_length=200)
    vendor = models.TextField("Fabricante",max_length=200)
    standard = models.TextField("Padrão",max_length=200)
    channel = models.IntegerField("Canal",default=6)
    frequency = models.TextField("Frequencia",max_length=200)
    signal = models.TextField("Sinal",max_length=200)
    status = models.IntegerField('Status',default=0)
    last_update = models.DateTimeField('Ultima Atualizacao',auto_now_add=True)

class Meta:
    db_table = 'devices'
    managed = True
    verbose_name = 'Aparelho'
    verbose_name_plural = 'Aparelhos'
    ordering = ['mac']