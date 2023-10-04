# Generated by Django 4.2.5 on 2023-10-01 14:21

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0004_header_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header_page',
            name='cate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todoApp.category'),
        ),
        migrations.AlterField(
            model_name='header_page',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name', unique=True),
        ),
    ]