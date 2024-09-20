from django.shortcuts import render, redirect
from Usuario.models import Colaborador, CriaColaborador
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




def registro(request):
    if request.method == 'POST':
        form = CriaColaborador(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Usuário criado com sucesso, realize o login!')
        else: 
            messages.error(request, "Erro ao criar o usuário. Verifique os dados.")
    else:
        form = CriaColaborador()

    return render(request, 'registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'E-mail ou senha inválidos')

    return render(request, 'login.html')
