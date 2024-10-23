from django.db import models
from Produto.models import Produto
from Organizações.models import Organizações
from django.utils import timezone


class Vendas(models.Model):
    produto = models.ManyToManyField(Produto)
    quantidade = models.DecimalField(decimal_places=1, max_digits=100000000)
    valor_total = models.DecimalField(decimal_places=2, max_digits=100000000)
    data_venda = models.DateField(default=timezone.now())
    cliente = models.ForeignKey(Organizações, on_delete=models.PROTECT)
