# Generated by Django 3.2.2 on 2021-06-11 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_builder', '0020_alter_discorduser_liked_builds'),
    ]

    operations = [
        migrations.AddField(
            model_name='builds',
            name='author_display_name',
            field=models.CharField(default='User', max_length=25),
        ),
    ]
