# Generated by Django 3.2 on 2021-04-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_customuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
    ]
