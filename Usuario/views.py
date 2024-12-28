from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm

def login_view(request):
    form_login = LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form_login.is_valid():
            # Pega os dados validados
            username = form_login.cleaned_data.get('username')
            password = form_login.cleaned_data.get('password')

            # Autentica o usuário
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            
            return redirect('index')
    

    return render(request, 'login.html', {'form_login': form_login})
