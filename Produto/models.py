from django.db import models
from django.forms import ModelForm
from django import forms
from Estoque.models import Estoque
from datetime import date


class Produto(models.Model):
    UNIDADES_MEDIDA = [
        ('KG', 'Kilograma'),
        ('UN', 'Unidade'),
        ('LT', 'Litro'),
        ('CX', 'Caixa'),
        ('MT', 'Metro'),
    ]

    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_medida = models.CharField(
        max_length=5, choices=UNIDADES_MEDIDA, blank=False, null=False)
    quantidade = models.DecimalField(max_digits=10, decimal_places=1)
    estoque_id = models.ForeignKey(
        Estoque, on_delete=models.CASCADE, related_name='produtos')
    data_joined = models.DateField(
        max_length=date.today(), default=date.today())

    def __str__(self):
        return self.descricao


class CriaProduto(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'valor',
                  'unidade_medida', 'quantidade', 'estoque_id']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidade_medida': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'estoque_id': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        organizacao = kwargs.pop('organizacao', None)
        super().__init__(*args, **kwargs)
        if organizacao:
            self.fields['estoque_id'].queryset = Estoque.objects.filter(
                organizacao=organizacao)
        else:
            self.fields['estoque_id'].queryset = Estoque.objects.none()
