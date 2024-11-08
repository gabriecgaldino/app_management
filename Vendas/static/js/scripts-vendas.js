document.addEventListener("DOMContentLoaded", function() {
    const addRowButton = document.getElementById("addRowButton")
    const salesTableBody = document.getElementById("salesTableBody")

    addRowButton.addEventListener("change", function() {
        const newRow = document.createElement("tr")

        newRow.innerHTML = `
            <td class="col-1">
                <input id="produtoId" class="form-control" readonly ></input>
            </td>
            <td class="col-3">
                <input type="text" class="form-control" id="buscaProduto">
            </td>
            <td class="col-2">
                <input type="text" id="unidadeMedida" class="form-control" readonly></input>
            </td>
            <td class="col-2">
                <input id="valorProduto" class="form-control" readonly></input>
            </td>
            <td class="col-1">
                <input type="text" class="form-control">
            </td>
            <td class="col-2">
                <input type="text" class="form-control">
            </td>
            <td>
                <button type="button" class="btn btn-danger btn-remove-row">X</button>
            </td>
        `
        salesTableBody.appendChild(newRow);

        newRow.querySelector(".btn-remove-row").addEventListener("click", function() {
            newRow.remove();
        })
    });

    document.querySelectorAll(".btn-remove-row").forEach(button => {
        button.addEventListener("click", function() {
            this.closest("tr").remove();
        })
    })
})

document.getElementById('buscaProduto').addEventListener('input', function() {
    const query = this.value

    if (query.length < 1) {
        document.getElementById("buscaProduto").innerHTML = "" 
        return;
    }

    fetch(`/vendas/api-produtos/q=${query}`)
        .then(response=> response.json())
        .then(data=> {
            const resultadoBusca = document.getElementById('resultadoBuscaProduto')
            resultadoBusca.innerHTML = ''

            data.forEach(produto=> {
                const item = createElement('li')
                item.textContent = produto.descricao
                item.classList.add('list-group-item', 'list-group-item-action')
                item.onclick = () =>{
                    document.getElementById('buscaProduto').value = produto.descricao
                    resultadoBusca.innerHTML = ''
                }
                resultadoBusca.appendChild(item)
            })
        })
        .catch(err => console.log('Erro ao buscar produto', err))


})

