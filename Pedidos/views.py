from .models import PedidoProdutoForm

def criar_pedido(request):
    form = PedidoProdutoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return form