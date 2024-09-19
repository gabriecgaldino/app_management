from django.shortcuts import render, redirect
from Usuario.models import Colaborador, CriaColaborador
from django.contrib import messages


def registro(request):
    if request.method == 'POST':
        form = CriaColaborador(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Usuário criado com sucesso, realize o login!')

    else:
        form = CriaColaborador()

    return render(request, 'registro.html', {'form': form})
