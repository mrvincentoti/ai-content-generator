# Generated by Django 3.2.13 on 2022-11-30 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20221130_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coverage',
            old_name='coverage_strength',
            new_name='coverage_name',
        ),
        migrations.RenameField(
            model_name='coverage',
            old_name='location_name',
            new_name='strength',
        ),
    ]
