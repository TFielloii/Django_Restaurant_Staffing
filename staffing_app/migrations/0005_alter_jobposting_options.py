# Generated by Django 4.2 on 2023-05-04 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("staffing_app", "0004_alter_application_applicant_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="jobposting",
            options={"ordering": ["-id"]},
        ),
    ]