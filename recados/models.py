from django.db import models

# Create your models here.

class Recado(models.Model):
    titulo = models.CharField(max_length=64)
    texto = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    

