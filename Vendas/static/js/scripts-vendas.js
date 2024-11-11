document.getElementById('addRowButton').addEventListener('click', function(){
    const tabel = document.getElementById('tabela-pedidos').getElementsByTagName('tbody')[0]
    const novaLinha = document.createElement('tr')


    novaLinha.innerHTML = `
    <td class='codigo'> </td>
    <td>
            <input type="text" class="form-control buscar-produto" placeholder="Buscar produto...">
            <div class="resultado-busca" style="position: relative;"></div>
    </td>
    <td class="unidade"></td>
    <td class="valor-unitario"></td>
    <td><input type="number" class="form-control quantidade" min="1" value="1"></td>
    <td class="subtotal"></td>
    <td><button class="btn btn-danger remover-linha">Remover</button></td>
    `

    tabel.appendChild(novaLinha)

    configBuscaProduto(novaLinha)
})

function configBuscaProduto(linha){
    const campoBusca = linha.querySelector('.buscar-produto')
    const resultadoBusca = linha.querySelector('.resultado-busca')

    campoBusca.addEventListener('input', async function(){
        const query = campoBusca.value
        if (query.length < 2){
            fetch(`/vendas/api-produtos/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    resultadoBusca.innerHTML = ''
                    data.produtos.forEach(produto => {
                        const item = document.createElement('div')
                        item.classList.add('list-group-item')
                        item.textContent = produto.descricao
                        item.addEventListener('click', function(){
                            campoBusca.value = produto.descricao
                            linha.querySelector(".unidade").textContent = produto.unidade_medida
                            linha.querySelector(".valor-unitario").textContent = produto.valor_unitario
                            resultadoBusca.innerHTML = ""
                        })
                        resultadoBusca.appendChild(item)
                    })
                })
        }
    })
}