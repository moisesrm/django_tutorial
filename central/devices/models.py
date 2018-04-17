from django.db import models
from access_points.models import AccessPoint

# Create your models here.
class Device(models.Model):
    login_required = True
    access_point = models.ForeignKey('access_points.AccessPoint', on_delete=models.CASCADE)
    # id_access_point = models.IntegerField("Access Point",default=0)
    mac = models.TextField("Mac",max_length=200)
    vendor = models.TextField("Fabricante",max_length=200)
    standard = models.TextField("Padrão",max_length=200)
    channel = models.IntegerField("Canal",default=6)
    frequency = models.TextField("Frequencia",max_length=200)
    signal = models.IntegerField("Sinal",max_length=200)
    status = models.IntegerField('Status',default=0)
    last_update = models.DateTimeField('Ultima Atualizacao',auto_now_add=True)
    
    def getStrStandard(self):
        strPadrao   = "802.11"
        if self.standard == "1" : 
            strPadrao += " FHSS"
        elif self.standard == "2" : 
            strPadrao += " IR"
        elif self.standard == "3" : 
            strPadrao += " DSSS"
        elif self.standard == "4" : 
            strPadrao += "b"
        elif self.standard == "5" : 
            strPadrao += "a"
        elif self.standard == "6" : 
            strPadrao += "g"
        elif self.standard == "7" : 
            strPadrao += "n"
        elif self.standard == "8" : 
            strPadrao += "ac"

        strPadrao += " (" + self.standard + ")"
        return strPadrao

    def getStrStatus(self):
        if self.status == 1 :
            return "Ativo"
        return "Inativo"

class Meta:
    db_table = 'devices'
    managed = True
    verbose_name = 'Aparelho'
    verbose_name_plural = 'Aparelhos'
    ordering = ['mac']
