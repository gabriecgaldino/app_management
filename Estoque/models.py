from django.db import models
from Organizações.models import Organizações

class Estoque(models.Model):
    nome = models.CharField(max_length=100)
    organizacao = models.ForeignKey(Organizações, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome




    
