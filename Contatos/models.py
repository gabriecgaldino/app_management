from django.db import models
from Usuario.models import Colaborador

class Contatos(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='contatos')
    nome = models.CharField(max_length=50)
    is_Customer = models.BooleanField(default=False)
    is_Partner = models.BooleanField(default=False)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome
    

