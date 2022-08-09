from django.db import models

#Makemigrations planta
#Migrate 

# Create your models here.
class Trabajador(models.Model): #Herencia de el framework
    cedula = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, null=True, blank=True)
    #fecha nacimiento calcular edad

    def nombreCompleto(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique = True)
    desc = models.CharField(max_length=254)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique = True)
    ficha_tecnica = models.TextField()
    costo = models.IntegerField()
    Categoria = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)
    COLOR = (
        ('rojo','ROJO'),
        ('verde','VERDE'),
        ('azul','AZUL'),
    )    
    color = models.CharField(max_length=100, choices=COLOR, default='r')

    def __str__(self) -> str:
        return f"{self.nombre}"

class Produccion(models.Model):
    Trabajador = models.ForeignKey(Trabajador, on_delete = models.DO_NOTHING)
    Producto = models.ForeignKey(Producto, on_delete = models.DO_NOTHING)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.Producto} {self.cantidad}"
    