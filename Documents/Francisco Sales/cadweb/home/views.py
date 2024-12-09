from django.shortcuts import render
from . models import Categoria



def index(request):
    return render(request,'index.html')

def categorias(request):
    lista = Categoria.objects.all()
    return render(request,'categoria/lista.html',{'lista':lista})

