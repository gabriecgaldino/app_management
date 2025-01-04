from .forms import EmpresaForm, SetorForm, CargoForm
from .models import Cargo, Setor
from django.shortcuts import render, redirect
from django.http import JsonResponse



def cria_empresa_view(request):

    form = EmpresaForm(request)

    if form.is_valid():
        form.save()
        return form
    else:
        form = EmpresaForm()
        return form

def cria_setor(request):
    print(request.POST)
    if request.method == 'POST':
        form_setor = SetorForm(request.POST)
        if form_setor.is_valid():
            setor = form_setor.save(commit=False)
            setor.save()
            return SetorForm()
    else: 
        form_setor = SetorForm()

    return form_setor

def cria_cargo(request):
    if request.method == 'POST': 
        form_cargo = CargoForm(request.POST)
        if form_cargo.is_valid():
            form_cargo.save()
            return redirect('configurações')
            
        else: 
            form_cargo = CargoForm()

    return form_cargo

def listar_setores_api(request):
    empresa_id = request.GET.get('empresa_id')
    if empresa_id is not None:
        try:
            setores = Setor.objects.filter(empresa=empresa_id).values('id', 'nome_setor')
            return JsonResponse({'setores': list(setores)}, safe=False)
        except ValueError:
            return JsonResponse({'error': 'empresa_id inválido'}, status=400)
    return JsonResponse({'error': 'empresa_id não fornecido'}, status=400)

def listar_cargos_api(request):
    setor_id = request.GET.get('setor_id')
    if setor_id is not None:
        try:
            # Filtra pelo setor usando o campo da chave estrangeira
            cargos = Cargo.objects.filter(setor=setor_id).values('id', 'nome_cargo')
            return JsonResponse({'cargos': list(cargos)}, safe=False)
        except ValueError:
            return JsonResponse({'error': 'setor_id inválido'}, status=400)
    return JsonResponse({'error': 'setor_id não fornecido'}, status=400)