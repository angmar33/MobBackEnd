# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.CharField(max_length=50)),
                ('news_information', models.FileField(upload_to='')),
                ('news_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
