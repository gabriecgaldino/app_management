from django.shortcuts import render, redirect
from django.contrib import messages


def configuracoes_view(request):
    return render(request, 'configurações.html')


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
