# Generated by Django 5.0 on 2023-12-27 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_product_university_alter_product_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='imagenes',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='titulo',
        ),
    ]
