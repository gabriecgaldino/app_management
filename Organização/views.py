from django.shortcuts import redirect, render
from .forms import EmpresaForm
from django.contrib import messages


def cria_empresa_view(request):

    form = EmpresaForm(request)

    if form.is_valid():
        form.save()
        return form
    else:
        form = EmpresaForm()
        return form
