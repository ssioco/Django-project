from re import A
from urllib import request
from django import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'planta/index.html')


