# Generated by Django 3.1.7 on 2021-03-05 21:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_pupil_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupil',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата'),
        ),
    ]