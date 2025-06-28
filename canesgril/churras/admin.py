from django.contrib import admin
from .models import Cliente, Produto, Prato

#class ClienteAdmin(admin.ModelAdmin):
#    list_display = ('nome', 'sobrenome', 'email')
#    search_fields = ('nome', 'sobrenome', 'email')
#    list_filter = ('nome', 'sobrenome', 'email')

#class ProdutoAdmin(admin.ModelAdmin):
#    list_display = ('nome', 'preco', 'estoque')
#    search_fields = ('nome', 'preco')
#    list_filter = ('nome', 'preco')

# Register your models here.
#dmin.site.register(Cliente)
#admin.site.register(Produto)

class ListandoPratos(admin.ModelAdmin):
    list_display = ('id', 'nome_prato', 'categoria', 'tempo_preparo')
    list_display_links = ('id', 'nome_prato')
    search_fields = ('nome_prato',)
    list_filter = ('categoria',)
    list_per_page = 12
    ordering = ('id',)


admin.site.register(Prato, ListandoPratos)
