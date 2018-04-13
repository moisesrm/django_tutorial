from django.db import models
# Create your models here.
class AccessPoint(models.Model):
    login_required = True
    mac = models.CharField("Mac",max_length=200)
    bssid = models.CharField("BSSID",max_length=200)
    bandwidth = models.CharField("Largura da Banda",max_length=200)
    standard = models.CharField("Padrão",max_length=200)
    channel = models.IntegerField("Canal",default=6)
    frequency = models.IntegerField("Frequencia")

class Meta:
    db_table = 'access_points'
    managed = True
    verbose_name = 'Acess Point'
    verbose_name_plural = 'Acess Points'
    ordering = ['bssid']
