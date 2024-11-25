from django import forms
from .models import Colaborador


class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['first_name', 'last_name', 'cpf',
                  'email', 'telefone', 'endereco', 'data_nascimento',
                  'setor', 'cargo', 'matricula', 'data_entrada',
                  'data_demissao', 'is_active']
