# Generated by Django 4.2.9 on 2024-05-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0022_remove_simplehttpoperatormodel_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dagmodel',
            name='trigger_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dagmodel',
            name='trigger_url_expected_response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
