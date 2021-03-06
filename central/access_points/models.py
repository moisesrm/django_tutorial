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
    active = models.IntegerField("Ativo")

    def __str__(self):
        return "%s" % (self.bssid)

    def getStrPadrao(self):
        if self.standard == "1":
            return "802.11 FHSS"
        elif self.standard == "2":
            return "802.11 IR"
        elif self.standard == "3":
            return "802.11 DSSS"
        elif self.standard == "4":
            return "802.11b"
        elif self.standard == "5":
            return "802.11a"
        elif self.standard == "6":
            return "802.11g"
        elif self.standard == "7":
            return "802.11n"
        elif self.standard == "8":
            return "802.11ac"
        else:
            return "802.11"
        

class Meta:
    db_table = 'access_points'
    managed = True
    verbose_name = 'Acess Point'
    verbose_name_plural = 'Acess Points'
    ordering = ['bssid']
