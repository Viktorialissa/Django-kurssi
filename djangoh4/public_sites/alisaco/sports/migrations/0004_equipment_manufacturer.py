# Generated by Django 4.2.1 on 2023-05-25 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.manufacturer'),
        ),
    ]
