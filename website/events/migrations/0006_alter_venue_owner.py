# Generated by Django 4.2.5 on 2023-09-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0005_venue_owner_alter_event_manager"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venue",
            name="owner",
            field=models.IntegerField(verbose_name="Venue Owner"),
        ),
    ]
