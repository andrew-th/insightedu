# Generated by Django 4.2.5 on 2023-11-29 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_rename_aun_school_aun"),
    ]

    operations = [
        migrations.CreateModel(
            name="KeystoneExam",
            fields=[
                (
                    "school_number",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("year", models.IntegerField()),
                ("percentage_bio_proficient", models.FloatField()),
                ("percentage_lit_proficient", models.FloatField()),
                ("percentage_alg_proficient", models.FloatField()),
            ],
            options={"db_table": "district",},
        ),
        migrations.DeleteModel(name="District",),
    ]