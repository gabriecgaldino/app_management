# Generated by Django 5.1.1 on 2024-12-28 00:09

import Usuario.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organização', '0007_remove_cargo_setor_cargo_setor'),
        ('Usuario', '0013_alter_colaborador_cargo_alter_colaborador_setor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cargo', to='Organização.cargo'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, validators=[Usuario.models.Colaborador.validar_cpf]),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='setor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cargo', to='Organização.setor'),
        ),
    ]