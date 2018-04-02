from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Anomalia

@login_required
def index(request):
    anomalia = Anomalia.objects.all()
    context = {'anomalias': anomalia}
    return render(request, 'anomalias/index.html', context)