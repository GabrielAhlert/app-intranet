from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Categoria, Documento
#from .models import Contato


# def get_children(parent):
#     children = Categoria.objects.filter(parente=parent).values()
#     for child in children:
#         c = get_children(child['id'])
#         if c:
#             child['children'] = c
#         d = get_documents(child['id'])
#         if d:
#             child['documentos'] =  d
#     return children
            
def get_document(categorys):
    documents = Documento.objects.filter(categoria__in=categorys).values()
    for document in documents:
        if document['arquivo'].endswith('.pdf'):
            document['icon'] = "fa-file-pdf"
        elif document['arquivo'].endswith('.doc') or document['arquivo'].endswith('.docx'):
            document['icon'] = "fa-file-word"
        elif document['arquivo'].endswith('.xls') or document['arquivo'].endswith('.xlsx'):
            document['icon'] = "fa-file-excel"
        elif document['arquivo'].endswith('.ppt') or document['arquivo'].endswith('.pptx'):
            document['icon'] = "fa-file-powerpoint"
        elif document['arquivo'].endswith('.zip') or document['arquivo'].endswith('.rar'):
            document['icon'] = "fa-file-archive"
        else:
            document['icon'] = "fa-file"
    return documents


def index(request):
    C1 = Categoria.objects.filter(parente=None)
    C2 = Categoria.objects.filter(parente__in=C1)
    C3 = Categoria.objects.filter(parente__in=C2)
    C4 = Categoria.objects.filter(parente__in=C3)
    
    D2 = get_document(C1)
    D3 = get_document(C2)
    D4 = get_document(C3)
    D5 = get_document(C4)
    
    print(C1)
    print(C2)
    print(C3)
    print(C4)

    
    template = loader.get_template('documentos.html')
    context = {
        'C1': C1,
        'C2': C2,
        'C3': C3,
        'C4': C4,
        'D2': D2,
        'D3': D3,
        'D4': D4,
        'D5': D5,
    }
    return HttpResponse(template.render(context, request))


def download(request, id):
    documento = Documento.objects.get(id=id)
    filename = documento.arquivo.name.split('/')[-1]
    if filename.endswith('.pdf'):
        response = HttpResponse(documento.arquivo, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={filename}'
    else:
        response = HttpResponse(documento.arquivo, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename={filename}'
        
    
    return response
