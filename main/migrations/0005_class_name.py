# Generated by Django 3.1.7 on 2021-03-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210303_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]