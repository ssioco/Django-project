from urllib import request
from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


#Mensajes tipo cookie temporales
from django.contrib import messages

#Gestion de Errores de base de datos
from django.db import IntegrityError

#Importe de modelos para las consultas
from .models import Categoria, Produccion, Producto, Trabajador

# Create your views here.
def index(request):
    return render(request, 'planta/index.html')

def listarTrabajadores(request):
    q = Trabajador.objects.all()
    context = { "datos": q }
    return render(request, 'planta/trabajador/listar_trabajador.html', context)

def formularioTrabajador(request):
    return render(request, 'planta/trabajador/nuevo_trabajador.html')

def guardarTrabajador(request):
    try:
        if request.method == "POST":
            q = Trabajador(
                cedula = request.POST["cedula"],
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                correo = request.POST["correo"]
            )
            q.save()
            messages.success(request, "Trabajador guardado correctamente")
        else:
            messages.warning(request, "Usted no ha enviado datos..")
    except Exception as e:
        messages.error(request, f"Error: {e}")
    return redirect('planta:listarTrabajador')
