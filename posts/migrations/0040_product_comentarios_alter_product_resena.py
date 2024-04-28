# Generated by Django 5.0 on 2024-02-04 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0039_rename_reseñas_product_resena'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comentarios',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='resena',
            field=models.FloatField(default=0.0),
        ),
    ]
