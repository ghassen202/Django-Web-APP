# Generated by Django 4.1 on 2022-08-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadApp', '0004_remove_workers_age_workers_fich'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='fich',
            field=models.FileField(upload_to=''),
        ),
    ]