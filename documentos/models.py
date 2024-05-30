from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        else:
            return self.name