# Generated by Django 5.0 on 2024-01-31 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0031_alter_product_subcategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
    ]