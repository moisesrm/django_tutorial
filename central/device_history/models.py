from django.db import models
from devices.models import Device
from access_points.models import AccessPoint
# Create your models here.
class DeviceHistory(models.Model):
    login_required = True
    id_device = models.IntegerField("Canal",default=0)
    id_access_point = models.IntegerField("Canal",default=0)
    channel = models.IntegerField("Canal",default=6)
    frequency = models.TextField("Frequencia",max_length=200)
    signal = models.TextField("Sinal",max_length=200)
    description = models.TextField("Descrição",max_length=200)
    datetime = models.DateTimeField('Data Hora',auto_now_add=True)

class Meta:
    db_table = 'device_history'
    managed = True
    verbose_name = 'Historico'
    verbose_name_plural = 'Historico'