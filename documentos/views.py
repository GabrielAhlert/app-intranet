from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Categoria
#from .models import Contato

def index(request, Categorias_id):
    template = loader.get_template('documentos.html')
    context = {
        'categorias': Categoria.objects.all()
    }
    return HttpResponse(template.render(context, request))