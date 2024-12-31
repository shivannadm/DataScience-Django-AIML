# Generated by Django 5.0.2 on 2024-12-21 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='datasets/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PredictionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction_date', models.DateTimeField(auto_now_add=True)),
                ('result_image', models.ImageField(upload_to='images/')),
                ('accuracy', models.FloatField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ai_app.uploadeddataset')),
            ],
        ),
    ]