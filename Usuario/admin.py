from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Colaborador

@admin.register(Colaborador)
class CustomUserAdmin(UserAdmin):
    # Adicione os campos personalizados no admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cpf',)}),  # Campos personalizados
    )

    # Exiba campos personalizados na lista de usuários
    list_display = ('username', 'email', 'cpf', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

