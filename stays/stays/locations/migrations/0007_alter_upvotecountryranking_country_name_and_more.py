# Generated by Django 4.2.4 on 2024-01-01 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "locations",
            "0006_challengeattempt_staychallenge_upvotecountryranking_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="upvotecountryranking",
            name="country_name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.CreateModel(
            name="AttemptHasLocationChallenge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "attempt",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="locations.challengeattempt",
                    ),
                ),
                (
                    "challenge",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="locations.staychallenge",
                    ),
                ),
            ],
            options={
                "unique_together": {("attempt", "challenge")},
            },
        ),
    ]