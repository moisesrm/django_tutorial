from django.db import models
from device_history.models import DeviceHistory
from devices.models import Device
from access_points.models import AccessPoint
# Create your models here.
class DeviceHistory(models.Model):
    login_required = True
    id_device = model.ForeignKey(AccessPoint, verbose_name='device', on_delete='models.CASCADE', related_name='device_history')
    id_access_point = model.ForeignKey(AccessPoint, verbose_name='access_point', related_name='device_history')
    channel = models.IntegerField("Canal",default=6)
    frequency = models.TextField("Frequencia",max_length=200)
    signal = models.TextField("Sinal",max_length=200)
    description = models.TextField("Descrição",max_length=200)
    datetime = models.DatetimeField('Data Hora',auto_now_add=True)

class class Meta:
    db_table = 'device_history'
    managed = True
    verbose_name = 'Historico'
    verbose_name_plural = 'Historico'