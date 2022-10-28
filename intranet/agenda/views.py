from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Contato

def index(request):
    template = loader.get_template('agenda.html')
    context = {
        'Contatos': Contato.objects.filter(ramal_ativo=True).order_by('ramal'),
    }
    return HttpResponse(template.render(context, request))



