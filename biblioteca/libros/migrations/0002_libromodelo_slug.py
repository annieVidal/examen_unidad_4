# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libromodelo',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
