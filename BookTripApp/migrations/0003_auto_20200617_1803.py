# Generated by Django 3.0.7 on 2020-06-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookTripApp', '0002_auto_20200617_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(upload_to='media/pics'),
        ),
    ]
