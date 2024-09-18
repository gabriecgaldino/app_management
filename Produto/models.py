from django.db import models

# Create your models here.


class Produto(models.Model):
    descricao = models.CharField()
    valor = models.DecimalField(decimal_places=2)
    unidade_medida = models.CharField()
