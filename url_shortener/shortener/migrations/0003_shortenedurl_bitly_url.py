# Generated by Django 4.2.5 on 2023-09-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_shortenedurl_delete_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenedurl',
            name='bitly_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
