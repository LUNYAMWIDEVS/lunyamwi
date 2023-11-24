# Generated by Django 4.2.7 on 2023-11-24 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_problem_gsheet_range_solution_gsheet_range'),
    ]

    operations = [
        migrations.CreateModel(
            name='GsheetSetting',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('spreadsheet_id', models.CharField(max_length=255)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
