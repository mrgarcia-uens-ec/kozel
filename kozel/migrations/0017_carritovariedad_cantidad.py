# Generated by Django 5.0.4 on 2024-09-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kozel", "0016_articulo_producto_mes"),
    ]

    operations = [
        migrations.AddField(
            model_name="carritovariedad",
            name="cantidad",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
