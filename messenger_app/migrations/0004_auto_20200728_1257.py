# Generated by Django 3.0.8 on 2020-07-28 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger_app', '0003_auto_20200728_1247'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='students',
            new_name='student',
        ),
    ]