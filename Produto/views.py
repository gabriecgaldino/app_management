from django.shortcuts import render
from Produto.models import CriaProduto, Produto
from django.contrib import messages


def cria_produto_view(request):
    if request.method == 'POST':
        form = CriaProduto(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado!')
        else:
            messages.info(request, 'Erro ao criar o produto, tente novamente.')

    else:
        form = CriaProduto()

    return render(request, 'produtos.html', {'form': form})


def lista_produto(request):
    produto = Produto.objects.all()
    return render(request, 'estoque.html', {'produtos': produto})
