# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-01-29 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='SOME STRING', upload_to='articles/'),
        ),
    ]
