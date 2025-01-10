
export async function listar_setor_api(empresa_id, setor_field){
    await fetch(`/api/setores/?empresa_id=${empresa_id}`)
    .then(res=> res.json())
    .then(data=> {
        const setorField = setor_field

        if(data.setores.length == 0) {
            return alert('Nenhum setor cadastrado na empresa!')
        }

        data.setores.forEach(setor => {
            const option = document.createElement('option')

            option.value = setor.id
            option.textContent = setor.nome_setor

            setorField.appendChild(option)
        })

    })
}
document.getElementById('empresa').addEventListener('change', function(){
    const setor = document.getElementById('setor')
    const empresaId = this.value

    while(setor.firstChild){
        setor.removeChild(setor.firstChild)
    }

    try {
        return listar_setor_api(empresaId, setor)
    } catch (err) {
       alert('Erro: ', err)
    }
})


export async function listar_cargos_api(setor_id, cargo_field){
    await fetch(`/api/cargos/?setor_id=${setor_id}`)
    .then(res=> res.json())
    .then(data=> {
        const cargoField = cargo_field

        if (data.cargos.length == 0) {
            return alert('Nenhum cargo cadastrado para o setor informado.')
        }

        data.cargos.forEach(cargo => {
            const option = document.createElement('option')
            option.value = cargo.id
            option.textContent = cargo.nome_cargo
            cargoField.appendChild(option)
        })
    })
}

document.getElementById('setor').addEventListener('change', function () {
    const cargo = document.getElementById('cargo')
    const setorId = this.value

    while (cargo.firstChild){
        cargo.removeChild(cargo.firstChild)
    }

    try {
        listar_cargos_api(setorId, cargo)
    } catch (error) {
        alert(error)
    }
})

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


