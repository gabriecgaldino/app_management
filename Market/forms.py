from django import forms
from Usuario.models import Developer
from Market.models import App
from django.contrib.auth.forms import AuthenticationForm


class DeveloperRegisterForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['email', 'first_name', 'last_name', 'cpf', 'telefone']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome',
                'id': 'first_name', 
                'name': 'first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sobrenome',
                'id': 'last_name',
                'name': 'last_name'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00',
                'id': 'cpf',
                'name': 'cpf'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'mail@exemple.com',
                'id': 'email',
                'name': 'email'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00)0 0000-0000',
                'id': 'telefone',
                'name': 'telefone'
            })
        }
        
class DeveloperLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'placeholder': 'Digite seu email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'placeholder': 'Digite sua senha'
    }))
    
class AppRegisterForm(forms.ModelForm):
    class Meta: 
        model = App
        fields = ['nome', 'descricao', 'versao', 'arquivo_pacote']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do App',
                'id': 'app-name'
            }),
            'versao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Versão',
                'id': 'app-version'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Detalhes do App',
                'id': 'app-details',
                'rows': '3'
            }),
            'arquivo_pacote': forms.FileInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Carregue seu arquivo',
                'id': 'app-path'
            })
        }