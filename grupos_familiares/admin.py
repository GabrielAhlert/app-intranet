from django import forms
from django.contrib import admin
from .models import Agricultor, GrupoFamiliar

class GrupoFamiliarAdminForm(forms.ModelForm):
    participantes = forms.ModelMultipleChoiceField(
        queryset=Agricultor.objects.all(),
        required=False,
        label="Participantes",
        widget=admin.widgets.FilteredSelectMultiple("Agricultores", is_stacked=False)
    )

    class Meta:
        model = GrupoFamiliar
        fields = ['proprietario', 'participantes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            qs = Agricultor.objects.exclude(id=self.instance.proprietario_id)
            self.fields['participantes'].queryset = qs
            self.fields['participantes'].initial = qs.filter(grupo_familiar=self.instance)
        else:
            self.fields['participantes'].queryset = Agricultor.objects.none()

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
            Agricultor.objects.filter(grupo_familiar=instance).exclude(id__in=self.cleaned_data['participantes']).update(grupo_familiar=None)
            self.cleaned_data['participantes'].update(grupo_familiar=instance)
        return instance

@admin.register(GrupoFamiliar)
class GrupoFamiliarAdmin(admin.ModelAdmin):
    form = GrupoFamiliarAdminForm
    list_display = ('id', 'proprietario')

@admin.register(Agricultor)
class AgricultorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'grupo_familiar')
    search_fields = ('nome', 'matricula')
    list_filter = ('grupo_familiar',)
