# Generated by Django 5.0.2 on 2024-02-23 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='checked_out',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='product',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='quality_check_pass',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vendor',
        ),
    ]