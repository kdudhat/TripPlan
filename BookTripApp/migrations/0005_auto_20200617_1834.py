# Generated by Django 3.0.7 on 2020-06-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookTripApp', '0004_auto_20200617_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(height_field='100px', upload_to='pics'),
        ),
    ]
