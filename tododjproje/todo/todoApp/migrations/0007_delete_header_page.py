# Generated by Django 4.2.5 on 2023-10-01 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0006_alter_header_page_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Header_page',
        ),
    ]