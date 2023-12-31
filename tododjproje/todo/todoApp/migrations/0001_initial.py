# Generated by Django 4.2.5 on 2023-09-30 07:14

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Oluşturma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Son Güncelleme Tarihi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='todoApp.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='Form_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Adınızı girin')),
                ('text', models.TextField(null=True, verbose_name='Yorumunuz')),
                ('cate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todoApp.todo', verbose_name='Kategori seçiniz')),
            ],
        ),
    ]
