# Generated by Django 4.2.9 on 2024-03-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0013_alter_leadsource_criterion'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramuser',
            name='qualified_keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
