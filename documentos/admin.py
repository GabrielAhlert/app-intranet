from django.contrib import admin
from .models import Categoria, Documento

class CategoriaAdmin(admin.ModelAdmin):
    #readonly_fields = ['profundidade',]
    list_display = ('nome', 'icone', '__str__', 'parente', 'categoria_ativa')
    search_fields = ['nome']
    
class documentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'arquivo')
    search_fields = ['nome']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Documento, documentoAdmin)
