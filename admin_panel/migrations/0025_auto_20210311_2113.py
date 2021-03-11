# Generated by Django 3.1.7 on 2021-03-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0024_remove_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='patronymic',
            field=models.CharField(blank=True, max_length=30, verbose_name='Отчество'),
        ),
    ]
