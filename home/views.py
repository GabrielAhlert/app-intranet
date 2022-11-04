from django.shortcuts import render
import datetime
from recados.models import Recado
from agenda.models import Contato
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    template = loader.get_template('home.html')
    today = datetime.datetime.now()
    data = Contato.objects.filter(nascimento__month=today.month, pessoa_ativo=True).order_by('nascimento__day')
    Pessoas = [data[x:x+12] for x in range(0, len(data), 12)]
    context = {
        'Recados': Recado.objects.filter(ativo=True, data_inicio__lte=today, data_fim__gte=today),
        'Pessoas': Pessoas
    }
    return HttpResponse(template.render(context, request))