# Generated by Django 4.2.1 on 2023-05-27 16:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0005_alter_car_manufacturer_alter_manufacturer_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="license_number",
            field=models.CharField(max_length=63, unique=True),
        ),
    ]