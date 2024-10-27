from django.db import models


class Agenda(models.Model):
    user = models.OneToOneField('Usuario.Colaborador', on_delete=models.CASCADE, related_name='agenda_associada')
    

