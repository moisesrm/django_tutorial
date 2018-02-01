from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AssinaturaForm
from .models import Assinatura

@login_required
def index(request):
    assinatura = Assinatura.objects.all()
    context = {'assinaturas': assinatura}
    return render(request, 'assinaturas/index.html', context)

def formulario(request, id=None):
    if request.method == 'POST':
        form = AssinaturaForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('assinaturas:index')
    else:
        pagina = "Nova"
        form = AssinaturaForm()
        if id is not None:
            pagina = "Editar"
            assinatura = get_object_or_404(Assinatura,id=id)  
            form = EditarAssinaturaForm(instance=assinatura)
        pagina += " Assinatura"
        context = {'form': form,'pagina': pagina}

    return render(request, 'formulario.html', context)