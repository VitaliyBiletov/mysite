# Generated by Django 3.2 on 2021-04-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_customuser_patronymic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='patronymic',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество'),
        ),
    ]