# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-10 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20200205_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoringaMerch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]
