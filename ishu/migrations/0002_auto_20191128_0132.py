# Generated by Django 2.2.7 on 2019-11-28 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ishu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='locality',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]