# Generated by Django 4.2.3 on 2023-07-12 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='adhar_number',
            new_name='adharnumber',
        ),
    ]
