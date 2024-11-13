from django.db import models
from django.utils import timezone

class Vendas(models.Model):
    numero_pedido = models.OneToOneField('Pedidos.Pedidos', on_delete=models.PROTECT)
    cliente = models.ForeignKey('Contatos.Contatos', on_delete=models.PROTECT)
    data_venda = models.DateField(default=timezone.now())
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    status = models.CharField(max_length=50, choices=[('Pendente',  'Pendente'), ('Pago', 'Pago'), ('Cancelado', 'Cancelado')])

    def __str__(self):
        return f'Venda #{self.id} - {self.cliente}'
    
    def calcular_total(self):
        total = self.pedido.calcular_total() if self.pedido else 0
        self.valor_total = total

        return total
    
    def save(self, *args, **kwargs):
        self.calcular_total()
        super().save(**args, **kwargs)