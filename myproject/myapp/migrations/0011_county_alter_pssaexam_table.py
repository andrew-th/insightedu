# Generated by Django 4.2.5 on 2023-11-29 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_pssaexam_alter_keystoneexam_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="County",
            fields=[
                ("county_id", models.IntegerField(primary_key=True, serialize=False)),
                ("county_name", models.CharField(max_length=255)),
            ],
            options={"db_table": "district",},
        ),
        migrations.AlterModelTable(name="pssaexam", table=None,),
    ]