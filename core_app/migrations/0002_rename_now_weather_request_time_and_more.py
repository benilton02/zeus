# Generated by Django 4.0.6 on 2022-07-22 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='now',
            new_name='request_time',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='request_id',
        ),
    ]
