# Generated by Django 5.1.1 on 2024-10-27 03:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produto', '0006_alter_produto_data_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='data_joined',
            field=models.DateField(default=datetime.datetime(2024, 10, 27, 3, 30, 1, 995300, tzinfo=datetime.timezone.utc), max_length=datetime.datetime(2024, 10, 27, 3, 30, 1, 995300, tzinfo=datetime.timezone.utc)),
        ),
    ]