from django.db import models


class Agenda(models.Model):
    user = models.OneToOneField('Usuario.Colaborador', on_delete=models.CASCADE, default=1)
    

