from django import forms 
from .models import Assinatura

class AssinaturaForm(forms.ModelForm):
	descricao = forms.CharField(label='Descrição:', max_length=100, required=True, error_messages={'required': 'Informe a Descrição.'})
	class Meta:
		model  = Assinatura
		fields = ['descricao']