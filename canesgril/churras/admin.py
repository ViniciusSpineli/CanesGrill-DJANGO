from django.contrib import admin
from .models import Cliente, Produto

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    search_fields = ('nome', 'sobrenome', 'email')
    list_filter = ('nome', 'sobrenome', 'email')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    search_fields = ('nome', 'preco')
    list_filter = ('nome', 'preco')

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Produto)