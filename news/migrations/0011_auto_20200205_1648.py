# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-05 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_newsletterrecipients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='editor',
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
    ]
