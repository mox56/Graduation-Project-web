# Generated by Django 4.1.7 on 2024-01-16 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0013_rename_course1_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Course1',
        ),
    ]
