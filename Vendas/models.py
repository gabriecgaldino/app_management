from django.db import models
from Produto.models import Produto
from Organizações.models import Organizações
from django.utils import timezone
from django import forms

class Vendas(models.Model):
    produto = models.ManyToManyField(Produto)
    valor_total = models.DecimalField(u'valor_total', decimal_places=2, max_digits=100000000)
    data_venda = models.DateField(u'data_venda', default=timezone.now())
    cliente = models.ForeignKey(Organizações, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id}"


class CriarPedido(forms.ModelForm):
    class Meta: 
        model = Vendas
        fields = ['produto', 'valor_total', 'data_venda', 'cliente']
