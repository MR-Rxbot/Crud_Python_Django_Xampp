from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Curso
from .forms import CursoForm

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')


def nosotros(request):
    return render(request,'nosotros.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request,'cursos/index.html',{'cursos': cursos})

def crear(request):
    formulario = CursoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("cursos")
    return render(request,'cursos/crear.html',{'formulario': formulario})

def editar(request):
    return render(request,'cursos/editar.html')

def eliminar(request,id):
    Curso = Curso.objects.get(id=id)
    Curso.delete()
    return redirect("cursos")