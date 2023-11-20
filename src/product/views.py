from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.messages import error, success
from .models import Produto

def index(request: HttpRequest):
    if not request.user.is_authenticated:
        error(request,"Usuário não logado")
        return redirect('login')
    return render(request,'content/index.html')

def listar(request: HttpRequest):
    pass

def delete(request: HttpRequest):
    pass

def update(request: HttpRequest):
    pass

def include(request: HttpRequest):
    pass