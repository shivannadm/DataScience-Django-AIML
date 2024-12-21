# Generated by Django 5.0.2 on 2024-12-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictionresult',
            name='result_image',
            field=models.ImageField(upload_to='ai_app\\static\\images'),
        ),
        migrations.AlterField(
            model_name='uploadeddataset',
            name='file',
            field=models.FileField(upload_to='media\\datasets'),
        ),
    ]
