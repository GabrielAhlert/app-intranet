from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from .models import Contato

def index(request):
    template = loader.get_template('documentos.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))