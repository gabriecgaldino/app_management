// Lógica de edição dos produtos
document.querySelectorAll('.btn-editar').forEach(button => {
    button.addEventListener('click', function () {
        const row = this.closest('tr');
        const fields = row.querySelectorAll('.editavel');

        fields.forEach(field => {
            field.setAttribute('data-original', field.textContent.trim());
            field.setAttribute('contenteditable', 'true');
            field.classList.add('editable');
        });

        fields.forEach(field => {
            field.setAttribute('contenteditable', 'true');
            field.classList.add('editable');
        });

        row.querySelector('.btn-confirmar').classList.remove('d-none');
        row.querySelector('.btn-cancelar').classList.remove('d-none');
        this.classList.add('d-none'); 
    });
});

document.querySelectorAll('.btn-cancelar').forEach(button => {
    button.addEventListener('click', function () {
        const row = this.closest('tr');
        const fields = row.querySelectorAll('.editavel');

        fields.forEach(field => {
            const originalValue = field.getAttribute('data-original');
            field.textContent = originalValue;  // Restaura o valor original
            field.setAttribute('contenteditable', 'false');
            field.classList.remove('editable');
        });

        fields.forEach(field => {
            field.setAttribute('contenteditable', 'false');
            field.classList.remove('editable');
            field.textContent = field.getAttribute('data-original');  
        });

        row.querySelector('.btn-editar').classList.remove('d-none');
        row.querySelector('.btn-confirmar').classList.add('d-none');
        this.classList.add('d-none');
    });
});

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
