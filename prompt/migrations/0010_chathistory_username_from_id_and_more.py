# Generated by Django 5.0.6 on 2024-05-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prompt', '0009_chathistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='chathistory',
            name='username_from_id',
            field=models.CharField(default='12', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chathistory',
            name='username_to_id',
            field=models.CharField(default='23', max_length=255),
            preserve_default=False,
        ),
    ]
