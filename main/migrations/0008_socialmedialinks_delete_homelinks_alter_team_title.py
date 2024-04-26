# Generated by Django 5.0.1 on 2024-04-26 00:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_changeprojectheaderimage_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialMediaLinks",
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
                ("facebook", models.URLField(blank=True, null=True)),
                ("twitter", models.URLField(blank=True, null=True)),
                ("linkedIn", models.URLField(blank=True, null=True)),
                ("google", models.URLField(blank=True, null=True)),
                ("instagram", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="HomeLinks",
        ),
        migrations.AlterField(
            model_name="team",
            name="title",
            field=models.CharField(
                choices=[("ms", "Ms"), ("mrs", "Mrs"), ("mr", "Mr")], max_length=10
            ),
        ),
    ]