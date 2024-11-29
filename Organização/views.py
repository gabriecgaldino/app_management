from .forms import EmpresaForm, SetorForm, CargoForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



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
            return redirect('configurações')
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

