# Generated by Django 5.0.1 on 2024-04-25 22:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_techhive_projects_videofile_alter_team_title_courses"),
    ]

    operations = [
        migrations.RenameField(
            model_name="team",
            old_name="positon",
            new_name="position",
        ),
        migrations.AlterField(
            model_name="team",
            name="title",
            field=models.CharField(
                choices=[("mrs", "Mrs"), ("ms", "Ms"), ("mr", "Mr")], max_length=10
            ),
        ),
    ]
