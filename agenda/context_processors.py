from .models import Contato

def contatos(request):
    return {
        'Contatos': Contato.objects.filter(ramal_ativo=True).order_by('ramal')
    }