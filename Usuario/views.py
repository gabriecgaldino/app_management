from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ColaboradorForm, LoginForm


def login_view(request):
    if request.method == 'POST':
        form_login = LoginForm(request, data=request.POST)
        if not form_login.is_valid():
            user = form_login.get_user()
            if user:
                login(request, user)
                return redirect('index')
        else:
            messages.error(request, 'Credenciais inválidas!')
    else:
        form_login = LoginForm()

    return render(request, 'login.html', {'form_login': form_login})



def cria_colaborador_view(request):
    form_colaborador = ColaboradorForm(request)
    if form_colaborador.is_valid():
        form_colaborador.save()

    return form_colaborador
