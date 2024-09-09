from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("busqueda", views.busqueda, name="busqueda"),
    path("catalogo", views.catalogo, name="catalogo"),
    path("detalle/<int:id_articulo>/<str:color_seleccionado>/<str:talla_seleccionada>", views.detalle, name="detalle"),    
]