from django.db import models
from django import template
from datetime import datetime
from Usuario.models import Developer

register = template.Library()
 
class App(models.Model):
    nome = models.CharField(max_length=20, unique=True, blank=False)
    descricao = models.CharField(max_length=200, blank=True)
    versao = models.CharField(max_length=20, blank=False)
    instalado = models.BooleanField(default=False)
    dependencias = models.JSONField(default=list)
    zip_file = models.FileField(upload_to='app_pacotes/')
    autor = models.ForeignKey(Developer, on_delete=models.PROTECT, blank=False, null=False)
    publicado = models.BooleanField(default=False)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    approved_status = models.CharField(null=True, blank=True, max_length=50, editable=True)
    
    def save(self, *args, **kwargs):
        self.approved_status = 'Em análise'
    
        super().save(*args, **kwargs)


    
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
    


