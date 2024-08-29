from django.contrib import admin

from .models import Estudiante
from .models import Curso
from .models import Asignatura
from .models import TipoArticulo
from .models import Articulo
from .models import Variedad
from .models import Carrito
from .models import CarritoVariedad
from .models import Compra
from .models import CompraVariedad

admin.site.register(Estudiante)
admin.site.register(Asignatura)
admin.site.register(Curso)
admin.site.register(TipoArticulo)
admin.site.register(Articulo)
admin.site.register(Variedad)
admin.site.register(Carrito)
admin.site.register(CarritoVariedad)
admin.site.register(Compra)
admin.site.register(CompraVariedad)
