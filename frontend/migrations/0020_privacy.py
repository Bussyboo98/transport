# Generated by Django 3.2.8 on 2021-10-06 21:08

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0019_auto_20211006_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Privacy',
            },
        ),
    ]