# Generated by Django 3.2.9 on 2021-11-25 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20211124_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='SOME STRING', upload_to='articles/'),
        ),
    ]
