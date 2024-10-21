from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from Produto.models import CriaProduto, Produto
from Usuario.models import Colaborador


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
        query = request.GET.get('q')

        if query:
            produtos = Produto.objects.filter(descricao__icontains=query)
        else:
            produtos = Produto.objects.filter(
                estoque_id__organizacao=organizacao)

    return render(request, 'estoque.html', {
        'form': form,
        'produtos': produtos
    })


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
        form = Produto(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Produto atualizado com sucesso!'}, status=200)
        else:
            return JsonResponse({'message': 'Erro ao validar formulário!'}, status=400)
    return JsonResponse({'message': 'Método não permitido!'}, status=405)