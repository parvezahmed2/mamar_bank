# Generated by Django 4.2.8 on 2024-02-11 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbankaccount',
            old_name='birthday_date',
            new_name='birth_date',
        ),
    ]
