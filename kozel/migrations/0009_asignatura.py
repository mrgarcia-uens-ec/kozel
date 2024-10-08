# Generated by Django 5.0.4 on 2024-06-24 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kozel", "0008_estudiante_curso_alter_curso_nombre"),
    ]

    operations = [
        migrations.CreateModel(
            name="Asignatura",
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
                ("nombre", models.CharField(max_length=200, null=True)),
                ("descripcion", models.CharField(max_length=500, null=True)),
                (
                    "curso",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="kozel.curso",
                    ),
                ),
            ],
        ),
    ]
