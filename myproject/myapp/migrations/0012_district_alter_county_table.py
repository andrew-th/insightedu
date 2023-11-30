# Generated by Django 4.2.5 on 2023-11-30 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0011_county_alter_pssaexam_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="District",
            fields=[
                ("county_id", models.IntegerField()),
                ("district_name", models.CharField(max_length=255)),
                ("aun", models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={"db_table": "district",},
        ),
        migrations.AlterModelTable(name="county", table=None,),
    ]
