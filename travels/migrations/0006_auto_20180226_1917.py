# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-26 11:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0005_article_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, upload_to='article_images'),
        ),
    ]
