# Generated by Django 5.0.4 on 2024-05-02 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='username',
            new_name='usernam',
        ),
    ]
