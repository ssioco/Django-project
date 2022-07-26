#Creacion de vistas para app
from django.urls import URLPattern, path
from . import views

app_name ="planta" #Permite utilizar un tag para usar la app

urlpatterns =[
    path('', views.index, name = "index"),
    path('saludar/', views.saludar, name = "saludar"),
    path('adios/', views.despedir, name = "despedir"),
    path('saludo-especial/<str:nombre>', views.saludoEspecial, name = "especial"),
    path('numero/<int:num>/<int:num2>', views.multiplo, name = "multiplo"),

    path('login-fornulario/', views.loginFormulario, name = "loginf"),
    path('login/', views.login, name = "login"),
    path('sumita/', views.sumita, name = "sumita"),
    path('sumitaRes/', views.sumitaResultado, name = "sumitaRes"),






]