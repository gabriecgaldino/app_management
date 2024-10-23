from django.shortcuts import render
from Vendas.models import Vendas
from Usuario.models import Colaborador 
from django.contrib import messages

def nova_venda(request):
    if request.method == 'POST':
        form = Vendas(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido criada com sucesso!')
        else: 
            messages.info(request, 'Erro ao realizar pedido, tente novamente.')

    else: 
        form = Vendas()

    return render(request, 'vendas.html', {'form': form})

