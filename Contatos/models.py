from django.db import models
from Agenda.models import Agenda


class Contatos(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    is_Customer = models.BooleanField(default=False)
    is_Partner = models.BooleanField(default=False)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome
    

