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
    list_display = ('id', 'nome_prato', 'categoria', 'tempo_preparo', 'publicado')
    list_display_links = ('id', 'nome_prato')
    search_fields = ('nome_prato',)
    list_filter = ('categoria',)
    list_editable = ('publicado',)
    ordering = ('id',)

    actions = ['marcar_como_publicado', 'desmcarcar_como_publicado']
    
    def marcar_como_publicado (self, request, queryset):
        atualizados = queryset.update(publicado=True)
        self.message_user(request, f"{atualizados} pratos foram marcados como publicados.")
    
    marcar_como_publicado.short_description = "Publicar Todos"

    def desmcarcar_como_publicado (self, request, queryset):
        atualizados = queryset.update(publicado=False)
        self.message_user(request, f"{atualizados} pratos foram desmarcados como publicados.")
    
    desmcarcar_como_publicado.short_description = "Desmarcar Todos"

admin.site.register(Prato, ListandoPratos)
