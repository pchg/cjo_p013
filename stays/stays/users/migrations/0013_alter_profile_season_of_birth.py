# Generated by Django 4.2.5 on 2023-11-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_alter_profile_about_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="season_of_birth",
            field=models.CharField(default="Spring", max_length=50),
        ),
    ]