from django.shortcuts import render
from Vendas.models import Vendas, NovaVenda
from Produto.models import Estoque
from django.contrib import messages

def vendas(request):
    if request.method == 'POST':
        form = NovaVenda(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido criada com sucesso!')
        else: 
            messages.info(request, 'Erro ao realizar pedido, tente novamente.')

    else: 
        form = Vendas()

    return render(request, 'vendas.html', {'form': form})




