# Generated by Django 4.1.7 on 2023-03-25 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examresult',
            name='Mark',
        ),
        migrations.RemoveField(
            model_name='student',
            name='CGPA',
        ),
        migrations.RemoveField(
            model_name='student',
            name='GPA',
        ),
    ]
