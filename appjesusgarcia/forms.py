from django import forms
from .models import Curso

class FormBusqueda(forms.Form):
    filtro = forms.CharField(label="Filtrar por", required=False)

class FormEstudiante(forms.Form):
    nombre = forms.CharField(label="Nombre")    
    apellidos = forms.CharField(label="Apellidos")
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(), label="Fecha de Nacimiento")
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.Select(), 
        label="Curso"
    )
    foto = forms.CharField(label="Foto")
