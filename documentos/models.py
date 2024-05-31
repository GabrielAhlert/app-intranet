from django.db import models
from django.forms import ValidationError

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    parente = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    categoria_ativa = models.BooleanField(default=True)
    
    def __str__(self):
        if self.parente:
            return f'{self.parente} -> {self.nome}'
        else:
            return self.nome
        
        
    
    def save(self, *args, **kwargs):
        if self.parente:
            if self.parente.parente:
                if self.parente.parente.parente:
                    raise ValidationError('Categoria não pode ter mais de 3 níveis de profundidade')
        super(Categoria, self).save(*args, **kwargs)