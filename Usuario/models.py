from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class Colaborador(AbstractUser):
    # Dados pessoais
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    # Dados profissionais
    setor = models.CharField(max_length=50)
    cargo = models.CharField(max_length=20)
    matricula = models.CharField(max_length=20, unique=True)
    data_entrada = models.DateField(default=timezone.now)
    data_demissao = models.DateField(blank=True, null=True)

    # Dados de acesso
    is_active = models.BooleanField(default=True)
    ultimo_login = models.DateTimeField(blank=True, null=True)


class CustomFormLoginColaborador(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-lg", 'placeholder':"Digite seu nome de usuário"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Digite sua senha'}))

    class Meta:
            model = AbstractUser
            fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == "admin":
            raise ValidationError("Este nome de usuário não é permitido!")
        return username
    



