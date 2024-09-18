from django.db import models

# Create your models here.


class Organizações(models.Model):
    nome_fantasia = models.CharField()
    cnpj = models.CharField()
    email = models.CharField()
