from django import forms 
from .models import Filter

class FilterForm(forms.ModelForm):

	description = forms.CharField(label='Descrição:', max_length=100, required=True, error_messages={'required': 'Informe a Descrição.'})
	file = forms.CharField(label='Arquivo:', max_length=100, required=True, error_messages={'required': 'Informe o Arquivo.'})
	
	class Meta:
		model  = Filter
		fields = ['description','file','priority']