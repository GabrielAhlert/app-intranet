from django.db import models
from pkg_resources import require

# Create your models here.

class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Funcao(models.Model):
    nome = models.CharField(max_length=100)
    class Meta: 
        verbose_name = "Funcão"
        verbose_name_plural = "Funções"
    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=128)
    ramal = models.CharField(max_length=16 , blank=True)
    telefone = models.CharField(max_length=16, default='-')
    email = models.CharField(max_length=100, default='-')
    funcao = models.ForeignKey(Funcao, on_delete=models.RESTRICT, blank=True, null=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.RESTRICT)
    admissao = models.DateField(blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    ramal_ativo = models.BooleanField(default=True)
    pessoa_ativo = models.BooleanField(default=True)
    image = models.ImageField(upload_to='fotos_funcionarios/', blank=True, null=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/home/placeholder.jpg'
    
    def __str__(self):
        return self.nome +  ' | ' + self.ramal + ' | ' + self.telefone + ' | ' + self.email + ' | ' + self.unidade.nome
