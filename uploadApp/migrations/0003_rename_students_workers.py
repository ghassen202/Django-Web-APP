# Generated by Django 4.1 on 2022-08-25 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadApp', '0002_alter_students_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='students',
            new_name='workers',
        ),
    ]
