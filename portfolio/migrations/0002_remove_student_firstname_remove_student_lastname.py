# Generated by Django 5.0.1 on 2024-02-06 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lastname',
        ),
    ]