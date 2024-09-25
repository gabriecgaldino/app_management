from django.db import models
from Produto.models import Produto
# Create your models here.


class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(decimal_places=1, max_digits=10)
    data_entrada = models.DateField()
    data_saida = models.DateField()
