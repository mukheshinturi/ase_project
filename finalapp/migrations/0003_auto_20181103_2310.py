# Generated by Django 2.1.2 on 2018-11-03 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0002_auto_20181103_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='userlogid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]