from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Categoria
#from .models import Contato




def index(request):
    
    parents = Categoria.objects.filter(parente=None).values()
    
    for parent in parents:
        children = Categoria.objects.filter(parente=parent['id']).values()
        parent['children'] = children
        
        for child in children:
            subchildren = Categoria.objects.filter(parente=child['id']).values()
            child['children'] = subchildren
            
    template = loader.get_template('documentos.html')
    context = {
        'parents': parents,
    }
    return HttpResponse(template.render(context, request))
