# Generated by Django 4.2.5 on 2023-11-30 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0012_district_alter_county_table"),
    ]

    operations = [
        migrations.DeleteModel(name="District",),
        migrations.AlterModelTable(name="county", table="district",),
    ]
