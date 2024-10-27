from django.db import models
from Agenda.models import Agenda


class Eventos(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=100)
    data_evento = models.DateField()
    hora_evento = models.TimeField()
    status = models.BooleanField(default=True)
