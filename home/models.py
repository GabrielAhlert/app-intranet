from django.db import models
from django.utils import timezone

# Create your models here.

class Banner(models.Model):
    titulo = models.CharField(max_length=100, default='Banner '+str(timezone.now()))
    imagem = models.ImageField(upload_to='banner')

    def __str__(self):
        return self.titulo
    
class Evento(models.Model):
    titulo = models.CharField(max_length=100, default='Evento '+str(timezone.now()))
    local = models.CharField(max_length=100, blank=True, null=True,  default='Local '+str(timezone.now()))
    data = models.DateField(default=timezone.now)

    def __str__(self):
        return self.titulo