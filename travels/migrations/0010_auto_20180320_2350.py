# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-20 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0009_auto_20180302_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(),
        ),
    ]
