# Generated by Django 4.2.3 on 2023-07-31 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_adv', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advertisments',
            new_name='Advertisements',
        ),
        migrations.AlterModelTable(
            name='advertisements',
            table='advertisements',
        ),
    ]