# Generated by Django 4.2.1 on 2023-05-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0002_remove_driver_license_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="driver",
            name="license_number",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
