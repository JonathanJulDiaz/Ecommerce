# Generated by Django 5.0 on 2024-01-18 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0011_userprofile_cont_comments_userprofile_cont_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cont_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
