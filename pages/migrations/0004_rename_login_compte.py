# Generated by Django 5.0.4 on 2024-05-03 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_usernam_login_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login',
            new_name='compte',
        ),
    ]
