from django.contrib import admin
from .models import Categoria, Produccion, Producto, Trabajador

# Register your models here.

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'cedula', 'nombre', 'apellido', 'correo', 'nombreCompleto')
    search_fields = ['nombre','apellido','cedula']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'desc')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ficha_tecnica', 'costo', 'Categoria','descripcionCategoria','color' )
    list_filter = ['Categoria']
    search_fields = ['nombre','Categoria__nombre']
    list_editable = ['color']

    def descripcionCategoria(self,obj):
        return obj.Categoria.desc

@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('Trabajador', 'Producto', 'cantidad', 'fecha_creacion', )