# Generated by Django 4.1.7 on 2024-01-25 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0032_alter_examresult_id_alter_examresult_student_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examresult',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
