from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import logging
from .forms import LoginForm
from .models import Colaborador

logger = logging.getLogger(__name__)

def login_view(request):
    form_login = LoginForm(request, data=request.POST or None)
    
    

    if request.method == 'POST':
        if form_login.is_valid():
            username = form_login.cleaned_data.get('username')
            password = form_login.cleaned_data.get('password')
            
            query_user = Colaborador.objects.get(username=username)

            if not query_user.is_developer:
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, f'Usuário autenticado com sucesso!')
                    return redirect('index')
                else:
                    messages.error(request, "Usuário ou senha incorretos.")
            else: 
                messages.warning(request, 'O acesso de desenvolvedor só está permitido na central do desenvolvedor.')
        else:
            messages.error(request, "Erro no preenchimento do formulário.")
            logger.error(f"Erro no formulário de login: {form_login.errors}")

    return render(request, 'login.html', {'form_login': form_login})
        


