from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Recado(models.Model):
    titulo = models.CharField(max_length=64, blank=True)
    # texto = models.TextField(blank=True)
    texto = RichTextField(blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo    

class ImagemRecado(models.Model):
    recado = models.ForeignKey(Recado, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/')

