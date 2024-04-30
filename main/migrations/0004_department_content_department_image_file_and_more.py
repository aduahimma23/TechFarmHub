# Generated by Django 5.0.1 on 2024-04-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_multimediahivegallery_techhivegallery_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="content",
            field=models.TextField(default="Add New department"),
        ),
        migrations.AddField(
            model_name="department",
            name="image_file",
            field=models.ImageField(
                default="tech.png", unique=True, upload_to="department_images"
            ),
        ),
        migrations.AddField(
            model_name="department",
            name="title",
            field=models.CharField(default="Add title", max_length=255, unique=True),
        ),
    ]
