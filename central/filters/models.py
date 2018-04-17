from django.db import models

# Create your models here.
class Filter(models.Model):
    login_required = True
    description = models.TextField("Descricao",max_length=200)
    file = models.TextField("Arquivo",max_length=200)
    status = models.IntegerField('Status',default=0)

    def getStrStatus(self):
        if self.status == 1 :
            return "Ativo"
        return "Inativo"

class Meta:
    db_table = 'filters'
    managed = True
    verbose_name = 'Filtro'
    verbose_name_plural = 'Filtros'
    ordering = ['id']
