from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser


class Colaborador(AbstractUser):
    # Dados pessoais
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    # Dados profissionais
    setor = models.CharField(max_length=50, blank=True)
    cargo = models.CharField(max_length=20, blank=True)
    matricula = models.CharField(max_length=20, unique=True)
    data_demissao = models.DateField(blank=True, null=True)


    # Dados de acesso
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs): 
        if not self.username:
            self.username = self.cpf
        if not self.password:
            self.password1 = self.set_password(self.cpf[:8])
            self.password2 = self.set_password(self.cpf[:8])
            
            
        super().save(*args, **kwargs)



