from django.db import models

class Agricultor(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    grupo_familiar = models.ForeignKey(
        'GrupoFamiliar',
        related_name='agricultores',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.matricula} - {self.nome}"

class GrupoFamiliar(models.Model):
    proprietario = models.OneToOneField(
        Agricultor,
        related_name='grupo_proprietario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.proprietario.nome if self.proprietario else "Grupo sem proprietário"
