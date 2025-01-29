from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .forms import DeveloperLoginForm, DeveloperRegisterForm, AppRegisterForm
from Usuario.models import Developer
from .models import App



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


def developer_view(request):
    dev = request.user.id
    app_form = AppRegisterForm()
    apps = App.objects.all()
    
    if request.method == 'POST':
        app_form = AppRegisterForm(request.POST, request.FILES)

        if app_form.is_valid():
            app_instance = app_form.save(commit=False)
            
            try:
                developer = Developer.objects.get(id=dev)
                app_instance.autor = developer
            except Developer.DoesNotExist:
                messages.error(request, 'Você precisa ser um desenvolvedor para postar um aplicativo!')
                return redirect('/developer/')

            app_instance.save() 
            messages.success(request, 'Aplicativo postado com sucesso!')
            return redirect('/developer/')

        else:
            messages.error(request, 'Erro ao realizar upload, tente novamente mais tarde!')

    return render(request, 'desenvolvedor/central_do_desenvolvedor.html', {
        'app_form': app_form,
        'apps': apps
    })


