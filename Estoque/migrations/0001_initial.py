# Generated by Django 5.1.1 on 2024-09-25 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=1, max_digits=10)),
                ('data_entrada', models.DateField()),
                ('data_saida', models.DateField()),
                ('produto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Produto.produto')),
            ],
        ),
    ]