from django import forms
from .models import Empresa, Setor


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            "razao_social",
            "nome_fantasia",
            "cnpj",
            "ie",
            "im",
            "endereco",
            "telefone",
            "email",
            "type_organizacao",
        ]
        widgets = {
            'razao_social': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Razão Social',
                'required': True,
                'id': 'razao_social'
            }),
            'nome_fantasia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'nome_fantasia',
                'required': True,
                'id': 'nome_fantasia'
            }),
            'cnpj': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CNPJ',
                'required': True,
                'id': 'cnpj'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Endereço',
                'required': True,
                'id': 'endereco'
            }),
            'ie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Inscrição Estadual',
                'required': True,
                'id': 'ie'
            }),
            'im': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Inscrição Munícipal',
                'required': True,
                'id': 'im'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000',
                'required': True,
                'id': 'telefone'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemple@mail.com',
                'required': True,
                'id': 'email'
            }),
            'type_organizacao': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
                'id': 'tipo'
            }),
        }


class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ['nome_setor']
        widgets = {
            'nome_setor': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nome_setor'
            })
        }
