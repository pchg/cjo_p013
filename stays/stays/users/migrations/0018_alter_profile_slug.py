# Generated by Django 4.2.5 on 2023-12-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0017_profile_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="slug",
            field=models.SlugField(blank=True),
        ),
    ]