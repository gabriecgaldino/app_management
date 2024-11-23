from django.shortcuts import render, redirect
from django.contrib import messages
from Organização.forms import EmpresaForm
from Organização.models import Empresa


def configuracoes_view(request):
        if request.method == 'POST': 
            form = EmpresaForm(request.POST)
            if form.is_valid():
                Empresa(form).save()
                return redirect('configurações')
        else:
             form = EmpresaForm()
        return render(request, 'configurações.html', {'form':form})


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
