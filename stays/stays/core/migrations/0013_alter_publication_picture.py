# Generated by Django 4.2.5 on 2023-12-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0012_alter_publication_author_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publication",
            name="picture",
            field=models.ImageField(
                default="seals-6627197_1280.jpg",
                max_length=800,
                null=True,
                upload_to="uploads/<django.db.models.fields.SlugField>/%Y/%m/%d/<django.db.models.fields.UUIDField>/picture",
            ),
        ),
    ]