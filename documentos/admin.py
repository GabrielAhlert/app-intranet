from django.contrib import admin
from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    #readonly_fields = ['profundidade',]
    list_display = ('nome', 'parente', 'categoria_ativa')
    search_fields = ['nome']

admin.site.register(Categoria, CategoriaAdmin)
