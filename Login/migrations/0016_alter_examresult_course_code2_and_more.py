# Generated by Django 4.1.7 on 2024-01-16 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0015_rename_course_code_examresult_course_code1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examresult',
            name='Course_code2',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.course2'),
        ),
        migrations.AlterField(
            model_name='examresult',
            name='Course_code3',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.course3'),
        ),
        migrations.AlterField(
            model_name='examresult',
            name='Course_code4',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.course4'),
        ),
        migrations.AlterField(
            model_name='examresult',
            name='Course_code5',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.course5'),
        ),
    ]
