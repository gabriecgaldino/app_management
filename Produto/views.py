from django.shortcuts import render, redirect
from django.contrib import messages
from Produto.models import CriaProduto, Produto
from Usuario.models import Colaborador
from Estoque.models import Estoque


def estoque_view(request):
    colaborador = Colaborador.objects.get(username=request.user)
    organizacao = colaborador.organizacao
    if request.method == 'POST':
        form = CriaProduto(request.POST, organizacao=organizacao)

        if form.is_valid():
            form.save(commit=False)

            form.save()
            messages.success(request, 'Produto criado!')
            return redirect('estoque')
        else:
            messages.info(request, 'Erro ao criar o produto, tente novamente.')

    else:
        form = CriaProduto(organizacao=organizacao)
        produtos = Produto.objects.filter(estoque_id__organizacao=organizacao)
        query = request.GET.get('q')

        if query:
            produtos = produtos.filter(descricao__icontains=query)

    return render(request, 'estoque.html', {
        'form': form,
        'produtos': produtos
    })
