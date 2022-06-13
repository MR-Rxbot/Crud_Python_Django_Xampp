from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('cursos',views.cursos,name='cursos'),
    path('crear',views.crear,name='crear'),
    path('editar',views.editar,name='editar'),
]
