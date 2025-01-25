from django import forms
from Usuario.models import Developer
from django.contrib.auth.forms import AuthenticationForm


class DeveloperRegisterForm(forms.Form):
    class Meta:
        Model = Developer
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