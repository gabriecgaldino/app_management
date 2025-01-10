from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse
import logging
import json
from .forms import LoginForm


from Usuario.models import Colaborador

logger = logging.getLogger(__name__)

def login_view(request):
    form_login = LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form_login.is_valid():
            username = form_login.cleaned_data.get('username')
            password = form_login.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                logger.info(f"Usuário {username} autenticado com sucesso.")
                return redirect('index')
            else:
                logger.warning(f"Tentativa de login falhou para o usuário {username}.")
                messages.error(request, "Usuário ou senha incorretos.")
        else:
            logger.error(f"Erro no formulário de login: {form_login.errors}")
            messages.error(request, "Erro no preenchimento do formulário.")

    return render(request, 'login.html', {'form_login': form_login})


## rotas da api
def busca_colaborador_api(request):
    colaboradorId = request.GET.get('colaboradorId')
    
    if colaboradorId is not None:
        try:
            colaborador = Colaborador.objects.filter(matricula__icontains=colaboradorId).values(
                'first_name', 'last_name', 'is_active', 'is_staff', 'cpf', 'email', 'telefone', 'data_nascimento',
                'empresa__nome_fantasia', 'setor__nome_setor', 'cargo__nome_cargo',
                'endereco__cep', 'endereco__rua', 'endereco__numero',  'endereco__estado', 'endereco__cidade', 
                'endereco__bairro', 'endereco__pais', 'matricula'
                )
            return JsonResponse({'colaborador': list(colaborador)}, safe=False)
        except ValueError:
            return JsonResponse({'Erro ao localizar o colaborador informado, tente novamente.'}, status=400) 
    else:
        return JsonResponse({'O Colaborador informado não está cadastrado.'})
    
    
@csrf_exempt
def atualiza_dados_colaborador(request, matricula):
    
    if request.method =='PUT':
        
        try:
            colaborador = Colaborador.objects.get(matricula=matricula)
            data = json.loads(request.body)
            
            if data is not None:
                colaborador.first_name = data.get('first_name', colaborador.first_name)
                colaborador.last_name = data.get('last_name', colaborador.last_name)
                colaborador.is_staff = data.get('is_staff', colaborador.is_staff)
                colaborador.email = data.get('cpf', colaborador.cpf)
                colaborador.telefone = data.get('telefone', colaborador.telefone)
                colaborador.endereco__cep = data.get('cep', colaborador.endereco__cep)
                colaborador.endereco__rua = data.get('rua', colaborador.endereco__rua)
                colaborador.endereco__bairro = data.get('bairro', colaborador.endereco__bairro)
                colaborador.endereco__estado = data.get('estado', colaborador.endereco__estado)
                colaborador.endereco__cidade = data.get('cidade', colaborador.endereco__cidade)
                colaborador.endereco__numero = data.get('numero', colaborador.endereco__numero)
                colaborador.endereco__pais = data.get('pais', colaborador.endereco__pais)
                colaborador.setor__nome_setor = data.get('setor', colaborador.setor__nome_setor)
                colaborador.cargo__nome_cargo = data.get('cargo', colaborador.cargo__nome_cargo)
                
                colaborador.save()
                
                return JsonResponse({'message': f'Dados do colaborador {colaborador.first_name}, atualizados com sucesso!'})
                
        except Colaborador.DoesNotExist:        
            return JsonResponse({'error': 'Hmm, não consegui localizar esse colaborador, talvez seja necessário cadastrá-lo no sistema.'})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
        return JsonResponse({'error': 'Método não permitido!'}, status=405)
        
        


