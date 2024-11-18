from django.db import models
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image as PILImage
from unidecode import unidecode
from .assinatura import Assinatura
import os
import logging
from decouple import config

PATH = config('ASSINATURAS_PATH')

class Unidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Funcao(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Função"
        verbose_name_plural = "Funções"

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=128)
    ramal = models.CharField(max_length=16, blank=True)
    telefone = models.CharField(max_length=16, default='-')
    email = models.CharField(max_length=100, default='-')
    funcao = models.ForeignKey(
        Funcao, on_delete=models.RESTRICT, blank=True, null=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.RESTRICT)
    admissao = models.DateField(blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    ramal_ativo = models.BooleanField(default=True)
    pessoa_ativo = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='fotos_funcionarios/', blank=True, null=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/home/placeholder.jpg'

    def save(self, *args, **kwargs):
        if self.email and self.email != '-':
            logger = logging.getLogger(__name__)
            template_image_path = './agenda/media_assinatura/template.png'
            template_image = PILImage.open(template_image_path)

            assinatura = Assinatura(
                template_image,
                self.nome,
                self.funcao.nome,
                self.ramal,
                self.unidade.nome,
                self.email,
                self.telefone
            )
            
            name_parts = unidecode(self.nome).lower().split() 
             
            if len(name_parts) == 1:
                file_name = f"{name_parts[0]}.png"
            else:
                file_name = f"{name_parts[0]}_{name_parts[-1]}.png"               
                
            try:                
                if os.path.exists(PATH):
                    assinatura.save_file(f"{PATH}{file_name}")
                    logger.info("Arquivo salvo com sucesso")
                else:
                    logger.error("Caminho da rede não encontrado")
            except Exception as e:
                logger.error(f"Erro ao salvar o arquivo: {e}")    

        super(Contato, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.nome} | {self.ramal} | {self.telefone} | {self.email} | {self.unidade.nome}'
