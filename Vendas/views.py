from django.shortcuts import render
from Vendas.models import CriarPedido, Vendas

from django.contrib import messages


def vendas(request):    
    if request.method == 'POST':
        form = CriarPedido(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido criada com sucesso!')
        else: 
            messages.info(request, 'Erro ao realizar pedido, tente novamente.')

    else: 
        form = CriarPedido()

    vendas = Vendas.objects.all()

    return render(request, 'vendas.html', {'form': form, 'vendas': vendas})




