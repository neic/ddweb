# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-11 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reference",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ship", models.CharField(max_length=200)),
                ("owner", models.CharField(max_length=200)),
                ("place", models.CharField(max_length=200)),
                (
                    "constructionType",
                    models.CharField(
                        choices=[("n", "New Building"), ("r", "Refurbishment")],
                        default="r",
                        max_length=1,
                    ),
                ),
                ("year", models.PositiveIntegerField(blank=True, null=True)),
                ("description", models.TextField(blank=True)),
                ("ongoing", models.BooleanField(default=True)),
                ("beforeDD", models.BooleanField(default=False)),
            ],
            options={"ordering": ["-year", "-id"]},
        )
    ]
