document.querySelectorAll('.view-details').forEach(button=> {
    button.addEventListener('click', function () {
        const colaboradorId = this.getAttribute('data-id')

        try {
            fetch(`/api/colaboradores/?colaboradorId=${colaboradorId}`)
            .then(res => res.json())
            .then(data => {
                document.getElementById('nome_edit').value = data.colaborador[0].first_name
                document.getElementById('sobrenome_edit').value = data.colaborador[0].last_name
                document.getElementById('cpf_edit').value = data.colaborador[0].cpf
                document.getElementById('email_edit').value = data.colaborador[0].email
                document.getElementById('telefone_edit').value = data.colaborador[0].telefone
                document.getElementById('data_nascimento_edit').value = data.colaborador[0].data_nascimento
                document.getElementById('cep_edit').value = data.colaborador[0].endereco__cep
                document.getElementById('rua_edit').value = data.colaborador[0].endereco__rua
                document.getElementById('n_edit').value = data.colaborador[0].endereco__numero
                document.getElementById('estado_edit').value = data.colaborador[0].endereco__estado
                document.getElementById('cidade_edit').value = data.colaborador[0].endereco__cidade
                document.getElementById('bairro_edit').value = data.colaborador[0].endereco__bairro
                document.getElementById('pais_edit').value = data.colaborador[0].endereco__pais
                document.getElementById('empresa_notEditable').value = data.colaborador[0].empresa__nome_fantasia

                const opSetor = document.createElement('option')
                const opCargo = document.createElement('option')

                opSetor.textContent = data.colaborador[0].setor__nome_setor
                opCargo.textContent = data.colaborador[0].cargo__nome_cargo
                
                document.getElementById('setor_edit').appendChild(opSetor) 
                document.getElementById('cargo_edit').appendChild(opCargo)

                if (data.colaborador[0].is_active) {
                    document.getElementById('is_active_edit').checked = true
                } else {
                    document.getElementById('is_active_edit').checked = false
                }

                if (data.colaborador[0].is_staff) {
                    document.getElementById('is_staff_edit').checked = true
                } else {
                    document.getElementById('is_staff_edit').checked = false
                }

                

                
                


                
            })
        } catch(err) {
            alert('Não foi possível concluir a busca, tente novamente.', err)
        }
    })
})