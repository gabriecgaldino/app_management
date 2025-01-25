from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import DeveloperLoginForm, DeveloperRegisterForm



def market_view(request):
    return render(request, 'market.html')

def developer_login_view(request):
    form_login = DeveloperLoginForm()
    form_register = DeveloperRegisterForm()

    if 'login' in request.POST:
        form_login = DeveloperLoginForm(request, data=request.POST or None)
        if form_login.is_valid():
            username = form_login.cleaned_data.get('username')
            password = form_login.cleaned_data.get('password')

            # Use o backend personalizado para autenticar
            user = authenticate(request, username=username, password=password, backend='Market.auth_backends.DeveloperAuthBackend')
            if user:
                login(request, user)
                messages.success(request, 'Usuário autenticado!')
                return redirect('/developer/')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            messages.warning(request, 'Hmm, formulário preenchido incorretamente.')

    if 'register' in request.POST:
        form_register = DeveloperRegisterForm(request.POST)
        if form_register.is_valid():
            developer = form_register.save(commit=True)
            developer.save()
            messages.success(request, 'Usuário cadastrado com sucesso, realize o login!')
            return redirect('developer_login_view')
        else:
            messages.error(request, 'Dados preenchidos incorretamente, verifique e tente novamente.')

    return render(request, 'desenvolvedor/login.html', {
        'form_login': form_login,
        'form_register': form_register
    })


def developer_view(request):

        
    return render(request, 'desenvolvedor/central_do_desenvolvedor.html')
