from django.db import models
from django.utils import timezone
from Produto.models import Produto

class Produtos_do_Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()

    def sub_total(self): 
        return self.produto.valor * self.quantidade

    def __str__(self):
        return f"{self.produto.descricao} - {self.quantidade}"

class Pedidos_de_Venda(models.Model):
    STATUS_PEDIDO = [
        ('Aberto', 'Aberto'),
        ('Em andamento', 'Em andamento'),
        ('Concluído', 'Concluído'),
    ]

    numero_pedido = models.CharField(max_length=10)
    status_pedido = models.CharField(
        max_length=20,
        choices=STATUS_PEDIDO,
        default='Aberto'
    )
    data_pedido = models.DateField(default=timezone.now)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    produtos = models.ManyToManyField(Produtos_do_Pedido)

    def __str__(self):
        return f"Pedido {self.numero_pedido} - {self.status_pedido}"
