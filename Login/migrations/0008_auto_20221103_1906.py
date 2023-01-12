# Generated by Django 3.2.12 on 2022-11-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0007_auto_20221029_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='course',
            name='CreditHours',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='examresult',
            name='Mark',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'), ('Z', 'Z')], max_length=50, null=True),
        ),
    ]