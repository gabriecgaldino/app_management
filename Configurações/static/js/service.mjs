// Mascara para CEP
$(document).ready(function () {
    $('#cep').mask('00000-000');
    $('#cep_edit').mask('00000-000');
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


document.getElementById('edit').addEventListener('click', function(){
    const buttonEdit = document.getElementById('edit')

    buttonEdit.setAttribute('name', 'atualizar')
})


