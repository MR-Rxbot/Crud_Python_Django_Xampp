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

def editar(request,id):
    curso = Curso.objects.get(id=id)
    formulario = CursoForm(request.POST or None, request.FILES or None, instance=curso)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect ('cursos')
    return render(request,'cursos/editar.html',{'formulario': formulario})

def eliminar(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect("cursos")