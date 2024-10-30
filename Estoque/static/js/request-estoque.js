

// Capturar o ID do produto quando o modal for aberto
document.getElementById('confirmDeleteModal').addEventListener('show.bs.modal', function (event) {
    let button = event.relatedTarget;  // Botão que acionou o modal
    produtoId = button.getAttribute('data-produto-id');  // Extrai o ID do produto
});

document.getElementById('confirmDeleteButton').addEventListener('click', async function () {
    await fetch(`/estoque/excluir/${produtoId}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
    })
        .then(response =>{
            if (response.ok) {
                
                document.getElementById(`${produtoId}`).remove()
                let modal = bootstrap.Modal.getInstance(document.getElementById('confirmDeleteModal'));
                modal.hide();
                alert('Protudo removido com sucesso.')
            } else {
                alert('Erro ao excluir o produto.');
            }
        });
});

// Enviar solicitação de atualização dos dados dos produtos. 
document.querySelectorAll('.btn-confirmar').forEach(button => {
    button.addEventListener('click', function () {
        const row = this.closest('tr');
        const produtoId = row.getAttribute('id');
        const fields = row.querySelectorAll('.editavel');
        let data = {};

        // Coleta os novos valores dos campos
        fields.forEach(field => {
            const fieldName = field.getAttribute('data-field');
            const newValue = field.textContent.trim();
            data[fieldName] = newValue;
        });

        // Enviar os dados via AJAX para o servidor
        fetch(`/produto/editar/${produtoId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                fields.forEach(field => {
                    field.setAttribute('contenteditable', 'false');
                    field.classList.remove('editable');
                });
                row.querySelector('.btn-editar').classList.remove('d-none');
                row.querySelector('.btn-confirmar').classList.add('d-none');
                row.querySelector('.btn-cancelar').classList.add('d-none');
            } else {
                alert('Erro ao atualizar o produto.');
            }
        })
        .catch(error => console.error('Erro na requisição:', error));
    });
});