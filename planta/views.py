from re import A
from urllib import request
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

def loginFormulario(request):
    return render(request, 'planta/login/login-form.html')

def login(request):
    u= request.POST["user"]
    c= request.POST["pswd"]

    if u == "Juan" and c == "12345":
        return HttpResponse("bienvenido mi rey")
    else:
        return HttpResponse("no eres bienvenido mi rey")

def sumita(request):
    return render(request, 'planta/suma/suma.html')

def sumitaResultado(request):
    a= int(request.POST["valor1"])
    b= int(request.POST["valor2"])

    r=a+b

    return HttpResponse(f"Resultado: {r}")
