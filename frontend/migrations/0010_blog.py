# Generated by Django 3.2.8 on 2021-10-06 15:48

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_auto_20211006_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blg_title', models.CharField(max_length=150, verbose_name='Blog Title')),
                ('blg_image', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Blog Image')),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
