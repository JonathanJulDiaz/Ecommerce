# Generated by Django 5.0 on 2024-03-03 20:09

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0017_remove_userprofile_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about_me',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, max_length=150, null=True),
        ),
    ]
