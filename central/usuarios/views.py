from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (get_user_model)

# Create your views here.
User = get_user_model()

@login_required
def listagem(request):
    user = User.objects.all() #lista todos os usuarios
    template_name = 'usuarios/index.html'
    context = {'users': user}
    return render(request, template_name, context)