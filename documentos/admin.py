from django.contrib import admin
from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_active')
    search_fields = ['name']
    list_filter = ['is_active']

admin.site.register(Categoria, CategoriaAdmin)
