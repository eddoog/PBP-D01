# Generated by Django 4.1 on 2022-10-29 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskadmin',
            name='is_ended',
        ),
    ]