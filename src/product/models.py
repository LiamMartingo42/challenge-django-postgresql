from django.db import models
from django.contrib.postgres.fields import DecimalRangeField

class Produto(models.Model):
    Id = models.AutoField(primary_key=True,null=False)
    nome = models.CharField(max_length=25,null=False,blank=False)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    descricao = models.TextField(max_length=50,null=False,blank=False)
    
    def __str__(self) -> str:
        return """
    Produto ({}, {}, {})""".format(self.nome,self.valor,self.descricao)