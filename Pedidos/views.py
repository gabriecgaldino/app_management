from .models import NovoPedido

def criar_pedido(request):
    form = NovoPedido(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return form