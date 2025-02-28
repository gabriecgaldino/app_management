# Generated by Django 5.1.1 on 2025-01-25 21:50

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0017_colaborador_is_developer'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador',
            name='is_developer',
        ),
        migrations.AddField(
            model_name='colaborador',
            name='colaborador_groups',
            field=models.ManyToManyField(blank=True, related_name='colaborador', to='auth.group'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='colaborador_permissions',
            field=models.ManyToManyField(blank=True, related_name='colaborador_permission', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='matricula',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('colaborador_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_developer', models.BooleanField(default=False)),
                ('is_developer_approved', models.BooleanField(default=False)),
                ('dev_groups', models.ManyToManyField(blank=True, related_name='developer', to='auth.group')),
                ('dev_permissions', models.ManyToManyField(blank=True, related_name='developer_permission', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('Usuario.colaborador',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
