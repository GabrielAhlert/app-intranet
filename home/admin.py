from django.contrib import admin
from .models import Banner, Evento

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ['titulo','imagem']

class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo','local','data']

admin.site.register(Banner, BannerAdmin)
admin.site.register(Evento, EventoAdmin)
