from django.db import models
# Create your models here.
class Log(models.Model):
    login_required = True
    description = models.TextField("Descrição",max_length=200)
    datetime = models.DateTimeField('Data Hora',auto_now_add=True)

class Meta:
    db_table = 'logs'
    managed = True
    verbose_name = 'Registros do Sistema'
    verbose_name_plural = 'Registros do Sistema'