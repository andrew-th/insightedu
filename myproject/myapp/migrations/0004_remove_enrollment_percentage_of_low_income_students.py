# Generated by Django 4.2.5 on 2023-11-29 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_enrollment_delete_table1"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="enrollment", name="percentage_of_low_income_students",
        ),
    ]