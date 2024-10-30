from django.shortcuts import render, redirect
from django.contrib import messages
from Produto.views import busca_produtos, cadastra_produto


def estoque_view(request):
    form = None
    produtos = None

    if request.method == 'POST':
        form = cadastra_produto(request)
    else:
        produtos = busca_produtos(request)

    context = {'produtos': produtos}

    if form:
        context['form'] = form

    return render(request, 'estoque.html', context)
