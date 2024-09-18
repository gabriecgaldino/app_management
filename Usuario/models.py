from django.db import models
from Organizações.models import Organizações

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField()
    sobrenome = models.CharField()
    email = models.CharField()
    senha = models.CharField()
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    cargo = models.CharField()
    organização = models.ForeignKey(Organizações, on_delete=models.CASCADE)
