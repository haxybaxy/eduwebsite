# Generated by Django 5.1.4 on 2025-03-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0025_alter_talk_options_remove_talk_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="talk",
            name="location",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
