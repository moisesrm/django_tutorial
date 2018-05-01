from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import AccessPoint

@login_required
def index(request):
    accessPoints = AccessPoint.objects.all()
    context = {'accessPoints': accessPoints}
    return render(request, 'access_points/index.html', context)


@login_required
def inativar_registro(request,id):
    accessPoints = get_object_or_404(Filter,id=id)
    if accessPoints:
        accessPoints.active ='0'
        accessPoints.save()
        messages.success(request,"Desativado com sucesso!")
        return redirect("filter:index")

@login_required
def ativar_registro(request,id):
    accessPoints = get_object_or_404(Filter,id=id)
    if accessPoints:
        accessPoints.active = '1'
        accessPoints.save()
        messages.success(request,"Ativado com sucesso!")
        return redirect("filter:index")