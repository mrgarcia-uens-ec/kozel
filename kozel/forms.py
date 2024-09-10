from django import forms

class FormBoton(forms.Form):
     texto = forms.CharField(label="Botón")

class FormBusqueda(forms.Form):
    filtro = forms.CharField(label="Buscar prendas en el catálogo", required=False)

class FormCarrito(forms.Form):
    cantidad = forms.IntegerField(
        label="Cantidad", 
        required=False, 
        show_hidden_initial=True,
        initial=1, 
        min_value=1, 
        widget=forms.NumberInput(attrs={'required': 'True', 'class': 'number-widget'})
    )
