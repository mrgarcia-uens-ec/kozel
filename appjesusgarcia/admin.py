from django.contrib import admin

from .models import Estudiante
from .models import Curso
from .models import Asignatura

admin.site.register(Estudiante)
admin.site.register(Asignatura)
admin.site.register(Curso)
