from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Log

@login_required
def index(request):
    #logs = Log.objects.all()
    logs = []
    context = {'logs': logs}
    return render(request, 'logs/index.html', context)