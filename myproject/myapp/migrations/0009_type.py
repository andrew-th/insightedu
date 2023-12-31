# Generated by Django 4.2.5 on 2023-12-02 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "school_number",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("school_name", models.CharField(max_length=255)),
                ("high_school", models.IntegerField()),
                ("middle_school", models.IntegerField()),
                ("elementary_school", models.IntegerField()),
            ],
        ),
    ]
