# Generated by Django 3.1.7 on 2021-03-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0027_profile_pupils'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Имя'),
        ),
    ]
