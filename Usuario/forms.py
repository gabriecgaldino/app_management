from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Colaborador
from Organização.models import Empresa


class LoginForm(AuthenticationForm):
    class Meta:
        model = Colaborador
        fields = [ 'username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome de usuário',
                'required': True,
                'id': 'username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
                'required': True,
                'id': 'pass'
            }),

        }
        
class ColaboradorForm(forms.ModelForm):
    class Meta:
        OPTIONS = [
            'SIM',
            'NÃO'
        ]
        model = Colaborador
        fields = ['first_name', 'last_name', 'cpf',
                  'email', 'telefone', 'endereco', 'data_nascimento',
                  'setor', 'cargo', 'matricula', 'is_active']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
                'required': True,
                'id': 'first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sobrenome',
                'required': True,
                'id': 'last_name'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00',
                'required': True,
                'id': 'cpf'
            }),
            'email': forms.TextInput(attrs={
                'class':  'form-control',
                'placeholder': 'exemple@mail.com',
                'required': True,
                'id': 'email'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000',
                'id': 'telefone'
            }),
            'endereco': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Endereço', 
                'id': 'endereco',
                'style': 'height: 40px'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'data_nascimento',
                'placeholder': '00/00/0000'
            }),
            'setor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe o setor...',
                'id': 'setor'
            }),
            'cargo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe um cargo...',
                'id': 'cargo'
            }),
            'matricula': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'AB00123',
                'id': 'matricula'
            }),
            'is_active': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'is_active',
                'disabled': True
            }),
        }
