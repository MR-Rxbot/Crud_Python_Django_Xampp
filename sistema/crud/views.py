from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')


def nosotros(request):
    return render(request,'nosotros.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request,'cursos/index.html',{'cursos': cursos})

def crear(request):
    return render(request,'cursos/crear.html')

def editar(request):
    return render(request,'cursos/editar.html')