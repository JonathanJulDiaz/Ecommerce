# Generated by Django 5.0 on 2024-01-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0015_userprofile_edad_userprofile_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about_me',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
