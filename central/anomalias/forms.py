from django import forms 
from .models import Anomalia

class AnomaliaForm(forms.ModelForm):
	descricao = forms.CharField(label='Descrição:', max_length=200, required=True, error_messages={'required': 'Informe a Descrição.'})
	identificador = forms.CharField(label='Identificação:', max_length=200, required=True, error_messages={'required': 'Informe a Identificação.'})
	class Meta:
		model  = Anomalia
		fields = ['descricao','identificador']