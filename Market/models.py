from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import datetime

class Developer(AbstractUser):
    groups = models.ManyToManyField(Group, related_name= 'developer', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='developer_permission', blank=True)
    aprovado = models.BooleanField(default=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    telefone = models.CharField(max_length=11)
    is_developer = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)
        
        
    
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
    


