from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from validate_docbr import CPF

from Organização.models import Empresa, Setor, Cargo
import re


class Endereco(models.Model):
    rua = models.CharField(max_length=100, blank=False)
    bairro = models.CharField(max_length=100, blank=False)
    cidade = models.CharField(max_length=100, blank=False)
    estado = models.CharField(max_length=100, blank=False)
    pais = models.CharField(max_length=100, blank=False)
    cep = models.CharField(max_length=9, blank=False)
    numero = models.CharField(max_length=10)


class Colaborador(AbstractUser):
    def validar_cpf(value):
        cpf = CPF()
        if not cpf.validate(value):
            raise ValidationError('CPF inválido.')
        
    # Dados pessoais
    colaborador_groups = models.ManyToManyField(Group, related_name='colaborador', blank=True)
    colaborador_permissions = models.ManyToManyField(Permission, related_name='colaborador_permission', blank=True)
    cpf = models.CharField(max_length=14, unique=True, validators=[validar_cpf])
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.PROTECT, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    # Dados profissionais
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, blank=True, null=True, related_name='colaboradores')
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT,
                              blank=True, null=True, related_name='cargo')
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT,
                              blank=True, null=True, related_name='cargo')
    matricula = models.CharField(max_length=20, unique=True, blank=True, null=True)
    data_demissao = models.DateField(blank=True, null=True)

    # Dados de acesso
    is_active = models.BooleanField(default=1)
    is_developer = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        self.is_active = 1
        self.cpf = re.sub(r'\D', '', self.cpf)
        if not self.username:
            self.username = self.cpf

        if not self.password:
            self.password1 = self.set_password(self.cpf[:8])
            self.password2 = self.set_password(self.cpf[:8])

        if not self.matricula:
            prefixo = self.empresa.nome_fantasia[:2].upper()
            numero = str(Colaborador.objects.filter(
                empresa=self.empresa).count() + 1).zfill(5)
            self.matricula = f'{prefixo}{numero}'
            
        

        super().save(*args, **kwargs)
        
        
class Developer(Colaborador):
    is_developer_approved = models.BooleanField(default=False)
    dev_groups = models.ManyToManyField(Group, related_name='developer', blank=True)
    dev_permissions = models.ManyToManyField(Permission, related_name='developer_permission', blank=True)
    
    def save(self, *args, **kwargs):
        self.is_active = 1
        self.cpf = re.sub(r'\D', '', self.cpf)
        self.username = self.email
        self.is_developer = True
        
        if self.is_developer:
            self.empresa = get_object_or_404(Empresa, id=2)
        
        if not self.password:
            self.password1 = self.set_password(self.cpf[:8])
            self.password2 = self.set_password(self.cpf[:8])
            
        super().save(*args, **kwargs)
