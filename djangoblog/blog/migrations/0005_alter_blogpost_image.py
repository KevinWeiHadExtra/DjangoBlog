# Generated by Django 5.1.7 on 2025-04-08 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='djangoblog/blog/media/default.jpg', upload_to='djangoblog/blog/media'),
        ),
    ]
