# Generated by Django 2.1.2 on 2018-11-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='email',
            field=models.CharField(default='a', max_length=150),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='fullname',
            field=models.CharField(default='a', max_length=150),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='userlogid',
            field=models.IntegerField(default='1', primary_key=True, serialize=False),
        ),
    ]