# Generated by Django 5.0.1 on 2024-02-14 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlshortener',
            old_name='custom_url',
            new_name='short_url',
        ),
    ]