# Generated by Django 4.2 on 2023-05-04 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_customuser_is_applicant"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="is_applicant",
        ),
    ]