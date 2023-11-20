from django.db import models
from product.models import Produto

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True,null=False,blank=False)
    nome_usuario = models.CharField(max_length=30,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False)
    senha = models.CharField(max_length=32,null=False,blank=False)
    id_produtos = models.ForeignKey(Produto,on_delete=models.CASCADE,null=False,blank=False)
    
    def __str__(self) -> str:
        return "Usuario ({}, {})".format(self.nome_usuario,self.email)