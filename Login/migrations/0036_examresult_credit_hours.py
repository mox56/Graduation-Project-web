# Generated by Django 4.1.7 on 2024-02-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0035_alter_examresult_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='examresult',
            name='Credit_hours',
            field=models.IntegerField(default=2),
        ),
    ]
