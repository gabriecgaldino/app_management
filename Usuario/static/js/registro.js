var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder = 'Primeiro Nome'
form_fields[2].placeholder = 'Último Nome'
form_fields[3].placeholder = 'E-mail'
form_fields[4].placeholder = 'CPF'
form_fields[5].placeholder = 'Telefone'
form_fields[6].placeholder = 'Senha'
form_fields[7].placeholder = 'Confirme a Senha'

for (var field in form_fields) {
    form_fields[field].className += 'form-control'
}

var select = document.getElementsByTagName('select')

select[0].className += 'form-control'