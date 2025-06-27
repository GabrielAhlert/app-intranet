from agenda.models import Contato
from documentos.models import Documento
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import json
from django.conf import settings
from pathlib import Path

def get_quicksearch(request, data):
    response = {
        'contatos': [],
        'documentos': []
    }

    # Quebrar a busca em palavras separadas
    search_words = data.split()

    # Criar um filtro dinâmico para que todas as palavras estejam contidas no nome, ramal etc.
    contatos_filter = Q(pessoa_ativo=True)
    for word in search_words:
        contatos_filter &= (
            Q(nome__icontains=word) |
            Q(ramal__icontains=word) |
            Q(telefone__icontains=word) |
            Q(email__icontains=word) |
            Q(funcao__nome__icontains=word) |
            Q(unidade__nome__icontains=word)
        )

    contatos = Contato.objects.filter(contatos_filter)   

    documentos_filter = Q()
    for word in search_words:
        documentos_filter &= Q(nome__icontains=word)

    documentos = Documento.objects.filter(documentos_filter)

    # Construção da resposta
    for contato in contatos:   
        response['contatos'].append({
            'id': contato.id,
            'nome': contato.nome,
            'ramal': contato.ramal,
            'email': contato.email,
            'telefone': contato.telefone if contato.telefone and contato.telefone != "-" else None,
            'funcao': contato.funcao.nome if contato.funcao else None,
            'unidade': contato.unidade.nome if contato.unidade else None
        })
    
    for documento in documentos:
        p = documento.categoria        
        top_parent = p

        while p:
            top_parent = p
            p = p.parente 

        response['documentos'].append({
            'id': documento.id,
            'nome': documento.nome,
            'categoria': top_parent.nome,
        })

    return HttpResponse(json.dumps(response), content_type='application/json')


def load_ies():
    json_path = Path(settings.BASE_DIR) / 'data' / 'ies.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def ie_check(request, data):
    ies = load_ies()
    required_nfe = data in ies

    response = {
        "ie": data,
        "requiredNfe": required_nfe
    }

    return JsonResponse(response)

