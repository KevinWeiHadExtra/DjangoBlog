# Generated by Django 5.1.7 on 2025-04-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
