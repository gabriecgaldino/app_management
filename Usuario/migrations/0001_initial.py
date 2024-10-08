# Generated by Django 5.1.1 on 2024-09-27 01:31

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Organizações', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
                ('organizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organizações.organizações')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
