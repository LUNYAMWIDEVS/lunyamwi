# Generated by Django 4.2.9 on 2024-03-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0011_instagramuser_cursor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramuser',
            name='account_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='instagramuser',
            name='cursor',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='instagramuser',
            name='linked_to',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='instagramuser',
            name='outsourced_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='instagramuser',
            name='round',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='instagramuser',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
