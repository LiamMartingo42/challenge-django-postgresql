from django.contrib import admin
from .models import Usuario, Produto

class ListProducts(admin.ModelAdmin):
    list_display = ("Id","nome","valor","descricao")
    list_display_links = ("Id","nome")
    search_fields = ("nome",)
    
class ListUsuario(admin.ModelAdmin):
    list_display = ("id_usuario","nome_usuario","email","senha")
    list_display_links = ("id_usuario","nome_usuario","email",)
    search_fields = ("nome_usuario","email",)

admin.site.register(Produto, ListProducts)
admin.site.register(Usuario, ListUsuario)