# Generated by Django 4.2.5 on 2023-09-26 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClubUser",
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
                    "first_name",
                    models.CharField(max_length=100, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=100, verbose_name="Last Name"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, verbose_name="User Email Address"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Venue",
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
                ("name", models.CharField(max_length=200, verbose_name="Venue Name")),
                ("address", models.CharField(max_length=300)),
                ("zipcode", models.CharField(max_length=15, verbose_name="Zipcode")),
                (
                    "phone_number",
                    models.CharField(max_length=15, verbose_name="Phone Number"),
                ),
                ("web", models.URLField(verbose_name="Website Address")),
                (
                    "email_address",
                    models.EmailField(max_length=254, verbose_name="Email Address"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=200, verbose_name="Event Name")),
                ("event_date", models.DateTimeField(verbose_name="Event Date")),
                ("manager", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                (
                    "attendees",
                    models.ManyToManyField(blank=True, null=True, to="events.clubuser"),
                ),
                (
                    "venue",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.venue",
                    ),
                ),
            ],
        ),
    ]
