from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
import json

from Produto.models import Produto
from Usuario.models import Colaborador

def buscar_produto(request):
    colaborador = Colaborador.objects.get(username=request.user)
    organizacao = colaborador.organizacao
    if request.method == 'GET':
        query = request.GET.get('q')

        if query:
            produtos = Produto.objects.filter(descricao__icontains=query)
        else:
            produtos = Produto.objects.filter(
                estoque_id__organizacao=organizacao)
            
    render(request, 'estoque.html', {'produtos': produtos})



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
        produto.unidade_medida = data.get('unidade_medida', produto.unidade_medida)
        produto.quantidade = data.get('quantidade', produto.quantidade)
        produto.valor = data.get('valor', produto.valor)
        produto.save()

        return JsonResponse({'message': 'Produto atualizado com sucesso!'}, status=200)
    
    return JsonResponse({'message': 'Método não permitido'}, status=405)