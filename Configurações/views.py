from django.shortcuts import render, redirect
from django.contrib import messages
from Organização.views import cria_empresa_view
from Organização.forms import EmpresaForm


def configuracoes_view(request):
    if request.method == 'POST':
        form = cria_empresa_view(request.POST)
        return render(request, 'configurações.html', {'form': form})

    else:
        form = EmpresaForm()

        return render(request, 'configurações.html', {'form': form})


def perfil_view(request):
    return render(request, 'perfil.html')


def atualizar_perfil_view(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.colaborador.telefone = request.POST.get('telefone')
        user.save()
        user.colaborador.save()
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('perfil')


def colaboradores_view(request):
    return render(request, 'colaboradores.html')
