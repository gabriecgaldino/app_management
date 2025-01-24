from django.shortcuts import render

def market_view(request):
    return render(request, 'market.html')

def developer_login_view(request):
    return render(request, 'desenvolvedor/login.html')

def developer_view(request):
    return render(request, 'desenvolvedor/central_do_desenvolvedor.html')