# Generated by Django 5.0 on 2024-01-18 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_alter_userprofile_options_userprofile_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cont_comments',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cont_posts',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
