document.getElementById("buscarCliente").addEventListener("input", function() {
    const query = this.value;

    if (query.length < 1) {
        document.getElementById("resultadoBusca").innerHTML = ""; 
        return;
    }

    fetch(`/buscar-contatos/?q=${query}`)
        .then(response => response.json())
        .then(data => {
            const resultadoBusca = document.getElementById("resultadoBusca");
            resultadoBusca.innerHTML = "";  // Limpa os resultados anteriores

            // Exibe cada contato como um item de lista
            data.forEach(contato => {
                const item = document.createElement("li");
                item.textContent = contato.nome;
                item.classList.add("list-group-item", "list-group-item-action");
                item.onclick = () => {
                    document.getElementById("buscarCliente").value = contato.nome;  // Define o nome do contato selecionado no campo
                    resultadoBusca.innerHTML = "";  // Limpa a lista
                };
                resultadoBusca.appendChild(item);
            });
        })
        .catch(error => console.error("Erro na busca:", error));
});

document.addEventListener("DOMContentLoaded", function() {
    const addRowButton = document.getElementById("addRowButton");
    const salesTableBody = document.getElementById("salesTableBody");

    // Função para adicionar uma nova linha na tabela
    addRowButton.addEventListener("click", function() {
        const newRow = document.createElement("tr");

        newRow.innerHTML = `
            <td><label class="form-control">0</label></td>
            <td><input type="text" class="form-control" name="produto[]"></td>
            <td><input type="text" class="form-control" name="valor_total[]"></td>
            <td><input type="number" class="form-control" name="quantidade[]"></td>
            <td><input type="text" class="form-control" name="valor[]"></td>
            <td><button type="button" class="btn btn-danger btn-remove-row">x</button></td>
        `;
        salesTableBody.appendChild(newRow);

        // Adiciona o evento de remoção à nova linha
        newRow.querySelector(".btn-remove-row").addEventListener("click", function() {
            newRow.remove();
        });
    });

    // Função para remover uma linha existente
    document.querySelectorAll(".btn-remove-row").forEach(button => {
        button.addEventListener("click", function() {
            this.closest("tr").remove();
        });
    });
});