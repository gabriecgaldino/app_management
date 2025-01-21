from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from datetime import datetime

import csv
import logging

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


fields = ['first_name', 'last_name', 'is_staff', 'date_joined', 'cpf', 
          'email', 'telefone', 'data_nascimento', 'cargo_id', 'matricula', 
          'is_active', 'empresa_id', 'setor_id']

logger = logging.getLogger(__name__)

def importar_funcionarios(request):
    if request.method == 'POST' and request.FILES.get('csvFile'):
        csv_file = request.FILES['csvFile']

        if not csv_file.name.endswith('.csv'):
            return JsonResponse({'error': 'O formato do arquivo é inválido.'}, status=400)

        errors = []

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file, delimiter=';')
            reader.fieldnames = [field.lstrip('\ufeff') for field in reader.fieldnames]

            with transaction.atomic():
                for i, row in enumerate(reader, start=1):
                    try:
                        # Verificar unicidade do e-mail
                        email = row['email'].strip()
                        if Colaborador.objects.filter(email=email).exists():
                            errors.append(f"Linha {i}: O e-mail '{email}' já está cadastrado.")
                            continue

                        # Verificar e converter datas
                        data_nascimento_str = row.get('data_nascimento', '').strip()
                        if not data_nascimento_str:
                            errors.append(f"Linha {i}: O campo 'data_nascimento' está vazio.")
                            continue

                        try:
                            data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
                        except ValueError:
                            errors.append(f"Linha {i}: A data '{data_nascimento_str}' não está no formato DD/MM/AAAA.")
                            continue

                        date_joined_str = row.get('date_joined', '').strip()
                        if not date_joined_str:
                            errors.append(f"Linha {i}: O campo 'date_joined' está vazio.")
                            continue

                        try:
                            date_joined = datetime.strptime(date_joined_str, '%d/%m/%Y')
                        except ValueError:
                            errors.append(f"Linha {i}: A data '{date_joined_str}' não está no formato DD/MM/AAAA.")
                            continue

                        # Criar e salvar o colaborador
                        colaborador = Colaborador(
                            first_name=row['first_name'].strip(),
                            last_name=row['last_name'].strip(),
                            is_staff=row['is_staff'].strip().lower() == 'true',
                            date_joined=date_joined,
                            cpf=row['cpf'].strip(),
                            email=email,
                            telefone=row['telefone'].strip(),
                            data_nascimento=data_nascimento,
                            cargo_id=int(row['cargo_id']),
                            is_active=row['is_active'].strip().lower() == 'true',
                            empresa_id=int(row['empresa_id']),
                            setor_id=int(row['setor_id'])
                        )
                        colaborador.save()

                    except Exception as e:
                        errors.append(f"Linha {i}: {e}")
                        logger.error(f"Erro ao processar linha {i}: {e}")


            if errors:
                return JsonResponse({'errors': errors}, status=400)

            return JsonResponse({'message': 'Importação concluída com sucesso!'})
        except Exception as e:
            logger.error(f"Erro ao processar o arquivo: {e}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Requisição inválida'}, status=400)