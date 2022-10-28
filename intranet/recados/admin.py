from django.contrib import admin

# Register your models here.

from .models import Recado

class RecadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'texto', 'data_inicio', 'data_fim', 'ativo')

admin.site.register(Recado, RecadoAdmin)
