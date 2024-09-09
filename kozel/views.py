from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from django.db.models import Q

from .models import Curso
from .models import Asignatura
from .models import Estudiante

from .forms import FormBusqueda
from .forms import FormEstudiante
from .forms import FormCarrito

from .models import TipoArticulo
from .models import Articulo
from .models import Variedad
from .models import Carrito
from .models import CarritoVariedad

import uuid

def index(request):
    contexto = { }
    return render(request, "inicio.html", contexto)

def busqueda(request):
    # Generar un usuario
    if 'userid' not in request.session:
        request.session['userid'] = str(uuid.uuid1())

    form = FormBusqueda()    
    lista_productos_mes = Articulo.objects.filter(producto_mes = 'SI')

    contexto = { 
        "form" : form,
        "lista_productos_mes": agrupar_en_filas(lista_productos_mes)
    }
    return render(request, "busqueda.html", contexto)

def catalogo(request):
    if request.method == 'POST':
        form = FormBusqueda(request.POST)
        if form.is_valid():
            filtro = form.cleaned_data["filtro"]
            filtroQ = Q(nombre__contains=filtro) | Q(descripcion__contains=filtro)

            productos_filtrados = Articulo.objects.filter(filtroQ)
            contexto = {
                "filtro": filtro, 
                "productos_filtrados": agrupar_en_filas(productos_filtrados),
            }
            return render(request, "catalogo.html", contexto)
               
def detalle(request, id_articulo, color_seleccionado, talla_seleccionada):
    articulo = Articulo.objects.get(pk=id_articulo)
    form = FormCarrito(request.POST)

    if request.method == 'POST':
        # Buscar la variadad seleccionada por el cliente
        variedad = Variedad.objects.filter(producto=articulo, talla=talla_seleccionada, color=color_seleccionado).get()

        # Insertar una fila en el carrito
        # Comprobar que el carrito existe
        usuario = request.session['userid']
        carrito = Carrito.objects.filter(usuario = usuario)
        if not carrito:
            carrito = Carrito(usuario = usuario)
            carrito.save()
        else:
            carrito = carrito.get()

        # obtener la cantidad
        cantidad = int(form.data["cantidad"])

        # Crear la variedad si no existe. Si existe, añadir la cantidad
        carritoVariedad = CarritoVariedad.objects.filter(carrito=carrito, variedad=variedad)

        if not carritoVariedad:
            carritoVariedad = CarritoVariedad(cantidad=cantidad, carrito=carrito, variedad=variedad)
            carritoVariedad.save()
        else:
            nueva_cantidad = carritoVariedad.get().cantidad + cantidad
            carritoVariedad.update(cantidad = nueva_cantidad)

        return redirect('/kozel/busqueda')
    
    else:
        variedades = Variedad.objects.filter(producto = articulo).values()

        tallas = set([variedad['talla'] for variedad in variedades])
        colores = set([variedad['color'] for variedad in variedades])

        if talla_seleccionada == '@':
            talla_seleccionada = list(tallas)[0]

        if color_seleccionado == '@':
            color_seleccionado = list(colores)[0]
        
        contexto = {
            "articulo" : articulo,
            "tallas" : tallas,
            "colores" : colores,
            "talla_seleccionada" : talla_seleccionada,
            "color_seleccionado" : color_seleccionado,
            "form" : form
        }
        
        return render(request, "detalle.html", contexto)

def agrupar_en_filas(productos):
    # Crear una lista de listas con cuatro productos por fila
    filas = []
    columnas = []
    columna = 0
    for p in productos:
        columnas.append(p)
        columna = columna + 1

        if columna > 3:
            filas.append(columna)
            columna = 0
            columnas = []
    
    filas.append(columnas)
    return filas









# ===========================================================
def adios(request):
    return HttpResponse("Adiós")

def mostrarhtml(request):
    lista_cursos = Curso.objects.all()
    contexto = {
        "lista_cursos": lista_cursos
    }
    return render(request, "cursos.html", contexto)

def lista_de_asignaturas(request):
    lista_asignaturas = Asignatura.objects.all()
    contexto = {
        "lista_asignaturas": lista_asignaturas,
        "equipos_de_futbol": ["Real Madrid", "Atlético de Madrid", "Español"],
        "mi_nombre": "Pepe"
    }
    return render(request, "asignaturas.html", contexto)

def lista_de_estudiantes(request):
    if request.method == 'POST':
        form = FormBusqueda(request.POST)
        if form.is_valid():
            filtro = form.cleaned_data["filtro"]
            filtroQ = Q(nombre__contains=filtro) | Q(apellidos__contains=filtro)
    else:
        form = FormBusqueda()
        filtroQ = ~Q(pk__in=[])
    
    lista_estudiantes = Estudiante.objects.filter(filtroQ)
    contexto = {
        "lista_estudiantes": lista_estudiantes,
        "form": form
    }
    return render(request, "estudiantes.html", contexto)

def detalle_estudiante(request, id_estudiante):
    if request.method == 'POST':
        form = FormEstudiante(request.POST)
        if form.is_valid():
            Estudiante.objects.filter(pk=id_estudiante).update(
                nombre = form.cleaned_data["nombre"],
                apellidos = form.cleaned_data["apellidos"],
                fecha_nacimiento = form.cleaned_data["fecha_nacimiento"],
                foto = form.cleaned_data["foto"],
                curso_id = form.cleaned_data["curso"].id                
            )
            return redirect(lista_de_estudiantes)
    else:
        estudiante = Estudiante.objects.get(pk=id_estudiante)
        form = FormEstudiante()
        form.initial['nombre'] = estudiante.nombre
        form.initial['apellidos'] = estudiante.apellidos
        form.initial['fecha_nacimiento'] = estudiante.fecha_nacimiento
        form.initial['foto'] = estudiante.foto
        form.initial['curso'] = estudiante.curso

        contexto = {
            "estudiante": estudiante,
            "form": form
        }
        return render(request, "estudiante.html", contexto)
