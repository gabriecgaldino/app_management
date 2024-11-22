from django.shortcuts import render

def configuracoes_view(request):
    return render(request, 'configurações.html')