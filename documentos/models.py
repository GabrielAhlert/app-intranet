from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    parente = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    categoria_ativa = models.BooleanField(default=True)
    profundidade = models.IntegerField(default=0)
    
    def __str__(self):
        if self.parente:
            return f'{self.parente} -> {self.nome}'
        else:
            return self.nome
    
    def save(self, *args, **kwargs):
        if self.parente:
            self.produndidade = self.parente.profundidade + 1
        if self.produndidade > 2:
            raise Exception('Categoria não pode ter mais que 2 níveis de profundidade')
        super(Categoria, self).save(*args, **kwargs)