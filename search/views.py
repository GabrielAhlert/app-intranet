from agenda.models import Contato
from documentos.models import Documento, Categoria
from django.http import HttpResponse
from django.db.models import Q
import json

# Create your views here.
def get_quicksearch(request, data):
    response = {
        'contatos': [],
        'documentos': []
    }

    contatos = Contato.objects.filter(
        pessoa_ativo=True
    ).filter(
        Q(nome__icontains=data) |
        Q(ramal__icontains=data) |
        Q(telefone__icontains=data) |
        Q(email__icontains=data) |
        Q(funcao__nome__icontains=data) |
        Q(unidade__nome__icontains=data)
    )[:5]    

    documentos = Documento.objects.filter(Q(nome__icontains=data))

    for contato in contatos:   
        contatos_dict = {
            'id': contato.id,
            'nome': contato.nome,
            'ramal': contato.ramal,
            'email': contato.email,
            'funcao': contato.funcao.nome if contato.funcao else None,
            'unidade': contato.unidade.nome if contato.unidade else None
        }

        response['contatos'].append(contatos_dict)
    
    for documento in documentos:
        documentos_dict = {
            'id': documento.id,
            'nome': documento.nome,
            'categoria': documento.categoria.nome,
        }

        response['documentos'].append(documentos_dict)

    return HttpResponse(json.dumps(response), content_type='application/json')