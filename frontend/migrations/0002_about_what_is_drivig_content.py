# Generated by Django 3.2.8 on 2021-10-06 04:26

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='what_is_drivig_content',
            field=tinymce.models.HTMLField(default=1, verbose_name='Content'),
            preserve_default=False,
        ),
    ]
