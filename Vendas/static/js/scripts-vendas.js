document.addEventListener("DOMContentLoaded", function() {
    const addRowButton = document.getElementById("addRowButton")
    const salesTableBody = document.getElementById("salesTableBody")

    addRowButton.addEventListener("click", function() {
        const newRow = document.createElement("tr")

        newRow.innerHTML = `
            <td class="col-1">
                <input id="produtoId" class="form-control" readonly ></input>
            </td>
            <td class="col-3">
                <select name="produto" class="form-control" id="produtoSelecionado">
                    {% for produto in form.fields.produto.queryset %}
                        <option 
                            value="{{produto.id}}" class="form-control"
                            data-unidade="{{produto.unidade_medida}}"
                            data-valor="{{produto.valor}}"></option>
                    {% empty %}
                        <option>Nenhum produto disponível</option>
                    {% endfor %}
                </select>
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


document.addEventListener('DOMContentLoaded', ()=>{
    const listen = document.getElementById('produtoSelecionado')

    listen.addEventListener('change', function() {
        const selectedOption = this.options[this.selectedIndex]
    
        // Obtendo os valores dos atributos de dados
        const unidadeMedida = selectedOption.getAttribute('data-unidade')
        const valorProduto = selectedOption.getAttribute('data-valor')
        const id = selectedOption.getAttribute('value')

    
        // Preenchendo os campos com os valores obtidos
        document.getElementById('unidadeMedida').value = unidadeMedida
        document.getElementById('valorProduto').value = valorProduto
        document.getElementById('produtoId').value = id
    })
})

