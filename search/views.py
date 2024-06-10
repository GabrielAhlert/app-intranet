from agenda.models import Contato
from documentos.models import Documento, Categoria
from django.http import HttpResponse
import json

# Create your views here.
def get_quicksearch(request, data):
    contatos = Contato.objects.filter(pessoa_ativo=True)
    categorias = Categoria.objects.filter()
    documentos = Documento.objects.filter()
    return HttpResponse(documentos)