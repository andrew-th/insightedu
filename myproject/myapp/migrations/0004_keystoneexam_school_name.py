# Generated by Django 4.2.5 on 2023-11-30 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_districtform"),
    ]

    operations = [
        migrations.AddField(
            model_name="keystoneexam",
            name="school_name",
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
