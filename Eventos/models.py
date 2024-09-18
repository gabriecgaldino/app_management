from django.db import models
from Usuario.models import Usuario

# Create your models here.


class Eventos(models.Model):
    descricao = models.CharField()
    data_evento = models.DateField()
    hora_evento = models.TimeField()
    convidados = models.ManyToManyField(Usuario, on_delete=models.PROTECT)
    status = models.BooleanField(default=True)
