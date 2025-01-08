document.querySelectorAll('.view-details').forEach(button=> {
    button.addEventListener('click', function () {
        const colaboradorId = this.getAttribute('data-id')

        try {
            fetch(`/api/colaboradores/?colaboradorId=${colaboradorId}`)
            .then(res => res.json())
            .then(data => {
                document.getElementById('nome_edit').textContent = data.colaborador[0].first_name
                document.getElementById('sobrenome_edit').value = data.colaborador[0].last_name
                document.getElementById('cpf_edit').value = data.colaborador[0].cpf
                document.getElementById('email_edit').value = data.colaborador[0].email
                


                
            })
        } catch(err) {
            alert('Não foi possível concluir a busca, tente novamente.', err)
        }
    })
})