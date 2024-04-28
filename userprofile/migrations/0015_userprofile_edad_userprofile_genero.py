# Generated by Django 5.0 on 2024-01-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0014_remove_userprofile_cont_comments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='edad',
            field=models.PositiveSmallIntegerField(default=18),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='genero',
            field=models.CharField(choices=[('M', 'Hombre'), ('F', 'Femenino')], default='M', max_length=8),
        ),
    ]