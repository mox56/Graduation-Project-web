# Generated by Django 4.1.7 on 2024-01-17 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0016_alter_examresult_course_code2_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course1',
            new_name='Course',
        ),
        migrations.RemoveField(
            model_name='course3',
            name='department',
        ),
        migrations.RemoveField(
            model_name='course4',
            name='department',
        ),
        migrations.RemoveField(
            model_name='course5',
            name='department',
        ),
        migrations.RenameField(
            model_name='examresult',
            old_name='Course_code1',
            new_name='Course_code',
        ),
        migrations.RenameField(
            model_name='examresult',
            old_name='Mark1',
            new_name='Mark',
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='Course_code2',
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='Course_code3',
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='Course_code4',
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='Course_code5',
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='Mark2',
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='Mark3',
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='Mark4',
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='Mark5',
        ),
        migrations.DeleteModel(
            name='Course2',
        ),
        migrations.DeleteModel(
            name='Course3',
        ),
        migrations.DeleteModel(
            name='Course4',
        ),
        migrations.DeleteModel(
            name='Course5',
        ),
    ]