# Generated by Django 3.0.7 on 2022-02-20 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20220220_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 20, 16, 5, 24, 466154)),
        ),
    ]
