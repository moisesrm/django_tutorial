from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AnomaliaForm
from .models import Anomalia

@login_required
def index(request):
    anomalia = Anomalia.objects.all()
    context = {'anomalias': anomalia}
    return render(request, 'anomalias/index.html', context)

def formulario(request, id=None):
    if request.method == 'POST':
        form = AnomaliaForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('anomalias:index')
    else:
        pagina = "Nova"
        form = AnomaliaForm()
        if id is not None:
            pagina = "Editar"
            anomalia = get_object_or_404(Anomalia,id=id)  
            form = EditarAnomaliaForm(instance=anomalia)
        pagina += " Anomalia"
        context = {'form': form,'pagina': pagina}

    return render(request, 'formulario.html', context)