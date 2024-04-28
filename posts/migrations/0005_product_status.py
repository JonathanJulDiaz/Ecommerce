# Generated by Django 5.0 on 2023-12-27 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_product_domicilio_product_inventario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('procesado', 'Procesado'), ('esperando_aprobacion', 'Esperando aprobación'), ('activo', 'Activo'), ('eliminado', 'Eliminado')], default='activo', max_length=50),
        ),
    ]