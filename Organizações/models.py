from django.db import models

# Create your models here.


class Organizações(models.Model):
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_fantasia
