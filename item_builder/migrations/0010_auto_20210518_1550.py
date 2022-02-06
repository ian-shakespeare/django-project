# Generated by Django 3.2.2 on 2021-05-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_builder', '0009_auto_20210516_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heroes',
            name='abilities',
        ),
        migrations.AddField(
            model_name='heroes',
            name='E',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='heroes',
            name='Q',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='heroes',
            name='R',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='heroes',
            name='RMB',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='heroes',
            name='passive',
            field=models.CharField(default='', max_length=250),
        ),
    ]
