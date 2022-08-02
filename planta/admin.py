from django.contrib import admin
from .models import Categoria, Produccion, Producto, Trabajador

# Register your models here.

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'cedula', 'nombre', 'apellido', 'correo')
    search_fields = ['nombre','apellido','cedula']

admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Categoria)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ficha_tecnica', 'costo', 'Categoria','descripcionCategoria','color' )
    list_filter = ['Categoria']
    search_fields = ['nombre','Categoria__nombre']
    list_editable = ['color']

    def descripcionCategoria(self,obj):
        return obj.Categoria.desc


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Produccion)
