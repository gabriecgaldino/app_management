from django.shortcuts import render

def market_view(request):
    return render(request, 'market.html')

def developer_view(request):
    if request.method == 'POST':
        return 0
    return render(request, 'desenvolvedor/central_do_desenvolvedor.html')