from .models import Categoria

def categorias(request):
    return {
        'categorias': Categoria.objects.filter(categoria_ativa=True)
    }