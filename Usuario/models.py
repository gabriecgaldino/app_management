from django.db import models
from django.contrib.auth.models import AbstractUser
from Organização.models import Empresa

class Endereco(models.Model):
    rua = models.CharField(max_length=100, blank=False)
    bairro = models.CharField(max_length=100, blank=False)
    cidade = models.CharField(max_length=100, blank=False)
    estado = models.CharField(max_length=100, blank=False)
    pais = models.CharField(max_length=100, blank=False)
    cep = models.CharField(max_length=9, blank=False)
    numero = models.CharField(max_length=10)
    
class Colaborador(AbstractUser):
    # Dados pessoais
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    # Dados profissionais
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, blank=True, null=True, related_name='colaboradores')
    setor = models.CharField(max_length=50, blank=True)
    cargo = models.CharField(max_length=20, blank=True)
    matricula = models.CharField(max_length=20, unique=True)
    data_demissao = models.DateField(blank=True, null=True)


    # Dados de acesso
    is_active = models.BooleanField(default=1)

    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs): 
        self.is_active = 1
        if not self.username:
            self.username = self.cpf
        if not self.password:
            self.password1 = self.set_password(self.cpf[:8])
            self.password2 = self.set_password(self.cpf[:8])

        user = kwargs.pop('user', None)

        if user:
            self.fields['empresa'].queryset = Empresa.objects.filter(gestor=user)
        super().save(*args, **kwargs)


        






