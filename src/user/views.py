from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.middleware.csrf import CsrfViewMiddleware
from http import HTTPStatus
from .forms import LoginForms, SignInForms

def login(request: HttpRequest):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form["nomeLogin"].value()
            senha = form["senhaLogin"].value()
            
        userlogin = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        print(userlogin)
        if userlogin is not None:
            auth.login(request, userlogin)
            messages.success(request,f"{nome} logado com sucesso")
            return redirect('home')
        else:
            messages.error(request,"Erro ao efetuar login")
            return redirect('login')
            
    return render(request,'auth/login.html',{'form': form})

def signin(request: HttpRequest):
    form = SignInForms()
    
    if request.method == 'POST':
        form = SignInForms(request.POST)
        if form.is_valid():
            
            nome = form["nomeSignIn"].value()
            email = form["email"].value()
            senha = form["senhaSignIn"].value()

            if User.objects.filter(username=nome, email=email).exists():
                messages.error(request, "Essa conta já existe!")
                return redirect('signin')

            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            user.save()
            messages.success(request, "Conta efetuada com sucesso")
            return redirect('home')
    return render(request,'auth/signin.html', {'form': form})

def logout(request: HttpRequest):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect('login')