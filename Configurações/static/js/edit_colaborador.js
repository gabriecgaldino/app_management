document.querySelectorAll('.view-details').forEach(button=> {
    button.addEventListener('click', function () {
        const colaboradorId = this.getAttribute('data-id')

        try {
            fetch(`/api/colaboradores/?colaboradorId=${colaboradorId}`)
            .then(res => res.json())
            .then(data => {
                document.getElementById('nome').value = data.colaborador[0].first_name
                document.getElementById('sobrenome').value = data.colaborador[0].last_name


                
            })
        } catch(err) {
            alert('Não foi possível concluir a busca, tente novamente.', err)
        }
    })
})