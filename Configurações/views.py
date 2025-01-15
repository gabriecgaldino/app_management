from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from Organização.views import cria_empresa_view, cria_setor, cria_cargo
from Organização.forms import EmpresaForm, SetorForm, CargoForm
from Usuario.forms import ColaboradorForm, EnderecoForm
from Usuario.models import Colaborador

def configuracoes_view(request):
    if request.method == 'POST':
        form = cria_empresa_view(request.POST)
        form_setor = cria_setor(request)
        form_cargo = cria_cargo(request)
    else:
        form = EmpresaForm()
        form_setor = SetorForm()
        form_cargo = CargoForm()

    return render(request, 'configurações.html', {
        'form': form,
        'form_setor': form_setor,
        'form_cargo': form_cargo,
    })

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


from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction

def colaboradores_view(request):
    matricula = request.GET.get('matricula')
    colaboradores = Colaborador.objects.filter(empresa=request.user.empresa_id)

    colaborador = None
    form_atualizar = None
    form_endereco = EnderecoForm()
    form_colaborador = ColaboradorForm()

    if matricula:
        try:
            colaborador = Colaborador.objects.get(matricula=matricula)
            form_atualizar = ColaboradorForm(instance=colaborador)
            if colaborador.endereco:
                form_endereco = EnderecoForm(instance=colaborador.endereco)
        except Colaborador.DoesNotExist:
            print(f"Colaborador com matrícula {matricula} não encontrado.")
            colaborador = None



    if request.method == 'POST':
        if 'atualizar' in request.POST and colaborador:
            # Atualização do colaborador
            print(form_atualizar)
            form_atualizar = ColaboradorForm(request.POST, instance=colaborador)
            
            
            
            form_endereco = EnderecoForm(request.POST, instance=colaborador.endereco)

            if form_atualizar.is_valid() and form_endereco.is_valid():
                with transaction.atomic():
                    endereco = form_endereco.save()
                    colaborador_atualizado = form_atualizar.save(commit=False)
                    colaborador_atualizado.endereco = endereco
                    colaborador_atualizado.save()
                print("Colaborador atualizado com sucesso.")
                return redirect('colaboradores')
            else:
                print("Erros ao atualizar colaborador:")
                print(form_atualizar.errors)
                print(form_endereco.errors)

        elif 'criar' in request.POST:
            form_colaborador = ColaboradorForm(request.POST)
            form_endereco = EnderecoForm(request.POST)

            if form_colaborador.is_valid() and form_endereco.is_valid():
                with transaction.atomic():
                    endereco = form_endereco.save()
                    novo_colaborador = form_colaborador.save(commit=False)
                    novo_colaborador.endereco = endereco
                    novo_colaborador.save()
                print("Novo colaborador criado com sucesso.")
                return redirect('colaboradores')
            else:
                print("Erros ao criar colaborador:")
                print(form_colaborador.errors)
                print(form_endereco.errors)

    return render(request, 'colaboradores.html', {
        'colaboradores': colaboradores,
        'form_colaborador': form_colaborador,
        'form_endereco': form_endereco,
        'form_atualizar': form_atualizar,
    })
