from django.db import models

from Produto.models import Produto
from django import forms

class Pedidos(models.Model):
    data_pedido = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey('Organizações.Organizações', on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, through='PedidoProduto')

    def __str__(self):
        return f"Pedido #{self.id}"

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.pedidoproduto_set.all())

class PedidoProduto(models.Model):
    numero_pedido = models.ForeignKey(Pedidos, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_subtotal(self):
        return self.quantidade * self.preco

class NovoPedido(forms.ModelForm):
    class Meta:
        model = PedidoProduto
        fields = ['produto', 'quantidade']
        
