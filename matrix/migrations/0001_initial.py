# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_description', models.TextField()),
                ('article_link', models.URLField()),
                ('publish_time', models.CharField(max_length=200)),
                ('publish_time_normal', models.CharField(max_length=200)),
            ],
        ),
    ]