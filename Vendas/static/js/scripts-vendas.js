document.getElementById('addRowButton').addEventListener('click', function(){
    const tabela = document.getElementById('tabela-pedidos').querySelector('tbody')
    const novaLinha =  document.getElementById('linha-template').cloneNode(true)

    novaLinha.style.display = ''
    novaLinha.id = ''
    tabela.appendChild(novaLinha)
})

document.querySelectorAll('th[data-produto-id]').forEach(th=> {
    document.getElementById('produto').addEventListener('click', function(){
        const produtoId = th.dataset.produtoId;
        const unidadeMedida = th.dataset.produtoUm;
        const valorUnitario = th.dataset.produtoValorUnit;
        const subtotal = th.dataset.produtoSubtotal;
        
        console.log(`Produto ID: ${produtoId}, Unidade: ${unidadeMedida}, Valor Unitário: ${valorUnitario}, Subtotal: ${subtotal}`);
    })  
})