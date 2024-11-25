from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import ColaboradorForm


def login_view(request):
    if request.method == 'POST':
        form_login = AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            user = form_login.get_user()
            login(request, user)
            messages(request, f'Bem, vindo {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Credenciais inválidas!')
    else:
        form_login = AuthenticationForm()

    return render(request, 'login.html', {'form_login': form_login})
