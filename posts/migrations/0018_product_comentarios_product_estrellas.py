# Generated by Django 5.0 on 2024-01-18 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_alter_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comentarios',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='estrellas',
            field=models.FloatField(default=0.0),
        ),
    ]
