# Generated by Django 3.1.7 on 2021-03-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0026_auto_20210316_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pupils',
            field=models.ManyToManyField(to='admin_panel.Pupil'),
        ),
    ]
