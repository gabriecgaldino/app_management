document.addEventListener("DOMContentLoaded", function () {
    const cpfInput = document.getElementById("cpf");

    cpfInput.addEventListener("input", function () {
        // Remove caracteres não numéricos
        let value = cpfInput.value.replace(/\D/g, "");

        // Limita o CPF a 11 dígitos numéricos
        if (value.length > 11) value = value.slice(0, 11);

        // Adiciona a formatação do CPF (###.###.###-##)
        if (value.length > 9) {
            value = value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
        } else if (value.length > 6) {
            value = value.replace(/(\d{3})(\d{3})(\d{1,3})/, "$1.$2.$3");
        } else if (value.length > 3) {
            value = value.replace(/(\d{3})(\d{1,3})/, "$1.$2");
        }

        cpfInput.value = value;
    });



    const form = document.getElementById("formCadastroColaborador");
    const errorSpan = document.getElementById("cpfError");

    form.addEventListener("submit", function (event) {
        const cpf = cpfInput.value;
        if (!validarCPF(cpf)) {
            event.preventDefault();
            errorSpan.textContent = "CPF inválido. Por favor, insira um CPF válido.";
            errorSpan.classList.add("text-danger");
        } else {
            errorSpan.textContent = ""; 
        }

        
    });

    const urlParams = new URLSearchParams(window.location.search);
    const matricula = urlParams.get('matricula');

    if (matricula) {
        const modal = new bootstrap.Modal(document.getElementById('editColaboradorModal'));
        modal.show();
    }

    const formEdit = document.getElementById('editColaboradorForm')
    inputs = formEdit.querySelectorAll('input')
    selects = formEdit.querySelectorAll('select')
    checkboxs = formEdit.querySelectorAll('checkbox')

    let options = [inputs, selects, checkboxs]

    options.forEach(option=> {
        option.forEach(item=> {
            item.disabled = true
        })
    })

    document.getElementById('edit').addEventListener('click', function() {
        const form = document.getElementById('editColaboradorForm');
    
        const inputs = form.querySelectorAll('input, select, input[type="checkbox"]');
        inputs.forEach(item => {
            item.disabled = false;
        });

        // alteração dos botões do formulário
        document.getElementById('edit').remove()

        const buttonSave = document.createElement('button')

        buttonSave.setAttribute('id', 'save')
        buttonSave.setAttribute('class', 'btn btn-success')
        buttonSave.textContent = 'Salvar'
        buttonSave.setAttribute('name', 'atualizar')

        document.getElementById('footerModal').appendChild(buttonSave)
        buttonSave.addEventListener('click', function() {
            const form = document.getElementById('editColaboradorForm');
            console.log('formulário enviado')
            form.submit();
        }); 
    });
});

function validarCPF(cpf) {
    cpf = cpf.replace(/\D/g, ""); 

    if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) return false; 

    let soma = 0;
    let resto;

    for (let i = 1; i <= 9; i++) soma += parseInt(cpf[i - 1]) * (11 - i);
    resto = (soma * 10) % 11;

    if (resto === 10 || resto === 11) resto = 0;
    if (resto !== parseInt(cpf[9])) return false;

    soma = 0;
    for (let i = 1; i <= 10; i++) soma += parseInt(cpf[i - 1]) * (12 - i);
    resto = (soma * 10) % 11;

    if (resto === 10 || resto === 11) resto = 0;
    return resto === parseInt(cpf[10]);
}






