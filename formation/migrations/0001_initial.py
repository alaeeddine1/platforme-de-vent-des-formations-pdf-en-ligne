# Generated by Django 5.0.4 on 2024-05-01 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image', models.ImageField(upload_to='photo/%y/%m/%j')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
