# Generated by Django 4.2.7 on 2023-11-24 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_databasecredential'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='database_credentials',
        ),
    ]
