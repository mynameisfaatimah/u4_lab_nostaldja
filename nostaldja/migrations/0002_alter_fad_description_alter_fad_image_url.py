# Generated by Django 4.2 on 2023-04-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fad',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='fad',
            name='image_url',
            field=models.CharField(max_length=1000),
        ),
    ]
