# Generated by Django 3.1.4 on 2021-05-21 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtuber',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='youtuber',
            name='last_name',
        ),
    ]
