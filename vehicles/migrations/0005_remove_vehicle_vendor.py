# Generated by Django 5.0.2 on 2024-02-23 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_vehicle_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='vendor',
        ),
    ]