from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Filter
from .forms import FilterForm
from django.contrib import messages
from django.db import IntegrityError


@login_required
def index(request):
    filters = Filter.objects.all()
    context = {'filters': filters}
    return render(request, 'filters/index.html', context)

@login_required
def registro(request):
    form = FilterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Registrado com sucesso!")
        return redirect("filter:index")
    context = {'form': form}
    return render(request, 'filters/form.html', context)

@login_required
def editar_registro(request,id):
    filtro = get_object_or_404(Filter,id=id)
    form = FilterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Editado com sucesso!")
        return redirect("filter:index")
    else:
        form = FilterForm(instance=filtro)
    context = {'form': form}
    return render(request, 'filters/form.html', context)

@login_required
def deletar_registro(request,id):
    filtro = get_object_or_404(Filter,id=id)
    if filtro:
        filtro.delete()
        messages.success(request,"Deletado com sucesso!")
        return redirect("filter:index")

@login_required
def inativar_registro(request,id):
    filtro = get_object_or_404(Filter,id=id)
    if filtro:
        filtro.update(ativo='0')
        return redirect("filter:index")

@login_required
def ativar_registro(request,id):
    filtro = get_object_or_404(Filter,id=id)
    if filtro:
        filtro.update(ativo='1')
        return redirect("filter:index")