# Generated by Django 5.1.1 on 2024-11-25 22:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organização', '0002_setor_cargo'),
        ('Usuario', '0004_remove_colaborador_data_entrada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Organização.empresa'),
            preserve_default=False,
        ),
    ]
