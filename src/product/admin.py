from django.contrib import admin
from .models import Produto

class ListProducts(admin.ModelAdmin):
    list_display = ("Id","nome","valor","descricao")
    list_display_links = ("Id","nome")
    search_fields = ("nome",)

admin.site.register(Produto, ListProducts)