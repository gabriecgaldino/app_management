from django.db import models
from django.forms import ModelForm
from django import forms

class Estoque(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

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
    unidade_medida = models.CharField(max_length=5, choices=UNIDADES_MEDIDA, blank=False, null=False)
    quantidade = models.DecimalField(max_digits=10, decimal_places=1)  # Ajustado para ser Decimal
    estoque = models.ForeignKey('Estoque', on_delete=models.CASCADE, related_name='produtos')  # Referência correta

    def __str__(self):
        return self.descricao

class CriaProduto(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'valor', 'unidade_medida', 'quantidade', 'estoque']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),  # Usar NumberInput para valores monetários
            'unidade_medida': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),  # Melhor utilizar NumberInput
            'estoque': forms.Select(attrs={'class': 'form-control'}),
        }