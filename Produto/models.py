from django.db import models
from django.forms import ModelForm


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_medida = models.CharField(max_length=5)
    quantidade = models.CharField(max_length=100000)

    def __unicode__(self):
        return self.descricao


class CriaProduto(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'valor', 'unidade_medida']
