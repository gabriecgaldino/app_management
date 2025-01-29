from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import DeveloperLoginForm, DeveloperRegisterForm, AppRegisterForm
from Usuario.models import Developer
from .models import App

import os
import zipfile

from .verify_app import verify_app




def market_view(request):
    return render(request, 'market.html')

def developer_logout_view(request):
    logout(request)
    messages.success(request, 'Desenvolvedor, desconectado com sucesso!')
    return redirect('/developer/login/')

def developer_login_view(request):
    form_login = DeveloperLoginForm()
    form_register = DeveloperRegisterForm()

    if 'login' in request.POST:
        form_login = DeveloperLoginForm(request, data=request.POST or None)
        if form_login.is_valid():
            username = form_login.cleaned_data.get('username')
            password = form_login.cleaned_data.get('password')

            # backend personalizado para autenticar
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                
                login(request, user)
                messages.success(request, 'Desenvolvedor autenticado!')
                return redirect('/developer/')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            messages.warning(request, 'Hmm, formulário preenchido incorretamente.')

    if 'register' in request.POST:
        try: 
            form_register = DeveloperRegisterForm(request.POST)
            if form_register.is_valid():
                developer = form_register.save()
                developer.save()
                messages.success(request, 'Usuário cadastrado com sucesso, realize o login!')
                return redirect('/developer/login/')
        except ValueError:
            messages.error(request, f'Erro ao criar usuário, verifique e tente novamente.')

    return render(request, 'desenvolvedor/login.html', {
        'form_login': form_login,
        'form_register': form_register
    })

@login_required
def developer_view(request):
    dev = request.user.id
    app_form = AppRegisterForm()
    apps = App.objects.all()
    
    if request.method == 'POST':
        app_form = AppRegisterForm(request.POST, request.FILES)

        if app_form.is_valid():
            uploaded_files = request.FILES['zip_file']
            app_instance = app_form.save(commit=False)
            
            
            if not zipfile.is_zipfile(uploaded_files):
                messages.error(request, 'O arquivo postado não está em formato ZIP.')
                return redirect('/developer/')
            
            try:
                developer = Developer.objects.get(id=dev)
                
                app_dir = os.path.join(settings.MEDIA_ROOT, f'apps/{developer.first_name}')
                
                os.makedirs(app_dir, exist_ok=True)
                
                with zipfile.ZipFile(uploaded_files, 'r') as zip_ref:
                    zip_ref.extractall(app_dir)
                    
                    
                app_instance.autor = developer
                app_instance.save()
                
                verification_result = verify_app(app_instance)
                
                if verification_result is True:
                    messages.success(request, 'Aplicativo enviado e aprovado com sucesso!')
                else:
                    messages.error(request, f"Erro ao verificar o aplicativo: {verification_result}")
                    return redirect('/developer/')
                    
                return redirect('/developer/')
                
                
            except Developer.DoesNotExist:
                messages.error(request, 'Você precisa ser um desenvolvedor para postar um aplicativo!')
                return redirect('/developer/')

        else:
            app_form = AppRegisterForm()
            messages.error(request, 'Erro ao realizar upload, tente novamente mais tarde!')

    return render(request, 'desenvolvedor/central_do_desenvolvedor.html', {
        'app_form': app_form,
        'apps': apps
    })


