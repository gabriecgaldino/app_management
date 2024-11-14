document.getElementById('addRowButton').addEventListener('click', function(){
    const tabela = document.getElementById('tabela-pedidos').querySelector('tbody')
    const novaLinha =  document.getElementById('linha-template').cloneNode(true)

    novaLinha.style.display = ''
    novaLinha.id = ''
    tabela.appendChild(novaLinha)
})

document.querySelectorAll('th[data-produto-id]').forEach(th=> {
    document.getElementById('produto').addEventListener('click', function(){
    })  
})