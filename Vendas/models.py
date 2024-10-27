from django.db import models
from Produto.models import Produto
from Organizações.models import Organizações
from django.utils.timezone import datetime
from django import forms

class Vendas(models.Model):
    produto = models.ManyToManyField(Produto)
    quantidade = models.DecimalField(decimal_places=1, max_digits=100000000)
    valor_total = models.DecimalField(decimal_places=2, max_digits=100000000)
    data_venda = models.DateField(default=datetime.now())
    cliente = models.ForeignKey(Organizações, on_delete=models.PROTECT)


class NovaVenda(forms.ModelForm):
    class Meta: 
        models = Vendas
        fields = ['produto', 'quantidade', 'valor_total', 'data_venda', 'cliente']
