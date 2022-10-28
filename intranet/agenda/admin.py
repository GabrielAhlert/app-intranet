from django.contrib import admin
from .models import Contato, Unidade

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ramal', 'telefone',  'ramal_ativo', 'pessoa_ativo')

class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Contato, AgendaAdmin)
admin.site.register(Unidade, UnidadeAdmin)