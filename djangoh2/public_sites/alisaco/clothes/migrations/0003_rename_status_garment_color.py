# Generated by Django 4.2.1 on 2023-05-23 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_garment_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='garment',
            old_name='status',
            new_name='color',
        ),
    ]
