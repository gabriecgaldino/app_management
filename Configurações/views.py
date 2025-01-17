from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse, JsonResponse


import csv
import logging
import datetime

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

def baixar_template(request):
    # Criação de um CSV para download
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="template.csv"'

    writer = csv.writer(response)
    writer.writerow(['id',"password","last_login","is_superuser","username","first_name","last_name","is_staff","date_joined","cpf","email","telefone","endereco_id","data_nascimento","cargo_id","matricula","data_demissao","is_active","empresa_id","setor_id"])

    return response


logger = logging.getLogger(__name__)

fields = ['first_name', 'last_name', 'is_staff', 'date_joined', 'cpf', 
          'email', 'telefone', 'data_nascimento', 'cargo_id', 'matricula', 
          'is_active', 'empresa_id', 'setor_id']

def importar_funcionarios(request):
    if request.method == 'POST' and request.FILES['csvFile']:
        csv_file = request.FILES['csvFile']
        
        # Verificação se o arquivo é um CSV
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'O arquivo deve ser um CSV.')
            return JsonResponse({'error': 'O formato do arquivo é inválido.'})

        # Processar o CSV
        errors = []
    
        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file, delimiter=';')
            
            # Verifica se as colunas do CSV correspondem às esperadas
            if reader.fieldnames != fields:
                errors.append('Campos inválidos! Colunas esperadas: ' + ', '.join(fields))
            
            for i, row in enumerate(reader, start=1):
                if not row.get('first_name'):
                    print(row.get('first_name'))
                    errors.append(f"Linha {i}: O campo 'nome', está vazio.")
                if not row.get('last_name'):
                    errors.append(f"Linha {i}: O campo 'sobrenome', está vazio. ")
                if not row.get('is_staff'):
                    errors.append(f"Linha {i}: O campo 'is_staff', está vazio. ")
                if not row.get('data_joined'):
                    errors.append(f"Linha {i}: O campo 'data_joined', está vazio.")
                if not row.get('cpf'):
                    errors.append(f"Linha {i}: O campo 'cpf', está vazio. ")
                if not row.get('email'):
                    errors.append(f"Linha {i}: O campo 'email', está vazio. ")
                if '@' not in row.get('email', ''):
                    errors.append(f"Linha {i}: Forneça um e-mail válido para o campo 'email'. ")
                if not row.get('telefone'):
                    errors.append(f"Linha {i}: O campo 'telefone', está vazio. ")
                if not row.get('data_nascimento'):
                    errors.append(f"Linha {i}: O campo 'data_nascimento', está vazio. ")
                try:
                    idade = int(row.get('data_nascimento', ''))
                    if idade <= 0:
                        errors.append(f"Linha {i}: O campo 'data_nascimento' deve ser maior que 0. ")
                except ValueError:
                    errors.append(f"Linha {i}: Idade {row.get('data_nascimento', '')}, não é um número válido")
                if not row.get('cargo_id'):
                    errors.append(f"Linha {i}: O campo 'cargo_id', está vazio. ")
                if not row.get('matricula'):
                    errors.append(f"Linha {i}: O campo 'matricula', está vazio. ")
                if not row.get('is_active'):
                    errors.append(f"Linha {i}: O campo 'is_active', está vazio. ")
                if not row.get('empresa_id'):
                    errors.append(f"Linha {i}: O campo 'empresa_id', está vazio. ")
                if not row.get('setor_id'):
                    errors.append(f"Linha {i}: O campo 'setor_id', está vazio. ")
        except ValueError:
            errors.append('Erro ao abrir o arquivo enviado, tente novamente!')

        if errors:
            logger.error("Erros encontrados durante a importação: %s", errors)
            messages.error(request, f'Houve erros ao processar o arquivo: {", ".join(errors)}')
            return JsonResponse({'errors': errors}, status=400)

        return JsonResponse({'message': 'Importação concluída com sucesso!'})

    return JsonResponse({'error': 'Requisição inválida'}, status=400)