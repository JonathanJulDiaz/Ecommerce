# Generated by Django 5.0 on 2024-02-05 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0040_product_comentarios_alter_product_resena'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='vistas',
        ),
    ]
