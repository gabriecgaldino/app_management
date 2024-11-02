from django.shortcuts import render
from Vendas.models import Vendas, CriarPedido
from Produto.models import Produto

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
        organizacao = request.user.colaborador.organizacao
        produtos_disponiveis = Produto.objects.filter(estoque_id__organizacao=organizacao)
        
        
        form.fields['produto'].queryset= produtos_disponiveis

    return render(request, 'vendas.html', {'form': form})




