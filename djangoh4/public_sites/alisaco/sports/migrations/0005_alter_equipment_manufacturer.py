# Generated by Django 4.2.1 on 2023-05-26 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0004_equipment_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='sports.manufacturer'),
        ),
    ]
