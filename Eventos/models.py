from django.db import models


class Eventos(models.Model):
    descricao = models.CharField(max_length=100)
    data_evento = models.DateField()
    hora_evento = models.TimeField()
    status = models.BooleanField(default=True)
