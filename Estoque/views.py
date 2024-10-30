from django.shortcuts import render, redirect
from django.contrib import messages


from Produto.models import CriaProduto, Produto
from Usuario.models import Colaborador
from Produto.views import buscar_produto

def estoque_view(request):
    colaborador = Colaborador.objects.get(username=request.user)
    organizacao = colaborador.organizacao

    if request.method == 'POST':
        form = CriaProduto(request.POST, organizacao=organizacao)
        if form.is_valid():
            novo_produto = form.save(commit=False)
            novo_produto.organizacao = organizacao
            novo_produto.save()
            messages.success(request, 'Produto criado!')
            return redirect('estoque')
        else:
            messages.info(request, 'Erro ao criar o produto, tente novamente.')
    else:
        produtos_encontrados = buscar_produto(request)

        form = CriaProduto(organizacao=organizacao)

    return render(request, 'estoque.html', {
        'form': form,
        'produtos': produtos_encontrados
    })
