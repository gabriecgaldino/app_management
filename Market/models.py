from django.db import models
from django.conf import settings
from datetime import datetime

class Developer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    nome_empresa = models.CharField(max_length=100, blank=False, null=False)
    cod_autorizacao = models.CharField(max_length=15, null=False, blank=False, unique=True)
    aprovado = models.BooleanField(default=False)
    
class App(models.Model):
    nome = models.CharField(max_length=20, unique=True, blank=False)
    descricao = models.CharField(max_length=200, blank=True)
    versão = models.CharField(max_length=20, blank=False)
    instalado = models.BooleanField(default=False)
    dependencias = models.JSONField(default=list)
    arquivo_pacote = models.FileField(upload_to='app_pacotes/')
    autor = models.ForeignKey(Developer, on_delete=models.PROTECT, blank=False, null=False)
    publicado = models.BooleanField(default=False)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    
class Market(models.Model):
    aplicativos = models.ForeignKey(
        App,
        blank=True,
        related_name='loja',
        on_delete=models.CASCADE
    )
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    data_publicacao = models.DateTimeField(default=datetime.now)
    destaque = models.BooleanField(default=False)
    


