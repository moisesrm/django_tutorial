from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from devices.models import Device
from access_points.models import AccessPoint
from logs.models import Log

@login_required
def index(request):
    return render(request, 'relatorios/index.html')

@login_required
def aparelhos(request):
    aps = AccessPoint.objects.all().annotate(aparelhos=Count('device'))
    print(aps)
    context = {'aps': aps}
    return render(request, 'relatorios/relatorio_aparelhos.html', context)

@login_required
def canal(request):
    aps = AccessPoint.objects.all()
    canal = {}
    for ap in aps:
        if ap.channel not in canal:
            canal[ap.channel] = [ap.channel,0]
        canal[ap.channel][1] += 1
    context = {'canais': canal}
    return render(request, 'relatorios/relatorio_canal.html', context)

@login_required
def sinal(request):
    devices = Device.objects.all().order_by('-signal')[:10] 
    context = {'devices': devices}
    return render(request, 'relatorios/relatorio_sinal.html', context)