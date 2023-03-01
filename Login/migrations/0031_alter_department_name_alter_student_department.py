# Generated by Django 4.1.7 on 2023-02-23 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0030_alter_student_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), (
                'Information Technology', 'Information Technology')], max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.department'),
        ),
    ]
