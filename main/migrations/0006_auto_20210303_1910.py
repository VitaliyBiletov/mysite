# Generated by Django 3.1.7 on 2021-03-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Название'),
        ),
    ]