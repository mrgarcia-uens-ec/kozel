from django.db import models

# Create your models here.

class TipoArticulo(models.Model):
   def __str__(self):
        return self.nombre
   
   codigo = models.CharField(max_length=50, null=True) 
   nombre = models.CharField(max_length=100, null=True)

class Articulo(models.Model):
   def __str__(self):
        return self.nombre
   
   nombre = models.CharField(max_length=100, null=True)
   descripcion = models.CharField(max_length=500, null=True)
   foto1 = models.CharField(max_length=200, null=True)
   foto2 = models.CharField(max_length=200, null=True)
   producto_mes = models.CharField(max_length=2, null=True)
   tipoArticulo = models.ForeignKey(TipoArticulo, on_delete=models.DO_NOTHING, null=True)

class Variedad(models.Model):
   def __str__(self):
        return self.producto.nombre + " " + self.talla + " " + self.color
   
   talla = models.CharField(max_length=10, null=True)
   color = models.CharField(max_length=20, null=True)
   precio = models.DecimalField
   stock = models.PositiveIntegerField(default=0)
   producto = models.ForeignKey(Articulo, on_delete=models.DO_NOTHING, null=True)

class Carrito(models.Model):
    fechaCreacion = models.DateTimeField
    usuario = models.CharField(max_length=100, null=True)

class CarritoVariedad(models.Model):
    cantidad = models.PositiveIntegerField(default=0)
    carrito = models.ForeignKey(Carrito, on_delete=models.DO_NOTHING, null=True)
    variedad = models.ForeignKey(Variedad, on_delete=models.DO_NOTHING, null=True)

class Compra(models.Model):
    fechaCreacion = models.DateTimeField
    usuario = models.CharField(max_length=100, null=True)

class CompraVariedad(models.Model):
    cantidad = models.DecimalField
    compra = models.ForeignKey(Compra, on_delete=models.DO_NOTHING, null=True)
    variedad = models.ForeignKey(Variedad, on_delete=models.DO_NOTHING, null=True)

# ============================================================
class Curso(models.Model):
    def __str__(self):
        return self.nombre
    
    nombre = models.CharField(max_length=100, null=True)

class Estudiante(models.Model):
    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    
    nombre = models.CharField(max_length=200, null=True)
    apellidos = models.CharField(max_length=200, null=True)
    fecha_nacimiento = models.DateTimeField(null=True)
    foto = models.CharField(max_length=100, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True)

class Asignatura(models.Model):
    def __str__(self):
        return self.nombre
    
    nombre = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True)
