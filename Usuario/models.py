from django.db import models
from django.contrib.auth.models import AbstractUser
from Organização.models import Empresa, Setor, Cargo
from django.core.exceptions import ValidationError
from validate_docbr import CPF
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
    matricula = models.CharField(max_length=20, unique=True)
    data_demissao = models.DateField(blank=True, null=True)

    # Dados de acesso
    is_active = models.BooleanField(default=1)

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
        
