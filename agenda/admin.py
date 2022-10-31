from django.contrib import admin
from .models import Contato, Unidade, Funcao

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ramal', 'telefone',  'ramal_ativo', 'pessoa_ativo')

class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Contato, AgendaAdmin)
admin.site.register(Unidade, UnidadeAdmin)
admin.site.register(Funcao, FuncaoAdmin)