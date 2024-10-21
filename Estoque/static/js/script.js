
// Ao clicar no botão de exclusão
let produtoId;

// Capturar o ID do produto quando o modal for aberto
document.getElementById('confirmDeleteModal').addEventListener('show.bs.modal', function (event) {
    let button = event.relatedTarget;  // Botão que acionou o modal
    produtoId = button.getAttribute('data-produto-id');  // Extrai o ID do produto
});

// Enviar solicitação de exclusão quando o botão "Excluir" for clicado
document.getElementById('confirmDeleteButton').addEventListener('click', function () {
    fetch(`/estoque/excluir/${produtoId}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
        },
    })
        .then(response => {
            if (response.ok) {
                console.log(`produto-${produtoId}`)
                document.getElementById(`produto-${produtoId}`).remove();
                let modal = bootstrap.Modal.getInstance(document.getElementById('confirmDeleteModal'));
                modal.hide();
                alert('Produto removido com sucesso!')
            } else {
                alert('Erro ao excluir o produto.');
            }
        });
});

// Ao clicar no botão de edição
document.querySelectorAll('.btn-editar').forEach(button => {
    button.addEventListener('click', function() {
        const produtoId = this.getAttribute('data-id');
        
        // Fazer requisição para buscar os dados do produto
        fetch(`/produto/${produtoId}/`)
            .then(response => response.json())
            .then(data => {
                // Preencher os campos do modal com os dados do produto
                document.getElementById('editDescricao').value = data.descricao;
                document.getElementById('editUnidade').value = data.unidade_medida;
                document.getElementById('editQuantidade').value = data.quantidade;
                document.getElementById('editValor').value = data.valor;
                document.getElementById('editProdutoId').value = data.id;
            })
            .catch(error => console.error('Erro ao carregar dados do produto:', error));
    });
});

// Lógica para salvar as alterações
document.getElementById('editProductForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const produtoId = document.getElementById(`${produto.id}`).value;
    console.log(produtoId)
    
    const formData = {
        descricao: document.getElementById('editDescricao').value,
        unidade_medida: document.getElementById('editUnidade').value,
        quantidade: document.getElementById('editQuantidade').value,
        valor: document.getElementById('editValor').value
    };
    
    fetch(`/produto/editar/${produtoId}/`, {
        
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (response.ok) {
            location.reload(); // Recarregar a página após salvar as alterações
        } else {
            console.error('Erro ao salvar produto');
        }
    })
    .catch(error => console.error('Erro ao salvar produto:', error));
});

