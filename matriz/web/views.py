from django.shortcuts import render

from .models import Matriz

def index(request):
    matrizes = Matriz.objects.all()
    context = {
        "matrizes": matrizes
    }
    return render(request, "web/index.html", context)

def detail(request, pk):
    matriz = Matriz.objects.get(pk = pk)
    context = {
        "matriz": matriz
    }
    return render(request, "web/detail.html", context)
