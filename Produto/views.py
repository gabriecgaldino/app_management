from django.shortcuts import render, redirect
from Produto.models import CriaProduto, Produto
from Usuario.models import Colaborador
from Produto.models import Estoque
from django.contrib import messages


def cria_produto_view(request):
    colaborador = Colaborador.objects.get(username=request.user)
    estoque_organizacao = Estoque.objects.filter(organizacao=colaborador.organizacao)
    organizacao = colaborador.organizacao
    if request.method == 'POST':
        form = CriaProduto(request.POST, request.POST, organizacao=organizacao)

        if form.is_valid():
            form.save(commit=False)

            form.estoque = form.cleaned_data['estoque']
            form.organizacao = organizacao
            form.save()
            messages.success(request, 'Produto criado!')
            return redirect('estoque')
        else:
            produto = form()
            produto.fields['estoque'].queryset = estoque_organizacao
            messages.info(request, 'Erro ao criar o produto, tente novamente.')

    else:
        form = CriaProduto()

    return render(request, 'produtos.html', {'form': form})


def lista_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque.html', {'produtos': produtos})
