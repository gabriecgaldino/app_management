from django.shortcuts import render
from django.http import JsonResponse

from .models import Contatos

def buscar_contatos(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        user = request.user
        contatos = Contatos.objects.filter(nome__icontains=query)

        contatos_data = [{'nome': contato.nome} for contato in contatos]

        return JsonResponse(contatos_data, safe=False)
