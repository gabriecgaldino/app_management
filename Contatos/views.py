from django.shortcuts import render
from django.http import JsonResponse

from .models import Contatos
from Produto.models import Produto

def buscar_contatos(request):

    if request.method == 'GET':
        query = request.GET.get('q', '')
        user = request.user
        
        contatos = Contatos.objects.filter(colaborador=user, nome__icontains=query, is_Customer=True)

        contatos_data  = [ {'nome': contato.nome} for contato in contatos ]

        return JsonResponse(contatos_data, safe=False)
    
def buscar_produtos(request):
    if request.method == 'GET':
        query = request.GET.get('p', '')
        user = request.user

        produtos = Produto.objects.filter(estoque_id_id=user.organizacao, descricao=query)

        produto_data = [{
            'descricao': produto.nome,
            'valor': produto.valor
            }
            for produto in produtos
        ]



        return JsonResponse(produto_data)

