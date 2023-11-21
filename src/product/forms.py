from django import forms
from product.models import Produto

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ['Id',]
        
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição do Produto',
            'valor':  'Valor do Produto(R$)'
        }
        
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control text-light',
                    'style': 'background-color: rgb(71, 71, 71);'
                }
            ),
            'valor': forms.NumberInput(
                attrs={
                    'class': 'form-control text-light',
                    'style': 'background-color: rgb(71, 71, 71);'
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control text-light',
                    'style': 'background-color: rgb(71, 71, 71);'
                }
            )
        }
        