from django.shortcuts import render
from django.http import HttpRequest
from .models import Produto, Usuario

def index(request: HttpRequest):
    return render(request,'index.html')

def listar(request: HttpRequest):
    pass

def delete(request: HttpRequest):
    pass

def update(request: HttpRequest):
    pass

def include(request: HttpRequest):
    pass