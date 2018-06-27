# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-13 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsitalia', '0008_auto_20180606_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='slug',
            field=models.SlugField(help_text='Pick the URL fragment following "https://github.com" in the organization URL, e.g ministero-della-documentazione.', max_length=255, unique=True, verbose_name='Slug'),
        ),
    ]