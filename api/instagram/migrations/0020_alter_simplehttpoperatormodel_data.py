# Generated by Django 4.2.9 on 2024-04-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0019_instagramuser_attached_salesrep_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplehttpoperatormodel',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
