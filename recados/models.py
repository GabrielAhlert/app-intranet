from django.db import models

# Create your models here.

class Recado(models.Model):
    titulo = models.CharField(max_length=64, blank=True)
    texto = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ativo = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    

