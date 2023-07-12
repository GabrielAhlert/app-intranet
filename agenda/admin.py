from django.contrib import admin
from .models import Contato, Unidade, Funcao

class AgendaMonthFilter(admin.SimpleListFilter):
    title = 'Mês'
    parameter_name = 'data__month'
    default_value = None
    def lookups(self, request, model_admin):
        lista_meses = [(1,'Janeiro'),(2,'Fevereiro'),(3,'Março'),(4,'Abril'),(5,'Maio'),(6,'Junho'),(7,'Julho'),(8,'Agosto'),(9,'Setembro'),(10,'Outubro'),(11,'Novembro'),(12,'Dezembro')]
        return lista_meses
    
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(nascimento__month=self.value())
        else:
            return queryset

class AgendaAdmin(admin.ModelAdmin):
    list_filter = (AgendaMonthFilter, 'unidade', 'ramal_ativo', 'pessoa_ativo', 'funcao')
    search_fields = ['nome', 'ramal', 'telefone', 'unidade__nome', 'funcao__nome']
    list_display = ('nome', 'ramal', 'telefone',  'ramal_ativo', 'pessoa_ativo', 'nascimento')
    list_max_show_all = 5000
    
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ['nome']

class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ['nome']
    

admin.site.register(Contato, AgendaAdmin)
admin.site.register(Unidade, UnidadeAdmin)
admin.site.register(Funcao, FuncaoAdmin)