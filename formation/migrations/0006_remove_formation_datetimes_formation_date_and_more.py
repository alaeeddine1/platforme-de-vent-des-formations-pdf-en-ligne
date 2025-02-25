# Generated by Django 5.0.4 on 2024-05-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0005_remove_formation_nombre_formation_datetimes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formation',
            name='datetimes',
        ),
        migrations.AddField(
            model_name='formation',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='formation',
            name='heure',
            field=models.TimeField(null=True),
        ),
    ]
