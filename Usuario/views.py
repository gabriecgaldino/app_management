from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ColaboradorForm, LoginForm


def login_view(request):
    if request.method == 'POST':
        form_login = LoginForm(request, data=request.POST)

        user = authenticate(username='47693697861', password='41674973@Gc')
        print("Usuário autenticado:", user)





        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Credenciais inválidas!')
        else:
            messages.error(request, 'Preencha todos os campos corretamente!')


    else:
        form_login = LoginForm()


        

    return render(request, 'login.html', {'form_login': form_login})



def cria_colaborador_view(request):
    form_colaborador = ColaboradorForm(request)
    if form_colaborador.is_valid():
        form_colaborador.save()

    return form_colaborador
