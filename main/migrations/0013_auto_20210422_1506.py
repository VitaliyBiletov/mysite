# Generated by Django 3.1.7 on 2021-04-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210422_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulatorymotorskills',
            name='repeat',
            field=models.IntegerField(blank=True, null=True, verbose_name='Повтори'),
        ),
    ]
