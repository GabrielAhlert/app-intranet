from django.contrib import admin
from django.db import models
from django.forms import ClearableFileInput

# Register your models here.

from .models import Recado
from .models import ImagemRecado

class ImagemRecadoInline(admin.TabularInline):
    model = ImagemRecado
    extra = 1
    formfield_overrides = {
        models.FileField: {'widget': ClearableFileInput(attrs={'allow_multiple_selected': True})},
    }

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        for f in request.FILES.getlist('file'):
            ImagemRecado.objects.create(model=obj, file=f)

class RecadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'texto', 'data_inicio', 'data_fim', 'ativo')   
    inlines = [ImagemRecadoInline]

admin.site.register(Recado, RecadoAdmin)

