# Generated by Django 3.2.12 on 2022-11-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0020_auto_20221107_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
