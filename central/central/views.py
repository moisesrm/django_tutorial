from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    latest_question_list = "Hello, world. You're at the polls index."
    context = {'texto': latest_question_list}
    return render(request, 'home/index.html', context)

def index_2(request):
    latest_question_list = "Hello, world. You're at the polls index."
    context = {'texto': latest_question_list}
    return render(request, 'assinaturas/index_2.html', context)

def index_3(request):
    return HttpResponse("Hello, world. You're at the polls index.")