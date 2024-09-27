from django.shortcuts import render, redirect
from django.contrib import messages
from Produto.models import CriaProduto, Produto
from Usuario.models import Colaborador


def cria_produto_view(request):
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

    return render(request, 'produtos.html', {'form': form})


def lista_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque.html', {'produtos': produtos})
