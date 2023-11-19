from django.db import models

class Produto(models.Model):
    Id = models.AutoField(primary_key=True,null=False)
    nome = models.CharField(max_length=25,null=False,blank=False)
    valor = models.DecimalField(decimal_places=2,max_digits=100000,null=False,blank=False)
    descricao = models.TextField(max_length=100,null=False,blank=False)
    
    def __str__(self) -> str:
        return """
    Produto ({}, {}, {})""".format(self.nome,self.valor,self.descricao)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True,null=False,blank=False)
    nome_usuario = models.CharField(max_length=30,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False)
    senha = models.CharField(max_length=32,null=False,blank=False)
    id_produtos = models.ForeignKey(Produto, on_delete=models.CASCADE,null=False,blank=False)
    
    def __str__(self) -> str:
        return "Usuario ({}, {})".format(self.nome_usuario,self.email)