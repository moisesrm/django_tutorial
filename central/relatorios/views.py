from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from devices.models import Device
from access_points.models import AccessPoint
from logs.models import Log

@login_required
def index(request):
    aps = AccessPoint.objects.all().annotate(Count('device'))
    context = {'aps': aps}
    return render(request, 'logs/index.html', context)

@login_required
def index(request):
    devices = Device.objects.all().order_by('-id')[:10] 
    context = {'devices': devices}
    return render(request, 'logs/index.html', context)