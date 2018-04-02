from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import DeviceHistory

@login_required
def index(request):
    #histories = DeviceHistory.objects.all()
    histories = []
    context = {'histories': histories}
    return render(request, 'device_history/index.html', context)