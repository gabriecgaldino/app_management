from django.db import models
from Produto.models import Produto
from Organizações.models import Organizações
# Create your models here.


class Vendas(models.Model):
    produto = models.ManyToManyField(Produto, on_delete=models.PROTECT)
    quantidade = models.DecimalField(decimal_places=1)
    valor_total = models.DecimalField(decimal_places=2)
    data_venda = models.DateField()
    cliente = models.ForeignKey(Organizações, on_delete=models.PROTECT)
