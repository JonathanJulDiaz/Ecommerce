# Generated by Django 5.0 on 2024-01-26 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_alter_product_subcategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategoria',
        ),
    ]
