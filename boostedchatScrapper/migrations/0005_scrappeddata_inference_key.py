# Generated by Django 4.2.9 on 2024-04-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boostedchatScrapper', '0004_alter_scrappeddata_sitemap_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrappeddata',
            name='inference_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
