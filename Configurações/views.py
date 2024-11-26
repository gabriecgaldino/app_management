from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Organização.views import cria_empresa_view, cria_setor
from Organização.forms import EmpresaForm, SetorForm
from Usuario.forms import ColaboradorForm
from Usuario.views import cria_colaborador_view

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
    if request.method == 'POST':
        form_colaborador = cria_colaborador_view(request.POST)
        return render(request, 'colaboradores.html', {'form_colaborador': form_colaborador})
    else: 
        form_colaborador = ColaboradorForm()
    return render(request, 'colaboradores.html', {'form_colaborador': form_colaborador})
