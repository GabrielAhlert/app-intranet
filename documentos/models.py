from django.db import models
from django.forms import ValidationError

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    parente = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    categoria_ativa = models.BooleanField(default=True)
    icone = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        if self.parente:
            return f'{self.parente} -> {self.nome}'
        else:
            return self.nome
        
        
    
    def save(self, *args, **kwargs):
        if self.parente:
            if self.parente.parente:
                    raise ValidationError('Categoria não pode ter mais de 2 níveis de profundidade')
        super(Categoria, self).save(*args, **kwargs)
        
class Documento(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='documentos')
    link = models.URLField(blank=True)
    
    def __str__(self):
        return self.nome