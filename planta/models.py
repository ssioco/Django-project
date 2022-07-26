from django.db import models

# Create your models here.
class Trabajador(models.Model):
    cedula = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"