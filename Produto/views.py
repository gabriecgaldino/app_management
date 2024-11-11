from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.http import JsonResponse
import json

from Produto.models import Produto, CriaProduto
from Usuario.models import Colaborador


def busca_produtos(request):
    if request.method == 'GET':
        colaborador = get_object_or_404(Colaborador, username=request.user)
        organizacao = colaborador.organizacao

        CriaProduto(organizacao=organizacao)

    query = request.GET.get('q', '')
    if query:
        produtos = Produto.objects.filter(
            descricao__icontains=query, estoque_id__organizacao=organizacao)
    else:
        produtos = Produto.objects.filter(estoque_id__organizacao=organizacao)

    return produtos

def busca_produtos_json(request):
    query = request.GET.get('q', '')
    produtos_data = []

    if query:
        produtos = Produto.objects.filter(descricao__icontains=query)

        produtos_data = [{
            'id': produto.id,
            'descricao': produto.descricao,
            'unidade_medida': produto.unidade_medida,
            'valor_unitario': produto.valor,

        } for produto in produtos]

        return JsonResponse({ 'produtos': produtos_data })


def cadastra_produto(request):
    colaborador = get_object_or_404(Colaborador, username=request.user)
    organizacao = colaborador.organizacao

    if request.method == 'POST':
        form = CriaProduto(request.POST, organizacao=organizacao)
        if form.is_valid():
            novo_produto = form.save(commit=False)
            novo_produto.organizacao = organizacao
            novo_produto.save()
            messages.success(request, 'Produto criado!')
            return novo_produto
        else:
            messages.info(request, 'Erro ao criar o produto, tente novamente.')

    return None


def excluir_produto(request, produto_id):
    if request.method == 'DELETE':
        produto = get_object_or_404(Produto, id=produto_id)
        produto.delete()
        return JsonResponse({'message': 'Produto removido!'}, status=200)
    else:
        return JsonResponse({'message': 'Produto não encontrado.'}, status=404)


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        produto.descricao = data.get('descricao', produto.descricao)
        produto.unidade_medida = data.get(
            'unidade_medida', produto.unidade_medida)
        produto.quantidade = data.get('quantidade', produto.quantidade)
        produto.valor = data.get('valor', produto.valor)
        produto.save()

        return JsonResponse({'message': 'Produto atualizado com sucesso!'}, status=200)

    return JsonResponse({'message': 'Método não permitido'}, status=405)
