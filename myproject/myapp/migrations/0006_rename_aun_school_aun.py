# Generated by Django 4.2.5 on 2023-11-29 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_school_remove_enrollment_id_and_more"),
    ]

    operations = [
        migrations.RenameField(model_name="school", old_name="AUN", new_name="aun",),
    ]