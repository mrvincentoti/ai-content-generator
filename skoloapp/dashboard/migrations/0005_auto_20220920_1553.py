# Generated by Django 3.2.13 on 2022-09-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_about_faqs_feedback_home_pricing'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Faqs',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Pricing',
        ),
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
