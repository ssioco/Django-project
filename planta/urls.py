#Creacion de vistas para app
from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('', views.index, name = "index"),
    path('saludar/', views.saludar, name = "saludar"),
    path('adios/', views.despedir, name = "despedir"),
    path('saludo-especial/<str:nombre>', views.saludoEspecial, name = "especial"),
    path('numero/<int:num>/<int:num2>', views.multiplo, name = "multiplo"),


]