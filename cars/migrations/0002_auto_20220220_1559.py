# Generated by Django 3.0.7 on 2022-02-20 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 20, 15, 59, 42, 167719)),
        ),
    ]
