# Generated by Django 5.1.6 on 2025-02-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_pays"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="pictures/", verbose_name="Аватар"
            ),
        ),
    ]
