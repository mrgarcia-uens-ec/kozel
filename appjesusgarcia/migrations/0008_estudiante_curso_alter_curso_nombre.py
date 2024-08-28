# Generated by Django 5.0.4 on 2024-06-20 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appjesusgarcia", "0007_curso"),
    ]

    operations = [
        migrations.AddField(
            model_name="estudiante",
            name="curso",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="appjesusgarcia.curso",
            ),
        ),
        migrations.AlterField(
            model_name="curso",
            name="nombre",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
