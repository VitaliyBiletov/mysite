# Generated by Django 3.1.7 on 2021-03-07 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_pupil_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pupil',
            name='teacher',
        ),
    ]