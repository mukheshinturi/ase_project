# Generated by Django 2.1.2 on 2018-11-04 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0005_auto_20181104_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='rating',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='document',
            name='total_image_downloads',
            field=models.IntegerField(default='0'),
        ),
    ]