# Generated by Django 5.0 on 2024-01-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_product_comentarios_product_estrellas'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vistas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
