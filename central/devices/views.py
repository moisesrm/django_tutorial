from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Device

@login_required
def index(request):
    devices = Device.objects.all()
    context = {'devices': devices}
    return render(request, 'devices/index.html', context)