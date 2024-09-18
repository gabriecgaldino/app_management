from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from Organizações.models import Organizações

# Create your models here.


class Usuario(AbstractBaseUser, models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    cargo = models.CharField(max_length=100)
    organização = models.ForeignKey(Organizações, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
