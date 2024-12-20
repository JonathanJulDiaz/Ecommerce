# Generated by Django 5.0 on 2023-12-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_product_options_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='domicilio',
            field=models.CharField(choices=[('NO', 'Solo dentro de la universidad'), ('SI', 'Se hacen domicilios fuera de la universidad')], default='NO', max_length=2),
        ),
        migrations.AddField(
            model_name='product',
            name='inventario',
            field=models.CharField(choices=[('LIMITADO', 'Venta limitada'), ('INFINITO', 'Venta sin limite')], default='LIMITADO', max_length=8),
        ),
        migrations.AddField(
            model_name='product',
            name='university',
            field=models.CharField(choices=[('EAFIT', 'Universidad EAFIT'), ('UDEA', 'Universidad de Antioquia'), ('CES', 'Universidad CES'), ('UPB', 'Universidad Pontificia Bolivariana'), ('ANDES', 'Universidad de los Andes')], default='EAFIT', max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
