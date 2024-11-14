from django.db import models
from Produto.models import Produto
from Organizações.models import Organizações  
from django import forms
from django.utils import timezone

# Modelo de Pedido
class Pedidos(models.Model):
    data_pedido = models.DateField(default=timezone.now)
    cliente = models.ForeignKey(Organizações, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, through='PedidoProduto')
    numero_pedido = models.CharField(max_length=5)

    def __str__(self):
        return f"Pedido #{self.numero_pedido}"

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.pedidoproduto_set.all())

# Modelo Intermediário PedidoProduto
class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_subtotal(self):
        return self.quantidade * self.preco

class PedidoProdutoForm(forms.ModelForm):
    data_pedido = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar Cliente...'}))
    numero_pedido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantidade = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    preco = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = PedidoProduto
        fields = ['produto', 'quantidade', 'preco']  
