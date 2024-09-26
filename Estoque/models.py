from django.db import models
from Produto.models import Produto
# Create your models here.


class Estoque(models.Model):
    nome = models.CharField(max_length=50, default='Estoque')
    
