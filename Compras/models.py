from django.db import models
from Organizações.models import Organizações

class Compras(models.Model):
    produto = models.ManyToManyField()
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(decimal_places=2)
    fornecedor = models.ForeignKey(Organizações, on_delete=models.PROTECT)
    data_compra = models.DateField()
