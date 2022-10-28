from django.db import models
from pkg_resources import require

# Create your models here.

class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=128)
    funcao = models.CharField(max_length=64 , blank=True)
    ramal = models.CharField(max_length=16 , blank=True)
    telefone = models.CharField(max_length=16, default='-')
    email = models.CharField(max_length=100, blank=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.RESTRICT)
    nascimento = models.DateField(blank=True, null=True)
    ramal_ativo = models.BooleanField(default=True)
    pessoa_ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome + ' | ' + self.funcao + ' | ' + self.ramal + ' | ' + self.telefone + ' | ' + self.email + ' | ' + self.unidade.nome