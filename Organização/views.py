from .forms import EmpresaForm, SetorForm

def cria_empresa_view(request):

    form = EmpresaForm(request)

    if form.is_valid():
        form.save()
        return form
    else:
        form = EmpresaForm()
        return form

def cria_setor(request):

    form_setor = SetorForm(request)
    if form_setor.is_valid():

        form_setor.save()

    else:
        form = SetorForm()

    return form
