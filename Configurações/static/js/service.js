// Mascara para CEP
$(document).ready(function () {
    $('#cep').mask('00000-000');
});
document.getElementById('cep').addEventListener('blur', function () {
    const cep = this.value.replace(/\D/g, ''); 
    if (cep.length === 8) {
        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(response => response.json())
            .then(data => {
                if (!data.erro) {
                    document.getElementById('rua').value = data.logradouro || '';
                    document.getElementById('bairro').value = data.bairro || '';
                    document.getElementById('cidade').value = data.localidade || '';
                    document.getElementById('estado').value = data.uf || '';
                    document.getElementById('pais').value = data.country || 'Brasil';
                } else {
                    alert('CEP não encontrado!');
                }
            })
            .catch(error => console.error('Erro ao buscar o CEP:', error));
    } else {
        alert('CEP inválido!');
    }
});

// Filtro de setor baseado na Empresa selecionada
document.getElementById('empresa').addEventListener('change', function(){
    const setor = document.getElementById('setor')
    while (setor.firstChild) {
        setor.removeChild(setor.firstChild)
    }
    const empresaId = this.value

    try {
        fetch(`/api/setores/?empresa_id=${empresaId}`)
        .then(response => response.json())
        .then(data => {
            const setorField = document.getElementById('setor')

            setorField.innerHTML = ''

            if (!data) {
                return alert('Nenhum setor cadastrado para a empresa, realize o cadastro antes de seguir com o cadastro do colaborador.')
            }

            

            data.setores.forEach(setor => {
                const option = document.createElement('option')

                option.value = setor.id
                option.textContent = setor.nome_setor

                setorField.appendChild(option)
            })
        })
    } catch (err) {
       alert('Erro: ', err)
    }
})


//Filtro de cargo baseado no setor selecionado
document.getElementById('setor').addEventListener('change', function () {
    const cargo = document.getElementById('cargo')
    while (cargo.firstChild) {
        cargo.removeChild(cargo.firstChild)
    }
    const setorId = this.value

    try {
        fetch(`/api/cargos/?setor_id=${setorId}`)
        .then(response => response.json())
        .then(data => {
            const cargoField = document.getElementById('cargo')
            cargoField.innerHTML = ''

            const item = data.cargos

            if (item.length == 0) {
                return alert('Nenhum cargo cadastrado para o setor informado, realize o cadastro do cargo antes de seguir.')
            }

            data.cargos.forEach(cargo => {
                const option = document.createElement('option')
                option.value = cargo.id
                option.textContent = cargo.nome_cargo
                cargoField.appendChild(option)
            })
        })
    } catch (error) {
        alert(error)
    }
})


