# Generated by Django 5.1.4 on 2025-02-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_keyword_publication_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to='banners/', verbose_name='Banner Image'),
        ),
    ]
