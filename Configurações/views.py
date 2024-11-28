from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from Organização.views import cria_empresa_view, cria_setor
from Organização.forms import EmpresaForm, SetorForm
from Usuario.forms import ColaboradorForm, EnderecoForm

@login_required
def configuracoes_view(request):
    if request.method == 'POST':
        form = cria_empresa_view(request.POST)
        form_setor = cria_setor(request.POST)

        return render(request, 'configurações.html', {
            'form': form,
            'form_setor': form_setor

        })

    else:
        form = EmpresaForm()
        form_setor = SetorForm()

        return render(request, 'configurações.html', {'form': form})

@login_required
def perfil_view(request):
    return render(request, 'perfil.html')

@login_required
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


@login_required
def colaboradores_view(request):
    if request.method == 'POST':
        form_colaborador = ColaboradorForm(request.POST)
        form_endereco = EnderecoForm(request.POST)

        if form_colaborador.is_valid() and form_endereco.is_valid():
            with transaction.atomic():
                endereco = form_endereco.save()
                colaborador = form_colaborador.save(commit=False)
                colaborador.endereco = endereco

                colaborador.save()
            return redirect('colaboradores')
    else: 
        form_colaborador = ColaboradorForm()
        form_endereco = EnderecoForm()
    return render(request, 'colaboradores.html', {
        'form_colaborador': form_colaborador,
        'form_endereco': form_endereco
        })