from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from .forms import LoginForm
import logging

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

def busca_colaborador_api(request):
    colaboradorId = request.GET.get('colaboradorId')
    
    if colaboradorId is not None:
        try:
            colaborador = Colaborador.objects.filter(matricula__icontains=colaboradorId).values(
                'first_name', 'last_name', 'is_staff', 'cpf', 'email', 'telefone', 'data_nascimento',
                'empresa', 'setor', 'cargo'
                )
            return JsonResponse({'colaborador': list(colaborador)}, safe=False)
        except ValueError:
            return JsonResponse({'Erro ao localizar o colaborador informado, tente novamente.'}, status=400) 
    else:
        return JsonResponse({'O Colaborador informado não está cadastrado.'})
        


