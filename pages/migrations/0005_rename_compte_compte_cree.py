# Generated by Django 5.0.4 on 2024-05-03 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_rename_login_compte'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='compte',
            new_name='compte_cree',
        ),
    ]
