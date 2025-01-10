import { listar_cargos_api } from "./service.mjs"

document.querySelectorAll('.view-details').forEach(button=> {
    button.addEventListener('click', function () {
        const colaboradorId = this.getAttribute('data-id')

        try {
            fetch(`/api/colaboradores/?colaboradorId=${colaboradorId}`)
            .then(res => res.json())
            .then(data => {
                document.getElementById('matricula').value = data.colaborador[0].matricula
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

document.getElementById('edit').addEventListener('click', function(event) {
    event.preventDefault()

    

    // 1° realizar as alterações dos botões 'fechar' e 'editar' para 'cancelar' e 'salvar'
    document.getElementById('edit').textContent = 'Salvar'
    document.getElementById('edit').setAttribute('class', 'btn btn-success')
    document.getElementById('close').textContent = 'Cancelar'
    document.getElementById('close').setAttribute('class', 'btn btn-secondary')

    // 2° capturar todos os campos que serão permitirão alteração
    const form = document.getElementById('editColaboradorForm')
    const inputs = form.querySelectorAll('input')
    const selects = form.querySelectorAll('select')

    // 3° configurar os campos de 'setor' e 'cargo' para exibirem a listagem de cargos e setores
    const setorField = document.getElementById('setor_edit')
    const empresaId = document.getElementById('empresa_notEditable').value
    try {
        // lista_setor_api()
    } catch (e){
        console.log(e)
    }

    // Listagem dos cargos
    document.getElementById('setor_edit').addEventListener('change', function(){
        // lista_cargo_api()
    })
    
    // 4° remover a propriedade disabled
    inputs.forEach(input=> {
        if(input.getAttribute('id') == 'cpf_edit' || input.getAttribute('id') =='empresa_notEditable' || input.getAttribute('id') == 'data_nascimento_edit'){
            
        }  else {
            input.removeAttribute('disabled')
        }
    })
    selects.forEach(item=> {
        item.removeAttribute('disabled')
    })

    



    
    // 5° enviar os dados para atualização no banco de dados
    
    

    
    

    /*
    document.getElementById('edit').textContent = 'Editar'
    document.getElementById('close').textContent = 'Fechar'
    document.getElementById('edit').setAttribute('class', 'btn btn-primary')
    document.getElementById('close').setAttribute('class', 'btn btn-danger')
    */
    
    
})

document.getElementById('edit').addEventListener('click', function(){  
    


})