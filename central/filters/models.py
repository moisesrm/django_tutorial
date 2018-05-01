from django.db import models

# Create your models here.

PRIORIDADES = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10))

class Filter(models.Model):
    login_required = True
    description = models.TextField("Descricao",max_length=200)
    file = models.TextField("Arquivo",max_length=200)
    status = models.IntegerField('Status',default=0)
    priority = models.CharField('Prioridade',max_length=6, choices=PRIORIDADES, default='5')

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
