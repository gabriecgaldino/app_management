from django.db import models
from Produto.models import Produto
from Organizações.models import Organizações
from django.utils import timezone
from django import forms

class Vendas(models.Model):
    produto = models.ManyToManyField(Produto)
    quantidade = models.DecimalField(u'quantidade', decimal_places=1, max_digits=100000000)
    valor_total = models.DecimalField(u'valor_total', decimal_places=2, max_digits=100000000)
    data_venda = models.DateField(u'data_venda', default=timezone.now())
    cliente = models.ForeignKey(Organizações, on_delete=models.PROTECT)


class CriarPedido(forms.ModelForm):
    class Meta: 
        model = Vendas
        fields = ['produto', 'quantidade', 'valor_total', 'data_venda', 'cliente']
