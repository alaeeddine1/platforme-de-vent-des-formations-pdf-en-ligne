# Generated by Django 5.0.4 on 2024-06-14 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_rename_formations_res_reservation_formations_reservees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compte_cree',
            old_name='formations_achetees',
            new_name='formations_panier',
        ),
    ]
