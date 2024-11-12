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

    document.querySelectorAll('.quantidade').forEach(item=> {
        item.addEventListener('change', function(){
            var quantidadeInput = novaLinha.querySelector('.quantidade')
            quantidadeInput = novaLinha.addEventListener('input', atualizarSubTotalELinha(quantidadeInput))
            atualizarValorTotal()
        })

    })
    
    var valorUnitarioInput = novaLinha.querySelector('.valor-unitario')

    
    valorUnitarioInput = novaLinha.addEventListener('input', atualizarSubTotalELinha(valorUnitarioInput))

    novaLinha.querySelector('.remover-linha').addEventListener('click', function(){
        novaLinha.remove()
        atualizarValorTotal()
    })

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
                            linha.querySelector('.valor-unitario').value = produto.valor_unitario
                            linha.querySelector(".codigo").textContent = produto.id

                            linha.querySelector('.subtotal').textContent = linha.querySelector('.valor-unitario').value * linha.querySelector(".quantidade").value
                            resultadoBusca.innerHTML = ""
                        })
                        resultadoBusca.appendChild(item)
                    })
                })
        }
    })
}

function atualizarSubTotalELinha(element) {
    const linha = element.closest('tr')
    let quantidade = parseFloat(linha.querySelector('.quantidade').value) || 0
    let valorUnitario = parseFloat(linha.querySelector('.valor-unitario').value) || 0
    let subtotal = quantidade * valorUnitario

    linha.querySelector('.subtotal').textContent = subtotal.toFixed(2)
    atualizarValorTotal()
}

function atualizarValorTotal() {
    let total = 0 
    const subtotais = document.querySelectorAll('.subtotal') || 0


    subtotais.forEach(subtotal => {
        const subTotal = parseFloat(subtotal.textContent) || 0
        total+= subTotal
    })

    document.querySelector('.valor-total').textContent = total.toFixed(2)
}