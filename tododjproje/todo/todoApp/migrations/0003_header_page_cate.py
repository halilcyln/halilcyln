# Generated by Django 4.2.5 on 2023-10-01 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_header_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='header_page',
            name='cate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todoApp.todo', verbose_name=''),
        ),
    ]
