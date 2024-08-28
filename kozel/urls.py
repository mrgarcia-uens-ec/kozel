from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hola", views.index, name="index"),
    path("adios", views.adios, name="adios"),
    path("mostrarhtml", views.mostrarhtml, name="mostrarhtml"),
    path("lista_de_asignaturas", views.lista_de_asignaturas, name="lista_de_asignaturas"),
    path("estudiantes", views.lista_de_estudiantes, name="lista_de_estudiantes"),
    path("estudiante/<int:id_estudiante>/", views.detalle_estudiante, name="detalle_estudiante"),
]