# Generated by Django 3.1.7 on 2021-03-19 22:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0033_auto_20210319_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата регистрации'),
        ),
    ]
