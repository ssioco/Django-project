#Creacion de vistas para app
from django.urls import URLPattern, path
from . import views

app_name ="planta" #Permite utilizar un tag para usar la app

urlpatterns =[
    path('', views.index, name = "index"),
    






]