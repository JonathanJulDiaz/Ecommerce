# Generated by Django 5.0 on 2024-02-21 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_reviewdetails_comentarios_reviewdetails_promedio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewdetails',
            options={'verbose_name': 'Detalle de Reseña', 'verbose_name_plural': 'Detalles de Reseñas'},
        ),
    ]