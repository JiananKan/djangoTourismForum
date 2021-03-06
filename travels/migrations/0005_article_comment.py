# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-25 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0004_auto_20180225_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('tags', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travels.UserProfile')),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travels.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travels.UserProfile')),
            ],
        ),
    ]
