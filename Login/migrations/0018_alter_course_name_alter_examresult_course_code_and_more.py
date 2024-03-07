# Generated by Django 4.1.7 on 2024-01-17 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0017_rename_course1_course_remove_course3_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='examresult',
            name='Course_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.course', to_field='Name'),
        ),
        migrations.AlterModelTable(
            name='course',
            table='Course',
        ),
        migrations.AlterModelTable(
            name='examresult',
            table='Exam',
        ),
    ]