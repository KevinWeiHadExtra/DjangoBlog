# Generated by Django 5.1.7 on 2025-04-22 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_rename_ratings_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost'),
        ),
    ]
