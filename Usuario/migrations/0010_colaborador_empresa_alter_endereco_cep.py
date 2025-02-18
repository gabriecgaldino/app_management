# Generated by Django 5.1.1 on 2024-11-28 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organização', '0002_setor_cargo'),
        ('Usuario', '0009_endereco_pais'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='empresa',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Organização.empresa'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=9),
        ),
    ]
