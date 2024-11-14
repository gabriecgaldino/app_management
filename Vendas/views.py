from django.shortcuts import render
from Vendas.models import Vendas
from Pedidos.views import criar_pedido

from django.contrib import messages


def vendas(request):    
    if request.method == 'POST':
        form = criar_pedido(request)
        
        if form.is_valid():
            nova_venda = Vendas(form)
            nova_venda.save()
            print(form)
            messages.success(request, 'Pedido criada com sucesso!')
        else: 
            print(form)
            messages.info(request, 'Erro ao realizar pedido, tente novamente.')

    else: 
        form = Vendas

    vendas = Vendas.objects.all()

    return render(request, 'vendas.html', {'form': form, 'vendas': vendas})




