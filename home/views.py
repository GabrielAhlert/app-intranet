from django.shortcuts import render
import datetime
from recados.models import Recado, ImagemRecado
from agenda.models import Contato
from django.http import HttpResponse
from django.template import loader
from .models import Banner, Evento
from agenda.models import Contato
import json


# Create your views here.
def index(request):
    template = loader.get_template('home.html')
    today = datetime.datetime.now()
    seven_days_ago = today - datetime.timedelta(days=7)

    # Aniversariantes do Mês
    # pessoas = Contato.objects.filter(nascimento__month=today.month, pessoa_ativo=True).order_by('nascimento__day')
    
    # Próximos Aniversariantes
    pessoas = Contato.objects.filter(nascimento__day__gt=today.day, pessoa_ativo=True).order_by('nascimento__day')[:20]

    proxAniversariantes = Contato.objects.filter(nascimento__day__gt=today.day, nascimento__month=today.month, pessoa_ativo=True).order_by('nascimento__day')[:4]
    AniversariantesData = Contato.objects.filter(nascimento__day=today.day, nascimento__month=today.month)

    if (AniversariantesData.count() > 0):
        titleAniversariante = "Aniversariantes"
        Aniversariantes = [AniversariantesData[x:x+4] for x in range(0, len(AniversariantesData), 4)]
    else:
        titleAniversariante = "Próximos Aniversariantes"
        Aniversariantes = [proxAniversariantes[x:x+4] for x in range(0, len(proxAniversariantes), 4)]

    Contatosadmitidos = Contato.objects.filter(admissao__gte=seven_days_ago, admissao__lte=today)
    admitidos = [Contatosadmitidos[x:x+4] for x in range(0, len(Contatosadmitidos), 4)]
    RecadosData = Recado.objects.filter(ativo=True, data_inicio__lte=today, data_fim__gte=today)
    Recados = [RecadosData[x:x+4] for x in range(0, len(RecadosData), 4)]
    context = {
        'Recados': Recados,
        'Aniversariantes_Mes': pessoas,
        'Aniversariantes': [titleAniversariante, Aniversariantes],
        'Admitidos': admitidos,
        'Banners': Banner.objects.all().order_by('id'),
    }
    
    return HttpResponse(template.render(context, request))

def get_recado(request, id_recado):
    recadoData = []
    imageData = []
    recados = Recado.objects.filter(id=id_recado)
    imagemRecado = ImagemRecado.objects.filter(recado_id=id_recado)    

    for image in imagemRecado:
        imageData.append({
            'image_url': image.image.url
        })

    for recado in recados:
        recadoData.append({
            "id": recado.id,
            "titulo": recado.titulo,
            "texto": recado.texto,
            "image": imageData
        })

    return HttpResponse(json.dumps(recadoData), content_type='application/json')

def get_eventos(request, data):
    data1 = datetime.datetime.strptime(data, '%d-%m-%Y')
    eventos = Evento.objects.filter(data=data1)
    eventos_json = []
    for evento in eventos:
        eventos_json.append({
            'titulo': evento.titulo,
            'local': evento.local,
        })
    return HttpResponse(json.dumps(eventos_json), content_type='application/json')

def get_days_with_events(request, month_year):
    print(month_year)
    month, year = month_year.split('-')
    month = int(month)
    year = int(year)
    eventos = Evento.objects.filter(data__month=month, data__year=year)
    # contato = Contato.objects.filter(nascimento__month=month)
    dias = []
    for evento in eventos:
        if evento.data.day not in dias:
            dias.append(evento.data.day)
    # for pessoa in contato:
    #     if pessoa.nascimento.day not in dias:
    #         dias.append(pessoa.nascimento.day)
    return HttpResponse(json.dumps(dias), content_type='application/json')

def get_eventos_mes(request, month_year):
    month, year = month_year.split('-')
    month = int(month)
    year = int(year)
    eventos = Evento.objects.filter(data__month=month, data__year=year)
    # aniversariantes = Contato.objects.filter(nascimento__month=month)
    eventos_json = []
    for evento in eventos:
        eventos_json.append({
            'titulo': evento.titulo,
            'local': evento.local,
            'data': evento.data.strftime('%d'),
        })
    # for aniversariante in aniversariantes:
    #     eventos_json.append({
    #         'titulo': 'Aniversário de ' + aniversariante.nome,
    #         'local': str(aniversariante.unidade.nome),
    #         'data': aniversariante.nascimento.strftime('%d'),
    #     })
    return HttpResponse(json.dumps(eventos_json), content_type='application/json')
