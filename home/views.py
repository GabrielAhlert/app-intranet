from django.shortcuts import render
import datetime
from recados.models import Recado
from agenda.models import Contato
from django.http import HttpResponse
from django.template import loader
from .models import Banner, Evento
import json


# Create your views here.

def index(request):
    template = loader.get_template('home.html')
    today = datetime.datetime.now()
    data = Contato.objects.filter(nascimento__month=today.month, pessoa_ativo=True).order_by('nascimento__day')
    Pessoas = [data[x:x+12] for x in range(0, len(data), 12)]
    context = {
        'Recados': Recado.objects.filter(ativo=True, data_inicio__lte=today, data_fim__gte=today),
        'Pessoas': Pessoas,
        'Banners': Banner.objects.all()

    }
    return HttpResponse(template.render(context, request))

def get_eventos(request, data):
    data1 = datetime.datetime.strptime(data, '%d-%m-%Y')
    eventos = Evento.objects.filter(data=data1)
    eventos_json = []
    for evento in eventos:
        eventos_json.append({
            'titulo': evento.titulo,
            'local': evento.local,
            'data': evento.data.strftime('%d/%m/%y')
        })
    return HttpResponse(json.dumps(eventos_json), content_type='application/json')

def get_days_with_events(request, month_year):
    print(month_year)
    month, year = month_year.split('-')
    month = int(month)
    year = int(year)
    eventos = Evento.objects.filter(data__month=month, data__year=year)
    dias = []
    for evento in eventos:
        dias.append(evento.data.day)
    return HttpResponse(json.dumps(dias), content_type='application/json')

