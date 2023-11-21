from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView
from product.forms import ProdutoForms
from product.models import Produto


class Home(View):
    
    def get(self,request: HttpRequest):
        produtos = Produto.objects.order_by("Id")
        context = {'products': produtos}
        return render(request,'content/home.html', context)
    
    def post(self,request: HttpRequest):
        if not request.user.is_authenticated:
            messages.error(request,"Usuário não está logado",extra_tags='danger')
            return redirect('login')

class AddProduct(View):      
    
    def get(self,request):
        form = ProdutoForms()
        context = {'form': form}
        return render(request, 'content/addProduct.html',context)
    
    def post(self,request):
        if not request.user.is_authenticated:
            messages.error(request,"Usuário não logado",extra_tags='danger')
            return redirect('login')
        if request.method == 'POST':
            form = ProdutoForms(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Produto Adicionado!")
                return redirect('home')

class UpdateProduct(View):
    
    def get(self,request, produto_id):
        produto = Produto.objects.get(Id=produto_id)
        form = ProdutoForms(instance=produto)
        context = {
            'form': form,
            'produto_id': produto_id
        }
        return render(request, 'content/updateProduct.html', context)
    
    def post(self,request: HttpRequest, produto_id):
        produto = Produto.objects.get(Id=produto_id)
        if not request.user.is_authenticated:
            messages.error(request,"Usuário não logado",extra_tags='danger')
            return redirect('login')
        if request.method == 'POST':
            form = ProdutoForms(request.POST,instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request,"Produto Atualizado!")
            return redirect('home')
    
class DeleteProduct(View):
    
    def get(self,request: HttpRequest, produto_id):
        produto = Produto.objects.get(Id=produto_id)
        context = {'product': produto}
        return render(request, 'content/deleteProduct.html',context)
    
    def post(self,request: HttpRequest, produto_id):
        if not request.user.is_authenticated:
            messages.error(request,"Usuário não logado",extra_tags='danger')
            return redirect('login')
        produto = Produto.objects.get(Id=produto_id)
        produto.delete()
        return redirect('home')

class DetailProduct(View):
    
    def get(self,request: HttpRequest, produto_id):
        produto = Produto.objects.get(Id=produto_id)
        context = {'product': produto}
        return render(request, 'content/detailProduct.html', context)
    
    def post(self,request: HttpRequest):
        if not request.user.is_authenticated:
            messages.error(request,"Usuário não logado",extra_tags='danger')
            return redirect('login')