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

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("loginForm");
    const cpfInput = document.getElementById("cpf");
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
});

document.addEventListener("DOMContentLoaded", function () {
    const dobInput = document.getElementById("data_nascimento");

    dobInput.addEventListener("input", function () {
        let value = dobInput.value.replace(/\D/g, "");

        // Limita o campo a 8 dígitos numéricos (DDMMAAAA)
        if (value.length > 8) value = value.slice(0, 8);

        // Adiciona a formatação (DD/MM/AAAA)
        if (value.length > 4) {
            value = value.replace(/(\d{2})(\d{2})(\d{1,4})/, "$1/$2/$3");
        } else if (value.length > 2) {
            value = value.replace(/(\d{2})(\d{1,2})/, "$1/$2");
        }

        dobInput.value = value;
    });
});

