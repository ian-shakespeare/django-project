# Generated by Django 3.2.2 on 2021-05-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_builder', '0010_auto_20210518_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='builds',
            name='role',
            field=models.CharField(default='', max_length=10),
        ),
    ]
