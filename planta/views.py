from django import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'planta/index.html')

def saludar(request):
    return HttpResponse("Hola mundo")

def despedir(request):
    return HttpResponse("Adios prro <a href='http://127.0.0.1:8000/planta/saludar/'>Click aqui</a>")

def saludoEspecial(request,nombre):
    return HttpResponse(f"Hola {nombre}")

def multiplo(request,num,num2):
    return HttpResponse(f"Hola tu resultado es {num*num2}")