from Usuario.models import Usuario
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


# Create your views here.


class RegistroForm(UserCreationForm):
    nome = forms.CharField(required=True)
    sobrenome = forms.CharField(required=True)
    email = forms.CharField(required=True)
    cpf = forms.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ('nome', 'sobrenome', 'email',
                  'telefone', 'cpf', 'cargo')


def registroView(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})
