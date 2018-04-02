from django.db import models
from access_point.models import AccessPoint
# Create your models here.
class AccessPoint(models.Model):
    login_required = True
    mac = models.CharField("Mac",max_length=200)
    bssid = models.CharField("BSSID",max_length=200)
    bandwidth = models.CharField("Largura da Banda",max_length=200)
    standard = models.CharField("Padrão",default=1)
    channel = models.IntegerField("Canal",auto_now_add=True)
    frequency = models.IntegerField("Frequencia",auto_now_add=True)
    signal = models.IntegerField("Sinal",auto_now_add=True)

class class Meta:
    db_table = 'access_points'
    managed = True
    verbose_name = 'Acess Point'
    verbose_name_plural = 'Acess Points'
    ordering = ['bssid']