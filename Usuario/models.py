from django.db import models
from django.contrib.auth.models import User
from Organizações.models import Organizações
from Agenda.models import Agenda

from django.contrib.auth.forms import UserCreationForm


class Colaborador(User):
    telefone = models.CharField(u'Telefone', max_length=11)
    cpf = models.CharField(u'CPF', max_length=11)
    cargo = models.CharField(u'Cargo', max_length=100)
    organizacao = models.ForeignKey(Organizações, on_delete=models.CASCADE)
    USERNAME_FIELD = 'email'
    

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)
        Agenda.objects.create(user=self)


    def __unicode__(self):
        return self.first_name


class CriaColaborador(UserCreationForm):
    class Meta:
        model = Colaborador
        fields = ['first_name', 'last_name', 'email',
                  'cpf', 'telefone', 'organizacao', 'password1', 'password2']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.username = user.email
            if commit:
                user.save()
            return user
