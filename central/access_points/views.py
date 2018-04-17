from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import AccessPoint

@login_required
def index(request):
    accessPoints = AccessPoint.objects.all()
    context = {'accessPoints': accessPoints}
    return render(request, 'access_points/index.html', context)